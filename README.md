# Fintech Crypto Compliance (FCC) Module for BMad

A self-contained, expert-agent suite for AML/CTF and regulatory decision-making in the fintech and crypto space.

## Features
- **Self-Contained RAG:** Local ChromaDB and Sentence-Transformers embedded within the module.
- **Expert Agents:** 
    - `fcc-agent-kyc`: Meticulous auditor for KYC/CDD procedures.
    - `fcc-agent-architect`: Meta-agent to scaffold new specialists.
- **Consensus Workflow:** Orchestrates multi-agent "Consensus Meetings" with structured audit trails.
- **Project-Agnostic:** Designed to be installed in any BMad-enabled workspace.

## Installation

### 1. Prerequisites
Ensure you have Python 3.9+ installed and BMad CLI configured in your project.

### 2. Install Dependencies
Navigate to the module directory and install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Initialize the Module
Run the unified setup skill to discover and initialize the database and all agents:
```bash
# In BMad CLI:
/fcc-setup
```
*Alternatively, run the setup script directly:*
```bash
python skills/fcc-setup/scripts/setup.py
```

## Usage

### Ingesting Documents
Ingest regulatory PDFs or Word docs with jurisdictional metadata:
```bash
python skills/fcc-database-service/scripts/service.py --ingest "./docs/my_regs/" --jurisdiction "Bulgaria" --domain "KYC"
```

### Running a Consensus Review
Trigger a multi-agent review for a client:
```bash
# In BMad CLI:
/fcc-consensus review client_id_123 --agents kyc
```

## Migration: Moving to an Externally Hosted Database

The FCC module is designed for portability. To move from a local bundled database to a remote server (e.g., a central Qdrant or Chroma server):

1. **Update Configuration:**
   Modify your `{project-root}/_bmad/config.user.toml` to override the internal database URL:
   ```toml
   [modules.fcc]
   vector_db_url = "http://your-remote-db-server:8000"
   use_local_db = false
   ```

2. **Update Database Service:**
   Modify `skills/fcc-database-service/scripts/service.py` to use `chromadb.HttpClient` instead of `PersistentClient` when `use_local_db` is false.

3. **Update Agent Tools:**
   Ensure the environment variable `FCC_VDB_URL` is set in your deployment environment. The agents are designed to check this variable before falling back to the local path.

## Project Structure
- `skills/fcc-database-service`: The RAG backbone.
- `skills/fcc-agent-architect`: The meta-agent for suite expansion.
- `skills/fcc-agent-kyc`: The KYC specialist.
- `skills/fcc-consensus-workflow`: The orchestrator.
- `_bmad/memory/fcc/`: Shared memory root (Daily logs, Client profiles, Internal storage).
