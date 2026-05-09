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

`/fcc-setup` command will create necessary folder structure, initialize database, and **run setup.py script in every fcc-\* skill**.

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

The documents can be tagged with **jurisdiction** (EU, Global, Singapore etc.) and **domain** (KYC, EDD, AML etc.). Multiple of them may be attached, separated by comma. Default values are **Global** for jurisdiction and **General** for domain. When querying, the agents may apply jurisdiction and domain filters as per user's request or their own reasoning.

Ingestion may take some time, depending on the size of the documents, you've been warned.
