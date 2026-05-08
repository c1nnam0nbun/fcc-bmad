---
name: Regulatory Gap Finder
code: regulatory_gap_finder
description: Compare provided client documents against the ideal regulatory KYC checklist.
---

# Regulatory Gap Finder

## Outcome
A comprehensive checklist of missing, expired, or non-compliant documents required for the specific KYC onboarding process.

## Input
- Current client onboarding documents (PDFs, images, data extracts).
- Regulatory requirements from RAG.

## Action
1. Compare provided documents against the "Ideal" KYC checklist found in the RAG database for the relevant jurisdiction.
2. Verify document validity (e.g., expiry dates, certified copies).
3. Identify missing mandatory elements (e.g., Proof of Address, UBO declaration).

## What Success Looks Like
- A "Missing Documents" table with clear explanations for why each is needed.
- Citations to the specific regulatory clause requiring the document.

## Memory Integration
- Update the client's profile in `{project-root}/_bmad/memory/fcc/clients/` with the current gap status.
