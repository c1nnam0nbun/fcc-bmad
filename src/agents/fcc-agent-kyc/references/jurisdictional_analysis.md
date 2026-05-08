---
name: Jurisdictional KYC Analysis
code: jurisdictional_analysis
description: Filter and analyze regulatory documents for a specific jurisdiction to determine KYC requirements.
---

# Jurisdictional KYC Analysis

## Outcome
A detailed report of KYC requirements for a specific entity/individual in a target jurisdiction, mapping regulatory mandates to the provided data and highlighting gaps or red flags.

## Input
- Entity/Individual details (name, type, country of residence/incorporation).
- Target Jurisdiction (e.g., "Germany", "Singapore").

## Action
1. Filter the shared RAG database using:
   - `jurisdiction == [Target Jurisdiction]`
   - `domain == 'KYC'`
2. Extract specific CDD (Customer Due Diligence) and EDD (Enhanced Due Diligence) requirements.
3. Compare requirements against the provided entity details.

## What Success Looks Like
- Every requirement cited with document name and section/page.
- Clear distinction between "Standard" and "Enhanced" due diligence.
- Neutral, evidence-based assessment.

## Memory Integration
- Append findings to the client's record in `{project-root}/_bmad/memory/fcc/clients/`.
- Log the analysis start and end in the daily shared log `{project-root}/_bmad/memory/fcc/daily/YYYY-MM-DD.md`.
