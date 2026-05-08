# Ingest Documents Capability

To ingest new regulatory documents into the internal FCC database:

1. **Prepare Documents:** Place PDF or Word files in a local folder.
2. **Execute Ingestion:** Run the following command via `run_shell_command`:
   ```powershell
   python {skill-root}/scripts/service.py --ingest "[path_to_docs]" --jurisdiction "[EU/US/SG]" --domain "[KYC/AML/Sanctions]"
   ```
3. **Verification:** The script will output the number of chunks added.

Note: Metadata (jurisdiction, domain) is critical for agents to filter correctly.
