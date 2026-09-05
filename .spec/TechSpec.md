# Technical Specification (TechSpec)
## Project SYZYGY: Runtime Toolchain, Dependency Matrix & Compute Tiers

---

### 1. Runtime Environment & Toolchain

| Runtime / Tool | Minimum Version | Recommended Version | Primary Role |
| :--- | :--- | :--- | :--- |
| **Python** | 3.10.x | 3.11.x or 3.12.x | Multi-agent CLI, vector slide synthesis, research crawler |
| **Node.js** | 18.x LTS | 20.x LTS | Web harnesses, UI engines, and Next.js / React runtimes |
| **Package Managers** | `pip` / `uv` & `npm` / `pnpm` | `uv` + `pnpm` | High-speed, lockfile-deterministic package installs |
| **Git** | 2.40+ | Latest | Version control and subproject provenance |
| **Containerization** | Docker 24.x | Latest with Compose v2 | Isolated execution for Strix security agents |

---

### 2. Core Python Dependencies (`requirements.txt`)
- `python-pptx>=0.6.23`: Programmatic native vector PowerPoint generation.
- `httpx>=0.27.0`: High-concurrency async HTTP client for Firecrawl Research Index queries.
- `pydantic>=2.7.0`: Strict schema typing and validation.
- `pytest>=8.0.0`: Automated test execution.

---

### 3. Compute Tiers & Hardware Requirements
1. **Ultra-Low Edge Tier (CPU Only):**
   - **Model:** Cactus Needle (14MB SLM, 28MB RAM).
   - **Workload:** Command parsing, local tool-calling, edge routing.
2. **Workstation Tier (Standard CPU / Integrated GPU):**
   - **Tools:** DeepSeek Harness (`dsh`), Firecrawl Research Index, PPT Master, OpenDesign.
   - **RAM:** 8 GB minimum.
3. **Consumer GPU Tuning Tier:**
   - **Tool:** Soup (Layer-streaming LoRA fine-tuning).
   - **Hardware:** 16 GB System RAM + 4 GB NVIDIA VRAM (e.g. RTX 3050/4050).
4. **Enterprise Pentesting & AI Simulation Tier:**
   - **Tools:** Strix Multi-Agent Cluster + SimFoundry Physical AI Simulator.
   - **Hardware:** 32 GB RAM + 12 GB+ VRAM.
