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
- **`fcc-agent-kyc`**: Specialist for KYC/CDD.
- **`fcc-consensus-workflow`**: Multi-agent orchestrator.

## Installation
Refer to the root `README.md` for installation and dependency management.
