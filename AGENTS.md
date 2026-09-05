# AGENTS.md: Autonomous Agent Execution Directives for Project SYZYGY
> **MANDATORY INSTRUCTION FOR ALL AI CODING AGENTS (Claude Code, Cursor, Codex, Antigravity, OpenCode)**

Whenever a user instructs you to:
- *"Use this repo"*
- *"Build a project using syzygy"*
- *"Create an app / system"*
- *"Scaffold a project"*

**YOU MUST PERMANENTLY AND AUTOMATICALLY FOLLOW THIS EXACT PROTOCOL BEFORE GENERATING ANY APPLICATION CODE:**

---

## ⚡ STEP 1: Execute Pre-Project Scaffolding via `syzygy.py`

Run the SYZYGY CLI to generate the **8 Spec-Driven Development (SDD) files**:
```bash
python syzygy.py init "<Project-Name>" --domain <web|distributed|ai|hackathon> --brand <linear|apple|stripe>
```

This immediately creates `<project-name>/.spec/` containing:
1. **`PRD.md`**: Product Requirements Document (Goals, Personas, Functional Requirements).
2. **`TechSpec.md`**: Technical Specification (Best-in-class tech stack, runtime dependencies, APIs).
3. **`Architecture.md`**: System Architecture & Multi-Agent Mesh (Mermaid.js distributed topology).
4. **`AppFlow.md`**: User Journey, Agent Handoffs, and State Machine Transitions.
5. **`Design.md`**: OpenDesign Contract (Tokens, typography, 8px grid, motion physics).
6. **`Rules.md`**: ASD-STE100 Simplified Technical English & Anti-AI Slop directives.
7. **`Schema.md`**: Data Models, JSON-RPC schemas, and OpenViking `viking://` URIs.
8. **`Tracker.md`**: Milestone execution checklist and verification test matrix.

---

## 🏛️ STEP 2: Consult Domain Tech Stack Matrix

Never use generic, outdated, or default libraries. You MUST use the benchmarked champions defined in [`docs/DOMAIN_TECH_STACKS.md`](docs/DOMAIN_TECH_STACKS.md):

- **Web Frontend:** Next.js 16 + React 19 + Tailwind CSS v4 / Vanilla CSS + Motion (`motion`) + ThreeUI primitives.
- **UI Design System:** OpenDesign `DESIGN.md` contract + Boneyard auto-skeletons.
- **Multi-Agent Orchestration:** DeepSeek Harness (`dsh`) + Antonio Gulli's 66 Agentic Patterns.
- **Academic Research:** Firecrawl Research Index (43M+ scientific papers, zero hallucination).
- **Architecture Flowcharts:** Diagram Design + System Design 101.
- **Presentations & Slides:** PPT Master (native vector `.pptx` shapes, no flat images) + SIH Grand Finale 10-slide deck.
- **Agent Memory:** OpenViking (`viking://` URI namespace) + AgentMemory.
- **Pre-Flight Pentesting:** Strix Multi-Agent Pentesting.
- **Documentation Standards:** ASD-STE100 Technical English.

---

## 🔍 STEP 3: Automated Research & Verification

If the project requires complex algorithms, distributed consensus, or scientific data:
```bash
python syzygy.py research "<Topic>"
```
Extract verified formulas and citations before implementing logic.

---

## 🛡️ STEP 4: Pre-Flight Quality & Security Gate

Before declaring any project complete, you MUST execute:
```bash
# 1. Verify text has zero AI slop
python syzygy.py validate "<Documentation or Summary Text>"

# 2. Run Strix pre-flight security audit
python syzygy.py audit --target http://localhost:3000
```

---

## 📊 STEP 5: Generate Presentation Deck (Optional / Hackathon)

If a presentation or deck is requested:
```bash
python syzygy.py deck "<Project Name>" --out presentation.pptx
```
Generates 100% native vector editable `.pptx` slides adhering to the winning SIH Grand Finale standard.
