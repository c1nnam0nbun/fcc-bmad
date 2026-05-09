# Ingest Documents Capability

To ingest new regulatory documents into the internal FCC database:

1. **Prepare Documents:** Place PDF, DOCX, MD, or TXT files in a local folder.
2. **Execute Ingestion:**
   ```powershell
   python {skill-root}/scripts/service.py --ingest "[path_to_file_or_folder]" --jurisdiction "[tag]" --domain "[tag]" --language "[lang]"
   ```
3. **Parameters:**
   - `--ingest`: Path to a specific file or a directory.
   - `--jurisdiction`: (Default: "Global") Comma-separated tags.
   - `--domain`: (Default: "General") Comma-separated tags.
   - `--language`: (Default: "English").

4. **Verification:** The script outputs the number of chunks added. Chunks are ~1000 characters with 200 character overlap.
