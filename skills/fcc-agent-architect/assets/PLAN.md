# Fintech Crypto Compliance (FCC) Module Plan

---
title: Fintech Crypto Compliance Module Plan
module_name: Fintech Crypto Compliance
module_code: fcc
description: A suite of expert agents for AML/CTF and regulatory decision-making in the fintech/crypto space using local RAG.
status: complete
created: 2026-05-07
updated: 2026-05-07
---

## Summary
The FCC module provides a self-contained environment for automated compliance audits. It features a shared RAG backbone (ChromaDB), a meta-agent for suite expansion, and a consensus-based decision workflow.

## Components
- **`fcc-database-service`**: Internal Vector DB and ingestion.
- **`fcc-agent-architect`**: Meta-agent for adding new experts.
- **`fcc-consensus-workflow`**: Multi-agent orchestrator.

## Architectural Mandates (from README)
- **Shared Backbone:** All agents must leverage the shared Vector DB and memory structure.
- **Expert Atomicity:** Each agent should have a clear, specialized domain of expertise.
- **Zero-Touch Setup:** One command (`/fcc-setup`) installs dependencies and initializes the suite.

## Migration & Portability
The module is designed for portability. To move from a local bundled database to a remote server (e.g., a central Qdrant or Chroma server):
1. **Update Configuration:** Modify `{project-root}/_bmad/config.user.toml` to override the internal database URL.
2. **Update Database Service:** Modify `skills/fcc-database-service/scripts/service.py` to use `chromadb.HttpClient`.
3. **Environment Variables:** Use `FCC_VDB_URL` as a fallback.
