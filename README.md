# Fintech Crypto Compliance (FCC) Module for BMad

A self-contained, expert-agent suite for AML/CTF and regulatory decision-making in the fintech and crypto space.

## Features
- **Self-Contained RAG:** Local ChromaDB and Sentence-Transformers embedded within the module.
- **Expert Agents:** 
    - `fcc-agent-kyc`: Meticulous auditor for KYC/CDD procedures.
    - `fcc-agent-architect`: Meta-agent to identify gaps and build new specialists.
- **Consensus Workflow:** Orchestrates multi-agent reviews with structured audit trails.
- **Zero-Touch Setup:** One command to install dependencies and initialize the suite.

## Installation & Setup

Everything is handled through the BMad CLI. Simply run:

```bash
/fcc-setup
```

This command will:
1.  **Install Dependencies:** Automatically install all required Python packages (`chromadb`, `sentence-transformers`, etc.).
2.  **Initialize Database:** Set up the local Vector DB and shared memory structures.
3.  **Configure Agents:** Ensure all agents are aware of the shared backbone.

## Usage

### Expanding the Suite
To add a new specialist or analyze a new regulation (e.g., MiCA):
```bash
/fcc-agent-architect Create an agent that will specialize in KYC procedure: requirements, nuances, corner cases etc
```

### Running a Consensus Review
Trigger a multi-agent review for a client:
```bash
/fcc-consensus review KYC workflow for EU region --agents kyc aml
```
`--agents` is optional and allows you to specify, which agents should take part in the discussion. All available `fcc-agent-*`s will be used if omitted.

### Ingesting Documents
```bash
/fcc-database-service ingest @docs/, tag them with domains KYC and General
```

You may also use script directly

```bash
python skills/fcc-database-service/scripts/service.py --ingest "./docs/my_regs/" --jurisdiction "Global" --domain "KYC, General"
```

All agents have access to `fcc-database-service` skill, so you may also ask specific agent to ingest the documents.

## Architecture
The module uses a **Shared Backbone** pattern:
- **`fcc-database-service`**: The central RAG engine.
- **`fcc-agent-architect`**: The meta-agent (assets/PLAN.md contains the roadmap).
- **`_bmad/memory/fcc/`**: Shared daily logs and client state.
