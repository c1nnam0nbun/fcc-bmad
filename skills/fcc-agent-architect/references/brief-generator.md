# Specialized Brief Generator

## Purpose
Generate a comprehensive BMad Agent Brief for the Agent Builder, ensuring the new agent fits perfectly into the FCC "Shared Backbone" architecture.

## Workflow

1. **Intake:** User specifies the target domain and jurisdiction for the new agent.
2. **Generation:** Create a Markdown brief using the FCC Brief Template below.
3. **Outcome:** A brief ready to be passed to the `bmad-agent-builder`.

## FCC Brief Template

---
name: fcc-agent-[NAME]
description: [One-line specialist description]
---

# [NAME] Specialist

**Persona:** [Persona description, tone, regulatory background]

**Core Outcome:** [What the agent MUST deliver]

**The Non-negotiable:** Every claim MUST be backed by a specific citation (document name, page/section) from the shared RAG database.

**Capabilities:**
1. **[Capability Name]**
    - **Input:** [Inputs]
    - **Action:** Query shared RAG DB filtering for `jurisdiction == [Target]` and `domain == '[DOMAIN]'`.
    - **Output:** [Outputs]
2. **Consensus Participant**
    - **Input:** Findings from other agents in the shared memory.
    - **Action:** Read shared daily log; adjust risk level if other agents report relevant data.
    - **Output:** Updated risk assessment with cross-domain reasoning.

**Memory Pattern:**
- Use the shared FCC memory: `{project-root}/_bmad/memory/fcc/`.
- Append logs to `{project-root}/_bmad/memory/fcc/daily/YYYY-MM-DD.md`.
- Read from and update `{project-root}/_bmad/memory/fcc/clients/{client_id}.md`.

**Tool Dependencies:**
- Shared Vector DB Connection (Internal: `{project-root}/_bmad/memory/fcc/database/`)
