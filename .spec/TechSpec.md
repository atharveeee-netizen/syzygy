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
- `torch>=2.2.0`: PyTorch engine for modern transformer modeling and backpropagation.
- `transformers>=4.40.0`: Model weights, tokenizers, and architectures.
- `peft>=0.10.0` & `trl>=0.8.6`: Parameter-Efficient Fine-Tuning and Supervised Fine-Tuning / DPO / GRPO.
- `bitsandbytes>=0.43.0`: 4-bit / 8-bit NormalFloat (NF4) quantization and paged optimizers.
- `vllm>=0.4.0`: High-throughput PagedAttention agent serving and guided JSON decoding.

---

### 3. Compute Tiers & Hardware Requirements
1. **Ultra-Low Edge Tier (CPU Only):**
   - **Model:** Cactus Needle (14MB SLM, 28MB RAM).
   - **Workload:** Command parsing, local tool-calling, edge routing.
2. **Workstation Tier (Standard CPU / Integrated GPU):**
   - **Tools:** DeepSeek Harness (`dsh`), Firecrawl Research Index, PPT Master, OpenDesign.
   - **RAM:** 8 GB minimum.
3. **Consumer GPU Tuning Tier (Single-GPU QLoRA):**
   - **Tools:** Unsloth + Hugging Face PEFT/TRL (or Soup for layer-streaming).
   - **Hardware:** 16 GB System RAM + 6-8 GB NVIDIA VRAM (e.g. RTX 3060/4060).
   - **Capability:** Fine-tunes 8B models (Llama 3.1, Qwen 2.5) with 4-bit NF4 and sequence length 4096.
4. **Enterprise Multi-GPU & Foundation Pretraining Tier:**
   - **Tools:** Axolotl + DeepSpeed ZeRO-3 / PyTorch FSDP.
   - **Hardware:** Multi-GPU node (e.g. 4x or 8x A100/H100 80GB, NVLink).
   - **Capability:** Full parameter fine-tuning, large MoE pretraining, and distributed RLHF/GRPO.
5. **Enterprise Pentesting & AI Simulation Tier:**
   - **Tools:** Strix Multi-Agent Cluster + SimFoundry Physical AI Simulator.
   - **Hardware:** 32 GB RAM + 12 GB+ VRAM.
