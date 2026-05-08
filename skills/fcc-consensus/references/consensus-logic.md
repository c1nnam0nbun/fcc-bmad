# Consensus Workflow References

## Phase 1: Individual Analysis
Invoke targeted expert agents (default: all installed `fcc-agent-*`).
- **Input:** `task_description`, `jurisdiction`, `domain` (from command args).
- **Execution:** Iterate through agents, passing the task requirements and relevant regulatory domain.
- **Requirement:** Agents must output citations back to `fcc-database-service`.

## Phase 2: Cross-Talk & Refinement
- **Memory Root:** `{project-root}/_bmad/memory/fcc/`
- **Execution:** Agents review each other's findings in `{fcc_daily_logs}{date}.md`.
- **Goal:** Identify contradictions or gaps between different regulatory domains (e.g., Privacy vs. AML).

## Phase 3: Synthesis & Reporting
- **Output:** Generate a consolidated `REGULATORY_CONSENSUS_REPORT.md`.
- **Structure:**
    1. **Executive Summary**: Definitive corporate decision/recommendation.
    2. **Domain Findings**: Categorized analysis from each participating agent.
    3. **Conflict Resolution**: How competing regulatory requirements were reconciled.
    4. **Action Items**: Concrete steps for the company to remain compliant.
    5. **Citations**: Full list of referenced regulatory documents.
- **Location:** Saved to `{project-root}/_bmad/output/consensus/{timestamp}_report.md`.
