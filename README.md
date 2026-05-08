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

1. Begin BMad Method interactive installation
   ```bash
   mkdir your_project
   cd your_project
   npx bmad-method@latest install
   ```
2. When asked to select official modules to install, make sure to have **BMad Builder** selected. **It is required for `fcc-agent-architect` to create proper BMad agents.**
3. When prompted to install custom module select `Yes` and paste link to this repo
   ```
   https://github.com/c1nnam0nbun/fcc-bmad
   ```
4. Once installed, run `/fcc-setup`

Alternatively, you may use non-interactive mode
1. Run BMad Method non-interactive installation
   ```bash
   mkdir your_project
   cd your_project
   npx bmad-method@latest install --directory . --modules bmm,bmb --custom-source https://github.com/c1nnam0nbun/fcc-bmad --tools <tool_names> --yes
   ```
   Substitute `<tool_names>` for your tools (gemini, claude-code etc.). List all available tools with `npx bmad-method@latest install --list-tools`
2. Once installed, run `/fcc-setup`

## Usage

### Expanding the Suite
To add a new specialist or analyze a new regulation (e.g., MiCA):
```
/fcc-agent-architect Create an agent that will specialize in KYC procedure: requirements, nuances, corner cases etc
```

### Running a Consensus Review
Trigger a multi-agent review for a client:
```
/fcc-consensus review KYC workflow for EU region --agents kyc aml
```
`--agents` is optional and allows you to specify, which agents should take part in the discussion. All available `fcc-agent-*`s will be used if omitted.

### Ingesting Documents
At this moment the suite is able to work with PDF (text, no OCR), DOCX, TXT and MD files. Place files into the directory and pass the directory to the `fcc-database-service`.

```
/fcc-database-service ingest @docs/, tag them with domains KYC and General
```

You may also use script directly

```bash
python skills/fcc-database-service/scripts/service.py --ingest "./docs/my_regs/" --jurisdiction "Global" --domain "KYC, General"
```

All agents have access to `fcc-database-service` skill, so you may also ask specific agent to ingest the documents.

### FCC Database Service Deep Dive

The `fcc-database-service` is the RAG (Retrieval-Augmented Generation) engine of the suite. It uses a local ChromaDB instance and `all-MiniLM-L6-v2` embeddings.

#### Supported Formats
- **PDF** (text-based)
- **DOCX**
- **Markdown** (.md)
- **Text** (.txt)

#### Commands & Usage

The service can be controlled via the `/fcc-database-service` skill or directly via Python:

**1. Ingesting Documents**
Ingest a single file or an entire directory.
```bash
python skills/fcc-database-service/scripts/service.py --ingest "./path/to/docs" --jurisdiction "EU" --domain "KYC, AML" --language "English"
```

**2. Querying**
Search the database with optional metadata filtering.
```bash
python skills/fcc-database-service/scripts/service.py --query "What are the KYC requirements for crypto exchanges?" --jurisdiction "EU" --domain "KYC"
```

**3. Updating Metadata**
Add or remove jurisdiction and domain tags from already ingested documents. This is useful for refining document categorization without re-ingesting.
- **Add tags:**
  ```bash
  python skills/fcc-database-service/scripts/service.py --update "regulation_v1.pdf" --domain "Sanctions" --action add
  ```
- **Remove tags:**
  ```bash
  python skills/fcc-database-service/scripts/service.py --update "regulation_v1.pdf" --jurisdiction "Global" --action remove
  ```

**4. Checking Status**
View the total number of chunks and a list of all ingested documents with their current tags.
```bash
python skills/fcc-database-service/scripts/service.py --status
```

**5. Resetting the Database**
Clear the entire collection (use with caution).
```bash
python skills/fcc-database-service/scripts/service.py --reset
```

#### Metadata Handling
The documents can be tagged with **jurisdiction** (EU, Global, Singapore etc.) and **domain** (KYC, EDD, AML etc.). Multiple values can be provided as a comma-separated string.
- **Default Jurisdiction:** `Global`
- **Default Domain:** `General`

When querying, filters use an "includes" logic: if a document has tags "KYC, AML", it will match a query filtered for "KYC".

## Architecture
The module uses a **Shared Backbone** pattern:
- **`fcc-database-service`**: The central RAG engine.
- **`fcc-agent-architect`**: The meta-agent (assets/PLAN.md contains the roadmap).
- **`_bmad/memory/fcc/`**: Shared daily logs and client state.
