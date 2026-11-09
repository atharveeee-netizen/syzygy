# Technical Specification (TechSpec)
## Project: Saanjh Neighbourhood Flexibility Network

### 1. Target Hardware & Execution Constraints (via AIArchitectAgent)
- **Target Hardware:** GENERIC_X86
- **Recommended Inference / Engine Framework:** Ollama / llama.cpp
- **Quantization Profile:** Q4_K_M
- **Architect Verdict:** CAPABLE: Hardware can support larger, unquantized or lightly quantized models.

### 2. Runtime & Component Stack
- **Core Runtime:** Python 3.11 / Node.js 20 LTS
- **Design System:** OpenDesign Contract (LINEAR Brand) + Motion Engine
- **Memory & State Persistence:** OpenViking SQLite DB (`viking://projects/saanjh-neighbourhood-flexibility-network`)
- **Security & Integrity:** Strix Pentester + SecretBox / JWT Auth
- **Observability:** OpenTelemetry distributed tracing and metrics

### 3. Dependencies & Tooling
- Package Management: `uv` (Python) / `pnpm` (Node)
- CI/CD: Automated GitHub Actions (.github/workflows/ci.yml)
