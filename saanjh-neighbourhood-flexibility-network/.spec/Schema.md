# Data Models & Schemas (Schema.md)
## Project: Saanjh Neighbourhood Flexibility Network

### 1. Primary Entity State
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "SaanjhNeighbourhoodFlexibilityNetworkState",
  "type": "object",
  "required": ["sessionId", "timestamp", "status"],
  "properties": {
    "sessionId": { "type": "string" },
    "timestamp": { "type": "integer" },
    "status": { "type": "string", "enum": ["IDLE", "RUNNING", "VERIFIED", "FAILED"] },
    "metadata": { "type": "object" }
  }
}
```

### 2. Memory URI Mapping
- **Active State:** `viking://projects/saanjh-neighbourhood-flexibility-network/state`
- **Telemetry Snapshots:** `viking://projects/saanjh-neighbourhood-flexibility-network/telemetry`
- **Security Checkpoints:** `viking://projects/saanjh-neighbourhood-flexibility-network/security`
