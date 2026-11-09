# System Architecture (Architecture.md)
## Project: Saanjh Neighbourhood Flexibility Network

### 1. Topology & Component Mesh (via ArchitectureDiagramGenerator)
```mermaid
graph TD
    subgraph Runtime_Services ["Runtime Services"]
        GATEWAY["API Gateway / IPC Router"]
        CORE_ORCH["Web Core Engine"]
        MEMORY_DB["OpenViking Context (viking://)"]
    end
    subgraph Security_Mesh ["Security Mesh"]
        AUTH["Auth Provider (Clerk/JWT)"]
    end
    CLIENT["Saanjh Neighbourhood Flexibility Network Client UI"]
    CLIENT -->|"HTTPS / WebSocket"| GATEWAY
    GATEWAY -->|"IPC Dispatch"| CORE_ORCH
    CORE_ORCH <-->|"State Sync"| MEMORY_DB
    GATEWAY -->|"Validate JWT"| AUTH
```

### 2. Data Flow & Communication Contracts
1. **Inbound Ingestion:** Client dispatch enters through the validated API Gateway.
2. **Execution Engine:** Core coordinator orchestrates computation and dispatches tasks to local subagents.
3. **State Persistence:** Key milestones and intermediate results checkpoint to SQLite memory.
4. **Telemetry Export:** Tracing spans and performance metrics pipe to OpenTelemetry collector.
