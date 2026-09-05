# Schemas & Protocol Definitions (Schema.md)
## Project SYZYGY: Tool Invocations, State Shapes & Memory Models

---

### 1. Model Context Protocol (MCP) JSON-RPC 2.0 Invocations
```json
{
  "jsonrpc": "2.0",
  "id": "syzygy-tool-001",
  "method": "syzygy_execute_tool",
  "params": {
    "toolName": "research_extract",
    "arguments": {
      "topic": "Distributed Consensus",
      "maxPapers": 3
    }
  }
}
```

---

### 2. OpenViking URI Memory Model
```
viking://[domain]/[namespace]/[resource_id]
```
- Session: `viking://session/active/{sessionId}`
- Agent Memory: `viking://memory/agent/{agentId}`
- Knowledge: `viking://knowledge/domain/{slug}`
- Presentation: `viking://presentation/decks/{deckId}`
