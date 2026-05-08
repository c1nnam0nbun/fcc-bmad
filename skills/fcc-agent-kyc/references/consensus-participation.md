# Consensus Participation

## Overview
Participate in multi-agent compliance reviews by incorporating findings from other domains (e.g., Sanctions, Transaction Monitoring) into a unified KYC risk assessment.

## What Success Looks Like
An updated KYC assessment that:
1. **Aggregates Findings:** Lists relevant data points from other FCC agents.
2. **Identifies Correlations:** Surfaces how a transaction monitoring alert might impact the KYC risk level (e.g., SoW mismatch).
3. **Drafts Consensus Memo:** A final risk statement for the FCC module's daily log.

## Execution Steps
1. **Scan Shared Memory:** Read the daily log and client files in `{project-root}/_bmad/memory/fcc/`.
2. **Cross-Domain Analysis:** Evaluate how other domain findings (Sanctions hits, TM alerts) change the KYC risk profile.
3. **Update Client File:** Update `{project-root}/_bmad/memory/fcc/clients/{client_id}.md` with the new assessment.
4. **Log Contribution:** Append a summary of findings to `{project-root}/_bmad/memory/fcc/daily/YYYY-MM-DD.md`.
