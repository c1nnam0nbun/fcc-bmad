import argparse
from pathlib import Path
from database import FCCDatabase

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FCC Database Service")
    parser.add_argument("--status", action="store_true", help="Get DB status")
    parser.add_argument("--query", type=str, help="Query text to search in DB")
    parser.add_argument("--n_results", type=int, default=5, help="Number of results to return")
    parser.add_argument("--ingest", type=str, help="Path to file or folder to ingest")
    parser.add_argument("--jurisdiction", type=str, help="Jurisdiction tag")
    parser.add_argument("--domain", type=str, help="Domain tag (e.g., KYC, AML)")
    parser.add_argument("--language", type=str, help="Document language")
    parser.add_argument("--reset", action="store_true", help="Delete and recreate the collection")
    
    args = parser.parse_args()
    fcc_db = FCCDatabase()

    if args.reset:
        print("Resetting database collection 'fcc_regulatory_docs'...")
        try:
            fcc_db.client.delete_collection("fcc_regulatory_docs")
            fcc_db.collection = fcc_db.client.create_collection(
                name="fcc_regulatory_docs",
                embedding_function=fcc_db.ef
            )
            print("Collection reset successfully.")
        except Exception as e:
            print(f"Error resetting collection: {e}")
            # Fallback: just ensure it exists
            fcc_db.collection = fcc_db.client.get_or_create_collection(
                name="fcc_regulatory_docs",
                embedding_function=fcc_db.ef
            )

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
        print(results)
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
            fcc_db.ingest_file(
                path, 
                args.jurisdiction if args.jurisdiction else "Global", 
                args.domain if args.domain else "General", 
                args.language if args.language else "English"
            )
        elif path.is_dir():
            for f in path.glob("*.*"):
                if f.suffix.lower() in [".pdf", ".docx", ".md", ".txt"]:
                    fcc_db.ingest_file(f, args.jurisdiction, args.domain, args.language)
