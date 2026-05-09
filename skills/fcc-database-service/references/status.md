# Database Status & Maintenance

To check the health and contents of the FCC database:

1. **Check Status:**
   ```powershell
   python {skill-root}/scripts/service.py --status
   ```
   - Returns total chunk count.
   - Lists all unique source documents with their current jurisdiction and domain tags.

2. **Reset Database:**
   ```powershell
   python {skill-root}/scripts/service.py --reset
   ```
   - **Warning:** This permanently deletes the `fcc_regulatory_docs` collection. Use only when a full re-index is required.
