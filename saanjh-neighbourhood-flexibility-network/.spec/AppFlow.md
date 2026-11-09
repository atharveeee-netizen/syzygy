# Application Flow (AppFlow.md)
## Project: Saanjh Neighbourhood Flexibility Network

### 1. Execution Sequence
1. **Initialization:** Load persistent state from `viking://projects/saanjh-neighbourhood-flexibility-network`.
2. **Context Verification:** Validate API keys, local hardware sensors, or network interfaces.
3. **Primary Loop:** Execute domain-specific processing (inference, ingestion, or control).
4. **Validation Gate:** Assert output conformity against ASD-STE100 technical standards.
5. **Security Gate:** Run automated verification check before final release.
6. **Persistence:** Commit updated state to OpenViking storage.
