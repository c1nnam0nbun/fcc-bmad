# Query Database Capability

This capability is used primarily by expert agents to retrieve evidence.

**Internal Logic:**
Agents use the `FCCDatabase` class in `scripts/service.py` or call it via shell to perform filtered searches.

**Filtering Rules:**
- `jurisdiction`: Only return documents matching the target country/region.
- `domain`: Only return documents matching the agent's expertise (e.g., KYC).

**Example Shell Query:**
```powershell
# (This is a conceptual example for testing)
python {skill-root}/scripts/service.py --query "What are the KYC requirements for crypto in Singapore?" --jurisdiction "Singapore" --domain "KYC"
```
