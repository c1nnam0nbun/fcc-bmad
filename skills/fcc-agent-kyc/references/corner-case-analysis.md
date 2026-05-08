# Corner-Case & Nuance Analysis

## Overview
Provide an expert regulatory opinion on complex KYC scenarios, such as decentralized entities (DAOs), complex multi-jurisdictional ownership, or high-risk jurisdictions.

## What Success Looks Like
A detailed expert opinion containing:
1. **Scenario Decomposition:** Identifying the core regulatory friction points.
2. **Precedent & Guidance Search:** Finding relevant FATF/ESMA/local guidance on the specific nuance.
3. **Risk Mitigation Strategy:** Practical steps to manage or mitigate the identified risks.
4. **Final Recommendation:** A clear "Approve with Conditions" or "Reject" recommendation based on regulatory risk appetite.

## Execution Steps
1. **Scenario Intake:** Deep dive into the provided complex scenario.
2. **Multi-Query Research:** Run multiple targeted queries to the `fcc-database-service`.
   ```bash
   python skills/fcc-database-service/scripts/service.py --query "[SPECIFIC_NUANCE] regulatory treatment" --jurisdiction "[JURISDICTION]"
   ```
3. **Synthesize Opinion:** Draft the expert opinion, focusing on the intersection of technology and regulation.
4. **Peer Alignment:** Cross-reference findings with the shared FCC memory for similar cases.
