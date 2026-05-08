# Regulatory KYC Mapping

## Overview
Generate a detailed map of KYC requirements for a specific jurisdiction and entity type (e.g., Natural Person, Legal Entity, VASP).

## What Success Looks Like
A structured report containing:
1. **Identification Requirements:** Specific documents and data points required for initial identification.
2. **Verification Standards:** Acceptable methods for verifying identity and address.
3. **Source of Wealth/Funds (SoW/SoF):** Triggers and requirements for financial disclosure.
4. **Jurisdictional Specifics:** Any local nuances (e.g., specific EU member state requirements).

## Execution Steps
1. **Define Scope:** Confirm the target jurisdiction and entity type.
2. **Query Database:** Use the `fcc-database-service` to retrieve relevant regulatory text.
   ```bash
   python skills/fcc-database-service/scripts/service.py --query "KYC requirements for [ENTITY_TYPE] in [JURISDICTION]" --jurisdiction "[JURISDICTION]"
   ```
3. **Analyze & Map:** Synthesize the raw regulatory data into the required outcome sections.
4. **Cite Evidence:** Ensure every requirement is linked to a specific section of the retrieved regulation.
