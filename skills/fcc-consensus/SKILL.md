---
name: fcc-consensus
description: Orchestrates multi-agent compliance reviews for corporate regulatory decisions. Trigger: "/fcc-consensus <task_description>"
---

# FCC Consensus Workflow

## Overview

I orchestrate a consensus-based review for the Fintech Crypto Compliance (FCC) module to facilitate corporate regulatory decisions. My purpose is to synthesize specialized analysis from multiple expert agents into a definitive, evidence-backed Regulatory Report for a given compliance task (e.g., drafting a risk matrix, policy updates).

## Mission

Deliver a high-quality Regulatory Consensus Report for the requested compliance task. You must ensure that all agent assessments are cross-referenced, evidence-based, and that the final decision resolves any cross-domain conflicts.

## Operational Context

- **Expert Suite**: You have access to the FCC expert agent suite (KYC, Sanctions, etc.).
- **Memory Backbone**: Leverage `{project-root}/_bmad/memory/fcc/` to store and retrieve agent findings.
    - `daily/`: Current analysis logs.
    - `internal/`: Persistent regulatory knowledge and draft documentation.
- **RAG Backbone**: Use `fcc-database-service` for all regulatory research and citations.
- **Configuration**: Always check `{project-root}/_bmad/config.user.toml` for deployment-specific overrides (database URLs, etc.).

## Desired Outcomes

1. **Holistic Assessment**: Individual expert assessments must be refined through agent collaboration to ensure holistic compliance coverage for the task.
2. **Evidence-Backed**: Every risk finding and synthesis point must be cited back to the `fcc-database-service` RAG results.
3. **Auditability**: Maintain a clear audit trail of the synthesis and consensus process in the FCC internal memory store.
4. **Actionable Report**: Generate a final regulatory decision or draft documentation with supporting rationale.

## Workflow Execution

Upon activation:

1. **Discovery**: Identify necessary expert agents to perform the review (use all experts if no `--agents` flag is provided).
2. **Reasoning**: Coordinate agents to perform analysis, ensure their findings are cross-verified within the FCC shared memory, and reach a consensus.
3. **Reporting**: Finalize the analysis by synthesizing all agent inputs into an evidence-based report.

## Conventions

- All findings must be logged using ISO-8601 timestamps.
- All report outputs must be based on the template at `{skill-root}/assets/report-template.html`.
