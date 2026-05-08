# Backbone Configuration

## Purpose
Provide the technical configuration and metadata tags required for a new FCC agent to interface correctly with the shared RAG backbone.

## Workflow

1. **Intake:** User specifies the technical requirements or the target domain of a new agent.
2. **Configuration:**
    - Define the `jurisdiction` tag(s).
    - Define the `domain` tag(s).
    - Specify the `memory_root` (always `{project-root}/_bmad/memory/fcc/`).
    - Provide any additional environment variables needed (e.g., `FCC_VDB_URL`).
3. **Outcome:** A JSON/YAML snippet for the agent's configuration.

## Standard FCC Metadata Tags
- `jurisdiction`: [e.g., EU, US, SG, Global]
- `domain`: [e.g., KYC, AML, Sanctions, MiCA]
- `doc_type`: [e.g., Regulation, Procedure, Guidance]

## Example Config Snippet
```yaml
agent_config:
  shared_rag:
    vdb_url: "${FCC_VDB_URL}"
    default_filters:
      jurisdiction: "EU"
      domain: "Sanctions"
  memory:
    root: "{project-root}/_bmad/memory/fcc/"
    pattern: "single_shared_curated"
```
