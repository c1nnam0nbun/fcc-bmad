---
name: Consensus Participant
code: consensus_participant
description: Adjust KYC risk assessment based on findings from other FCC agents in shared memory.
---

# Consensus Participant

## Outcome
An updated, cross-domain risk assessment that incorporates findings from other specialists (e.g., Sanctions, Sanctions & PEP Screener).

## Input
- Current KYC risk findings.
- Shared daily log: `{project-root}/_bmad/memory/fcc/daily/YYYY-MM-DD.md`.
- Shared client profile: `{project-root}/_bmad/memory/fcc/clients/client_id.md`.

## Action
1. Scan shared memory for findings related to the client being reviewed.
2. Identify cross-domain risks (e.g., Sanctions specialist flags the client's home city as high-risk, which elevates the KYC EDD requirement).
3. Synthesize findings into the final KYC report.

## What Success Looks Like
- KYC risk levels are adjusted dynamically based on holistic evidence.
- "Cross-domain Reasoning" section explicitly stating which other agent findings influenced the decision.

## Memory Integration
- Append the synthesized consensus observation to the daily shared log with the tag `[KYC:Consensus]`.
