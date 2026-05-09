# Initialize Module Capability

To initialize the entire Fintech Crypto Compliance (FCC) suite:

1. **Automatic Initialization:**
   Run the setup script which discovers all internal agents and prepares the shared backbone.
   ```
   python {skill-root}/scripts/setup.py
   ```

2. **What it does:**
   - Installs required Python dependencies (`chromadb`, `sentence-transformers`, etc.).
   - Initializes the local Vector Database.
   - Downloads/loads the default embedding models.
   - Prepares directory structures for memory and reports.
   - Verifies all expert agents are correctly configured.
