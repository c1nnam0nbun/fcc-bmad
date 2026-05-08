# Agent Build Workflow

## Purpose
Orchestrate the end-to-end process of identifying an expertise gap and building a new specialized FCC agent.

## Workflow

1.  **Analysis:** Use `Agent Requirement Analysis` (Load `./references/requirement-analysis.md`) to identify the specific expertise gap and jurisdiction.
2.  **Drafting:** Use `Specialized Brief Generator` (Load `./references/brief-generator.md`) to create a comprehensive brief for the new agent.
3.  **Review:** Present the generated brief to the user for confirmation.
4.  **Handoff:** Once confirmed, invoke the `bmad-bmb-setup` skill and then `bmad-agent-builder` skill.

IMPORTANT: You MUST invoke `bmad-agent-builder` skill once the plan is confirmed. It is important to setup freshly created agent properly.

## Handoff Directive

When handing off to `bmad-agent-builder`, use the following command structure:

"I have designed a new FCC expert agent. Use the brief below to build it. Save the new agent in `{project-root}/skills/` and ensure it follows all 'Non-negotiable' instructions provided in the brief.

**Post-Build Instruction:** After the agent is created, check the new agent's `scripts/` directory. If a `setup.py` file exists, execute it immediately to complete the agent's initialization within the FCC suite.

[PASTE GENERATED BRIEF HERE]"
