# Global Rule: Master Multi-Agent Autonomous Engineering Directives (SYZYGY)

## 🚨 MANDATORY PERMANENT DEFAULT: ALL AGENTS ACTIVATED AS PER NEED

Whenever the user gives a prompt to build, create, scaffold, or generate a project:
1. **Zero Trigger Words Required**: Never wait for manual trigger phrases or explicit commands.
2. **Execute Multi-Agent Synthesis First**:
   Run:
   ```bash
   python syzygy.py new "<Full User Prompt>"
   ```
3. **Dynamic Agent Routing (As Per Need)**:
   - **ReconEngineAgent**: Searches GitHub for live reference implementations, PCB schematics, and libraries.
   - **FirecrawlResearchIndex**: Queries the official arXiv API for peer-reviewed papers and mathematical formulations.
   - **HackathonStrategistAgent**: Brainstorms killer features, value proposition, and user personas.
   - **AIArchitectAgent**: Analyzes hardware limits (Jetson, ESP32, RPi, Mac, Cloud), memory thresholds, and quantization.
   - **ArchitectureDiagramGenerator**: Generates syntax-verified distributed Mermaid topology.
   - **GitHubActionsAgent**: Generates `.github/workflows/ci.yml` pipeline.
   - **ScaffoldAuthAgent**: Generates Clerk / JWT authentication scaffolding.
   - **ScaffoldTelemetryAgent**: Generates OpenTelemetry tracing and metrics.
   - **ScaffoldCryptoAgent**: Generates SecretBox cryptographic vault boilerplate.
   - **AIMLEngineAgent**: Scaffolds LoRA/QLoRA training harness.
   - **StrixPentestAgent**: Scaffolds automated pre-flight security scan harness.
   - **OpenVikingClient**: Checkpoints session state to persistent SQLite database (`viking://projects/<slug>`).
   - **STE100Validator**: Audits text and specifications against ASD-STE100 Simplified Technical English.
4. **8-File Spec-Driven Development (SDD) Standard**:
   Ensure all 8 files in `<project-slug>/.spec/` (`PRD.md`, `TechSpec.md`, `Architecture.md`, `AppFlow.md`, `Design.md`, `Rules.md`, `Schema.md`, `Tracker.md`) are populated with the real synthesized agent data.
5. **Zero AI Slop**: No simulated fake data, placeholder mocks, or marketing buzzwords.
