# Metadata Update Capability

To modify jurisdiction or domain tags for documents already in the database without re-ingesting them:

1. **Parameters:**
   - `update`: The exact source filename (e.g., "regulation.pdf").
   - `action`: Either `add` or `remove`.
   - `jurisdiction` (Optional): Tag(s) to add or remove.
   - `domain` (Optional): Tag(s) to add or remove.

2. **Execute Update:**
   - **Add tags:**
     ```powershell
     python {skill-root}/scripts/service.py --update "[source_name]" --domain "[new_tag]" --action add
     ```
   - **Remove tags:**
     ```powershell
     python {skill-root}/scripts/service.py --update "[source_name]" --jurisdiction "[old_tag]" --action remove
     ```

3. **Note:** Multi-value tags are supported (comma-separated).
