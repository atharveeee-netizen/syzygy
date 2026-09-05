# AGENTS.md: Autonomous Agent Execution Directives for Project SYZYGY
> **MANDATORY INSTRUCTION FOR ALL AI CODING AGENTS (Antigravity, Claude Code, Cursor, Codex, OpenCode)**

## 🚨 PERMANENT GLOBAL DEFAULT: ALL AGENTS ACTIVATED AS PER NEED

Whenever a user provides a prompt to:
- *"Build a project..."*
- *"Create an app / system / tool..."*
- *"Scaffold a project..."*
- *"Make a project for [X]..."*

**YOU MUST PERMANENTLY AND AUTOMATICALLY EXECUTE THE MULTI-AGENT SYNTHESIS ENGINE BEFORE GENERATING ANY APPLICATION CODE:**

```bash
python syzygy.py new "<Full User Prompt>"
```

This dynamically evaluates the prompt and automatically activates all required specialized agents as per need:
1. **`ReconEngineAgent`**: Real GitHub API search for reference implementations, CAD files, and packages.
2. **`FirecrawlResearchIndex`**: Live arXiv queries for scientific papers, equations, and citations.
3. **`HackathonStrategistAgent`**: Ideation, killer features, market moats, and winning hackathon angles.
4. **`AIArchitectAgent`**: Hardware sizing (Jetson, ESP32, RPi, Mac, Cloud), memory limits, and quantization profile.
5. **`ArchitectureDiagramGenerator`**: Syntax-verified distributed Mermaid architecture topology.
6. **`GitHubActionsAgent`**: Language-specific CI/CD workflow (`.github/workflows/ci.yml`).
7. **`ScaffoldAuthAgent`**: Identity, session management, and authentication middleware.
8. **`ScaffoldTelemetryAgent`**: OpenTelemetry distributed tracing and metrics instrumentation.
9. **`ScaffoldCryptoAgent`**: Cryptographic vault, SecretBox encryption, and key generation.
10. **`AIMLEngineAgent`**: LoRA/QLoRA training harness, hyperparameters, and dataset scaffolding.
11. **`StrixPentestAgent`**: Pre-flight security audit script and vulnerability checklist.
12. **`OpenVikingClient`**: Persistent SQLite memory checkpoint (`viking://projects/<slug>`).
13. **`STE100Validator`**: Anti-slop audit against ASD-STE100 technical English standards.

This automatically generates the **8 Spec-Driven Development (SDD) files** in `<project-slug>/.spec/`:
1. **`PRD.md`**: Problem statement, research citations, reference repos, and metrics.
2. **`TechSpec.md`**: Hardware constraints, framework verdict, and technology stack.
3. **`Architecture.md`**: Mermaid component mesh and data flow contracts.
4. **`AppFlow.md`**: Execution sequences and state machine transitions.
5. **`Design.md`**: OpenDesign tokens, typography (Outfit/Inter), and spring physics.
6. **`Rules.md`**: ASD-STE100 guidelines and anti-slop code directives.
7. **`Schema.md`**: Data models, JSON-RPC schemas, and `viking://` memory URIs.
8. **`Tracker.md`**: Atomic milestone execution checklist.

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
