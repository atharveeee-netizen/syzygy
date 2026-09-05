# Application Flow & Execution Pipelines (AppFlow.md)
## Project SYZYGY: Agent Self-Bootstrapping Workflow & State Transitions

---

### 1. End-to-End Self-Bootstrapping Sequence

```
[Agent Receives User Prompt]
       │
       ▼
[Phase 1: Self-Bootstrapping via AGENTS.md]
  Agent reads AGENTS.md / SYZYGY_PROTOCOL.md
  Agent runs `python syzygy.py init "<Project>" --domain <type>`
  Project directory and .spec/ 8-file suite generated
       │
       ▼
[Phase 2: Verbatim Academic & Technical Research]
  Agent invokes `python syzygy.py research "<Topic>"`
  Firecrawl Research Index returns verified formulas and citations
  Equations stored in viking://knowledge/domain
       │
       ▼
[Phase 3: Visual Topology Generation]
  Agent generates Mermaid.js distributed architecture diagram
  Embeds verified visual flows into Architecture.md and pitch deck
       │
       ▼
[Phase 4: Design Contract & UI Implementation]
  Agent reads design-systems/DESIGN.md
  Applies dark obsidian canvas (#090D16), Outfit/Inter typography, and Motion physics
  Implements components with ThreeUI 3D primitives and Boneyard auto-skeletons
       │
       ▼
[Phase 5: Presentation Synthesis]
  Agent runs `python syzygy.py deck "<Project>" --out deck.pptx`
  PPT Master renders native editable vector PowerPoint deck
       │
       ▼
[Phase 6: Quality & Security Verification]
  Agent runs `python syzygy.py validate "<Text>"` (ASD-STE100 anti-slop pass)
  Agent runs `python syzygy.py audit` (Strix pre-flight security scan)
       │
       ▼
[Phase 7: Final Turnkey Delivery]
  Tracker.md updated to 100% COMPLETE
  Verified production codebase delivered to user
```
