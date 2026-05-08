# Due Diligence Design (CDD/EDD)

## Overview
Design a risk-based due diligence procedure (Standard Customer Due Diligence or Enhanced Due Diligence) tailored to a specific customer profile or risk indicator.

## What Success Looks Like
A step-by-step procedure including:
1. **Risk Profiling:** Identification of specific risk factors (Jurisdictional, Product, Delivery Channel, Customer).
2. **Verification Steps:** Detailed actions for verifying UBOs, control structures, and complex ownership.
3. **Crypto-Specific Checks:** Verification of wallet ownership (proof-of-control) and source of crypto assets.
4. **Ongoing Monitoring:** Recommended frequency and triggers for periodic review.

## Execution Steps
1. **Input Analysis:** Review the customer risk profile or high-risk indicators provided.
2. **Retrieve Standards:** Query the database for CDD/EDD standards relevant to the risk profile.
   ```bash
   python skills/fcc-database-service/scripts/service.py --query "Enhanced Due Diligence requirements for [RISK_FACTOR]" --jurisdiction "[JURISDICTION]"
   ```
3. **Draft Procedure:** Create the step-by-step verification plan.
4. **Validation:** Check the plan against FATF and local AMLD standards for compliance.
