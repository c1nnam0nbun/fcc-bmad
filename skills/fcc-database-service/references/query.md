# Query Capability

To search for regulatory information in the FCC database:

1. **Parameters:**
   - `query`: The search string.
   - `jurisdiction` (Optional): Filter results by jurisdiction (e.g., "EU").
   - `domain` (Optional): Filter results by domain (e.g., "KYC").
   - `n_results` (Optional): Number of results to return (default: 5).

2. **Execute Query:**
   ```powershell
   python {skill-root}/scripts/service.py --query "[your_question]" --jurisdiction "[filter]" --domain "[filter]"
   ```

3. **Output:** The script returns the most relevant document chunks along with their source metadata.
