---
name: fcc-consensus-workflow
description: Orchestrates multi-agent compliance reviews using the Consensus Meeting pattern. Trigger: "/fcc-consensus review <client_id>"
---

# FCC Consensus Workflow

## Overview

This skill implements the "Consensus Meeting" pattern for the Fintech Crypto Compliance (FCC) module. It orchestrates a three-phase analysis where multiple expert agents (KYC, Sanctions, etc.) perform individual RAG-based analysis, engage in cross-talk via shared memory, and produce a synthesized, high-quality Compliance Report.

## Activation

### Step 1: Resolve Configuration
Load module configuration from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root and `fcc` section).
Key paths:
- `fcc_memory_root`: `{project-root}/_bmad/memory/fcc/`
- `fcc_daily_logs`: `{fcc_memory_root}daily/`
- `fcc_client_profiles`: `{fcc_memory_root}clients/`

### Step 2: Set Context
1. **Extract `client_id`**: From the trigger command (e.g., `/fcc-consensus review client_123` -> `client_123`).
2. **Filter Agents (Optional)**: If the command includes an `--agents` flag (e.g., `--agents kyc,mica`), restrict Phase 1 and 2 to only those specific agents. If no flag is provided, default to all installed expert agents in the `fcc` namespace.

## Phase 1: Individual Analysis

In this phase, the selected expert agents are invoked sequentially to perform their specialized domain analysis.

1.  **Iterate through Target Agents**:
    - For each agent (e.g., `fcc-agent-kyc`, `fcc-agent-mica`):
        - **Action**: Perform domain-specific risk assessment for `{client_id}`.
        - **Memory**: Agent must write findings to `{fcc_daily_logs}{date}.md` and update `{fcc_client_profiles}{client_id}.md`.
        - **Requirement**: Must include citations to source regulatory documents from the `fcc-database-service`.

## Phase 2: Cross-Talk & Refinement

Once individual assessments are logged, agents are re-engaged to ensure awareness of cross-domain findings.

1.  **Shared Memory Review**:
    - Each agent reads the latest entries in `{fcc_daily_logs}{date}.md` related to `{client_id}`.
    - If a finding from another agent (e.g., Sanctions) impacts their own domain (e.g., KYC risk level), the agent must update their assessment in the shared memory.

## Phase 3: Synthesis & Reporting

1.  **Synthesize Findings**:
    - Collect all distilled findings from `{fcc_client_profiles}{client_id}.md` and the daily log.
    - Resolve any conflicts between agent opinions based on evidence weight and regulatory hierarchy.

2.  **Generate Compliance Report**:
    - Produce a structured HTML report as defined in `{skill-root}/assets/report-template.html`.
    - **Report Elements**:
        - Summary Risk Level (Green/Yellow/Red).
        - Executive Summary of the Consensus decision.
        - Agent-specific findings with citation links.
        - Audit trail of the cross-talk phase.

## Tools & Scripts

- `scripts/generate_report.py`: Aggregates memory data into the final HTML report.
- `fcc-database-service`: Used by individual agents for RAG retrieval.

## Conventions

- Shared Memory Root: `{project-root}/_bmad/memory/fcc/`
- All timestamps must follow ISO-8601.
- Agent tags in logs: `[AGENT_NAME] Finding...`
