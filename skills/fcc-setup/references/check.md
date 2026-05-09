# Check Integrity Capability

To verify that the FCC module and its dependencies are correctly installed and configured:

1. **Verify Database:**
   Ensure `fcc-database-service` can connect to ChromaDB and load the embedding function.
   ```powershell
   python skills/fcc-database-service/scripts/service.py --status
   ```

2. **Verify Environment:**
   Confirm that the `_bmad` directory exists and has the correct permissions for logging and output.

3. **Verify Agents:**
   Check that all `fcc-agent-*` directories contain valid `SKILL.md` files and required assets.
