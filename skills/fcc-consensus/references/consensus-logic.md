# Consensus Workflow References

## Phase 1: Individual Analysis
Invoke targeted expert agents (default: all installed `fcc-agent-*`).
- **Input:** `client_id`, `jurisdiction` (from command args).
- **Execution:** Iterate through agents, passing the client profile and regulatory domain.
- **Requirement:** Agents must output citations.

## Phase 2: Cross-Talk & Refinement
- **Memory Root:** `{project-root}/_bmad/memory/fcc/`
- **Execution:** Read `{fcc_daily_logs}{date}.md`. If conflicts exist, flag for synthesis.

## Phase 3: Synthesis & Reporting
- **Script:** `python {skill-root}/scripts/generate_report.py --client {client_id}`
- **Report:** Generates HTML dashboard from `assets/report-template.html`.
