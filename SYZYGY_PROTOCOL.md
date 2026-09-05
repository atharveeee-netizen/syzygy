# SYZYGY Protocol Specification (v1.0.0)
## Autonomous Agent Alignment & Spec-Driven Development Standard

---

### 1. The Syzygy Principle
A *syzygy* represents linear gravitational alignment. In autonomous software engineering, **SYZYGY** enforces perfect alignment between:
1. **User Intent & Natural Language Goals**
2. **Deterministic Context (The 8 SDD Specification Files)**
3. **Open-Source Champion Tooling (Best-in-Class Matrix)**
4. **Automated Quality & Security Gates (ASD-STE100 + Strix)**

---

### 2. The 8 Spec-Driven Development (SDD) Documents

Every project constructed within this framework must maintain a `.spec/` directory with:

1. **`PRD.md` (Product Requirements Document):** Problem statement, target personas, quantified success metrics, and functional scope.
2. **`TechSpec.md` (Technical Specification):** Technology stack breakdown, runtime dependencies, APIs, and hardware tier bounds.
3. **`Architecture.md` (System Architecture):** Topology mesh, distributed component layout, and IPC communication protocols in Mermaid.js.
4. **`AppFlow.md` (Application Flow):** Step-by-step user journeys, state machine diagrams, and failure rollback policies.
5. **`Design.md` (OpenDesign Contract):** Design tokens, typography hierarchy (Outfit/Inter), 8px layout grid, and spring motion physics.
6. **`Rules.md` (Agent & Code Directives):** ASD-STE100 technical writing constraints, typing mandates, and zero AI slop enforcement.
7. **`Schema.md` (Data Models & Protocol Schemas):** JSON-RPC 2.0 tool definitions, database models, and OpenViking `viking://` URI mappings.
8. **`Tracker.md` (Implementation Milestones):** Atomic execution checklist, test suite passes, and deployment gates.

---

### 3. Agent Command Protocol

AI agents can execute the SYZYGY protocol using the `syzygy` CLI:
```bash
# Synthesize a new project from prompt using all agents as per need (PERMANENT DEFAULT)
python syzygy.py new "Autonomous AI Edge Drone Tracker on Jetson Nano with telemetry and secure auth"

# Initialize a new project with explicit domain & brand override
python syzygy.py init "Project Name" --domain <web|distributed|ai|hackathon|edge|robotics> --brand <linear|apple|stripe>


# Run academic research query
python syzygy.py research "Query"

# Generate SIH-grade native vector presentation deck
python syzygy.py deck "Title" --out deck.pptx

# Audit code/text against AI slop
python syzygy.py validate "Text"

# Execute pre-flight penetration testing
python syzygy.py audit --target http://localhost:3000
```
