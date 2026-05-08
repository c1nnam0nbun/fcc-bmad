import os
import argparse
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions
from docx import Document
import pypdf

def find_project_root(start_path: Path) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / "_bmad").is_dir():
            return current
        current = current.parent
    return Path.cwd()

class FCCDatabase:
    def __init__(self):
        project_root = find_project_root(Path(__file__))
        self.db_path = str(project_root / "_bmad" / "memory" / "fcc" / "database")
        self.model_path = str(project_root / "_bmad" / "memory" / "fcc" / "models")
        
        os.makedirs(self.db_path, exist_ok=True)
        os.makedirs(self.model_path, exist_ok=True)

        # Initialize Embedding Function (Local)
        # Note: In a real environment, this might download the model if not found in model_path
        self.ef = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2",
            cache_folder=self.model_path
        )
        
        # Initialize Chroma Client
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(
            name="fcc_regulatory_docs",
            embedding_function=self.ef
        )

    def ingest_file(self, file_path: Path, jurisdiction: str, domain: str, language: str):
        print(f"Ingesting: {file_path.name}...")
        text = ""
        if file_path.suffix.lower() == ".pdf":
            with open(file_path, "rb") as f:
                pdf = pypdf.PdfReader(f)
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
        elif file_path.suffix.lower() == ".docx":
            doc = Document(str(file_path))
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif file_path.suffix.lower() in [".md", ".txt"]:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            print(f"Unsupported file type: {file_path.suffix}")
            return

        # Simple chunking by paragraph/lines for now
        chunks = [c.strip() for c in text.split("\n\n") if len(c.strip()) > 50]
        
        ids = [f"{file_path.name}_{i}" for i in range(len(chunks))]
        metadatas = [{
            "source": file_path.name,
            "jurisdiction": jurisdiction,
            "domain": domain,
            "language": language
        } for _ in range(len(chunks))]

        self.collection.add(
            documents=chunks,
            ids=ids,
            metadatas=metadatas
        )
        print(f"Success: Added {len(chunks)} chunks from {file_path.name}")

    def query(self, query_text: str, jurisdiction: str = None, domain: str = None, n_results: int = 5):
        # We query the DB and then filter client-side for multi-value matches
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results * 3 # Fetch more to account for post-filtering
        )
        
        filtered_docs = []
        filtered_ids = []
        filtered_metadatas = []
        filtered_distances = []

        for i, meta in enumerate(results['metadatas'][0]):
            j_match = True if not jurisdiction else jurisdiction in [j.strip() for j in meta.get("jurisdiction", "").split(",")]
            d_match = True if not domain else domain in [d.strip() for d in meta.get("domain", "").split(",")]
            
            if j_match and d_match:
                filtered_docs.append(results['documents'][0][i])
                filtered_ids.append(results['ids'][0][i])
                filtered_metadatas.append(meta)
                if results.get('distances') and results['distances'][0]:
                    filtered_distances.append(results['distances'][0][i])
                if len(filtered_docs) >= n_results:
                    break

        return {
            "documents": [filtered_docs],
            "ids": [filtered_ids],
            "metadatas": [filtered_metadatas],
            "distances": [filtered_distances] if results.get('distances') else None
        }

    def get_status(self):
        count = self.collection.count()
        # Retrieve all metadata to list documents
        results = self.collection.get(include=["metadatas"])
        docs = {}
        if results['metadatas']:
            for meta in results['metadatas']:
                source = meta.get("source", "unknown")
                if source not in docs:
                    docs[source] = {
                        "jurisdiction": meta.get("jurisdiction", ""),
                        "domain": meta.get("domain", "")
                    }
        return {
            "document_count": count,
            "db_path": self.db_path,
            "model_path": self.model_path,
            "documents": docs
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FCC Database Service")
    parser.add_argument("--status", action="store_true", help="Get DB status")
    parser.add_argument("--query", type=str, help="Query text to search in DB")
    parser.add_argument("--n_results", type=int, default=5, help="Number of results to return")
    parser.add_argument("--ingest", type=str, help="Path to file or folder to ingest")
    parser.add_argument("--jurisdiction", type=str, default="Global", help="Jurisdiction tag")
    parser.add_argument("--domain", type=str, default="General", help="Domain tag (e.g., KYC, AML)")
    parser.add_argument("--language", type=str, default="English", help="Document language")
    
    args = parser.parse_args()
    fcc_db = FCCDatabase()

    if args.status:
        status = fcc_db.get_status()
        print(f"Documents in DB: {status['document_count']}")
        print(f"Data Location: {status['db_path']}")
        if status['documents']:
            print("\nDocuments:")
            for name, meta in status['documents'].items():
                print(f" - {name} | Jurisdictions: {meta['jurisdiction']} | Domains: {meta['domain']}")
    
    if args.query:
        results = fcc_db.query(args.query, args.jurisdiction, args.domain, args.n_results)
        print(f"\nQuery Results for: '{args.query}'")
        if results['documents'] and results['documents'][0]:
            for i, doc in enumerate(results['documents'][0]):
                meta = results['metadatas'][0][i]
                print(f"\nResult {i+1} [{meta.get('source', 'unknown')}]:")
                print(f"  {doc[:200]}...")
        else:
            print("No results found.")
    
    if args.ingest:
        path = Path(args.ingest)
        if path.is_file():
            fcc_db.ingest_file(path, args.jurisdiction, args.domain, args.language)
        elif path.is_dir():
            for f in path.glob("*.*"):
                if f.suffix.lower() in [".pdf", ".docx", ".md", ".txt"]:
                    fcc_db.ingest_file(f, args.jurisdiction, args.domain, args.language)
