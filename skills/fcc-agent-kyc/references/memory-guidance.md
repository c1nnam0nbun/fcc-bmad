# Memory Guidance: fcc-agent-kyc

As a compliance expert, your memory is your audit trail. Discipline is mandatory.

## Active Session: The Daily Log

- Every significant finding or jurisdictional decision MUST be appended to the shared daily log: `_bmad/memory/fcc/daily/YYYY-MM-DD.md`.
- Format: `[KYC][Jurisdiction:XX][Client:YY] Finding description. Citations: [Ref1], [Ref2].`
- This allows the `fcc-agent-architect` and future specialists to "hear" your analysis.

## Session Close: Curation

Before finishing any session:
1. **Update Client Profiles:** If you performed an analysis for a specific client, update or create `_bmad/memory/fcc/clients/{client_id}.md`.
2. **Update Index:** If a new client was reviewed, ensure they are listed in `_bmad/memory/fcc/index.md` with a `KYC_COMPLETE` or `KYC_PENDING` status.
3. **Identify Patterns:** If you noticed a new regulatory pattern (e.g., a recurring gap in Singaporean onboarding), note it in `_bmad/memory/fcc/curated/regulatory_patterns.md`.

## Memory Ethics

- Never store PII (Personally Identifiable Information) directly in the log if a client ID can be used instead.
- Stick to facts and citations. Do not store conversational "fluff."
