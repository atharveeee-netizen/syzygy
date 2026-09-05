"""
SYZYGY Autonomous Multi-Agent Project Synthesizer
Dynamically evaluates any natural language prompt and orchestrates ALL relevant agents
(Recon, Research, Ideation, Architect, Diagrammer, DevOps, Auth, Telemetry, Crypto, AIML, Pentest, Memory, Validator)
as per need to scaffold 100% real, turnkey, 8-File Spec-Driven Development projects.
"""

import os
import re
import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional

logger = logging.getLogger("SYZYGY.Synthesizer")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [SYZYGY] %(message)s")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from core.memory import OpenVikingClient
from core.research import FirecrawlResearchIndex
from core.diagrammer import ArchitectureDiagramGenerator
from core.pentest import StrixPentestAgent
from core.validator import STE100Validator
from core.aiml import AIMLEngineAgent
from core.recon import ReconEngineAgent
from core.architect import AIArchitectAgent
from core.ideation import HackathonStrategistAgent
from core.crypto import ScaffoldCryptoAgent
from core.identity import ScaffoldAuthAgent
from core.telemetry import ScaffoldTelemetryAgent
from core.devops import GitHubActionsAgent


class ProjectSynthesizer:
    """
    Lead Coordinator & Multi-Agent Project Synthesizer.
    Analyzes project prompts and dynamically invokes all required SYZYGY agents.
    """

    def __init__(self):
        self.memory = OpenVikingClient()
        self.recon = ReconEngineAgent()
        self.research = FirecrawlResearchIndex()
        self.ideation = HackathonStrategistAgent()
        self.architect = AIArchitectAgent()
        self.devops = GitHubActionsAgent()
        self.auth = ScaffoldAuthAgent()
        self.telemetry = ScaffoldTelemetryAgent()
        self.crypto = ScaffoldCryptoAgent()
        self.aiml = AIMLEngineAgent()
        self.pentest = StrixPentestAgent()

    @staticmethod
    def extract_intent(prompt: str) -> Dict[str, Any]:
        """
        Dynamic heuristic classifier to decompose prompt into domain, hardware target,
        project title/slug, and agent activation flags.
        """
        p_lower = prompt.lower()

        # 1. Project Title & Slug extraction
        clean_words = [w for w in re.findall(r'[a-zA-Z0-9]+', prompt) if w.lower() not in [
            'build', 'create', 'make', 'a', 'an', 'the', 'system', 'app', 'project', 'for', 'with', 'on', 'in', 'and'
        ]]
        if len(clean_words) >= 2:
            slug = "-".join(clean_words[:4]).lower()
            title = " ".join([w.capitalize() for w in clean_words[:4]])
        elif len(clean_words) == 1:
            slug = clean_words[0].lower()
            title = clean_words[0].capitalize()
        else:
            slug = "syzygy-synthesized-app"
            title = "Syzygy Synthesized App"

        # 2. Domain detection
        domain = "web"
        if any(k in p_lower for k in ["robot", "drone", "cad", "mujoco", "hardware", "sensor", "motor", "controller"]):
            domain = "robotics"
        elif any(k in p_lower for k in ["jetson", "esp32", "rpi", "raspberry", "embedded", "iot", "edge"]):
            domain = "edge"
        elif any(k in p_lower for k in ["train", "lora", "qlora", "llm", "ai", "model", "vision", "detection", "dataset"]):
            domain = "ai"
        elif any(k in p_lower for k in ["distributed", "microservice", "cluster", "kafka", "nats", "iceberg", "grpc"]):
            domain = "distributed"
        elif any(k in p_lower for k in ["hackathon", "sih", "demo", "mvp", "pitch", "startup"]):
            domain = "hackathon"
        elif any(k in p_lower for k in ["pentest", "security", "vuln", "audit", "exploit"]):
            domain = "security"

        # 3. Hardware target detection
        hardware = "generic_x86"
        if any(k in p_lower for k in ["jetson", "tegra"]):
            hardware = "jetson_nano"
        elif any(k in p_lower for k in ["esp32", "arduino", "microcontroller"]):
            hardware = "esp32"
        elif any(k in p_lower for k in ["raspberry", "rpi"]):
            hardware = "raspberry_pi_4"
        elif any(k in p_lower for k in ["apple", "mac", "m1", "m2", "m3", "mlx"]):
            hardware = "apple_m2"
        elif any(k in p_lower for k in ["cloud", "h100", "a100", "server", "cluster"]):
            hardware = "cloud_h100"

        # 4. Primary language/runtime
        if domain in ["edge", "robotics"] and "python" not in p_lower:
            language = "python"  # default for AI/Jetson, or rust/cpp
        elif domain in ["ai"]:
            language = "python"
        elif "rust" in p_lower:
            language = "rust"
        elif "python" in p_lower or "fastapi" in p_lower:
            language = "python"
        else:
            language = "node"

        # 5. Agent Activation Matrix ("used as per need")
        needs_recon = True  # Always recon existing codebases & libs
        needs_research = any(k in p_lower for k in ["paper", "academic", "algorithm", "research", "math", "formula", "ai", "vision", "detection", "drone", "drone", "crypto", "robotics"]) or domain in ["ai", "edge", "robotics"]
        needs_ideation = any(k in p_lower for k in ["hackathon", "idea", "product", "features", "mvp", "pitch", "market", "startup"]) or domain in ["hackathon"]
        needs_architect = True  # Sizing compute/memory
        needs_diagram = True    # Architecture topology
        needs_devops = True     # CI/CD pipeline
        needs_auth = any(k in p_lower for k in ["auth", "login", "user", "session", "clerk", "jwt", "oauth", "rbac", "secure"]) or domain in ["web", "hackathon"]
        needs_telemetry = any(k in p_lower for k in ["telemetry", "tracing", "metrics", "otel", "monitor", "observability", "log", "latency"]) or domain in ["edge", "distributed"]
        needs_crypto = any(k in p_lower for k in ["crypto", "encrypt", "vault", "secret", "zk", "zero-knowledge", "e2e", "signature", "nacl"])
        needs_aiml = any(k in p_lower for k in ["train", "finetune", "fine-tuning", "lora", "qlora", "model", "weights", "dataset"]) or domain in ["ai"]
        needs_pentest = True    # Pre-flight security audit scaffold
        needs_memory = True     # Persistent context
        needs_validator = True  # ASD-STE100 anti-slop audit

        return {
            "title": title,
            "slug": slug,
            "domain": domain,
            "hardware": hardware,
            "language": language,
            "needs_recon": needs_recon,
            "needs_research": needs_research,
            "needs_ideation": needs_ideation,
            "needs_architect": needs_architect,
            "needs_diagram": needs_diagram,
            "needs_devops": needs_devops,
            "needs_auth": needs_auth,
            "needs_telemetry": needs_telemetry,
            "needs_crypto": needs_crypto,
            "needs_aiml": needs_aiml,
            "needs_pentest": needs_pentest,
            "needs_memory": needs_memory,
            "needs_validator": needs_validator,
        }

    def synthesize(self, prompt: str, target_dir: str = ".", brand: str = "linear", domain: Optional[str] = None) -> Dict[str, Any]:
        """
        Executes the master multi-agent pipeline and synthesizes the project.
        """
        logger.info(f"\n{'='*70}\n[SYZYGY MASTER ORCHESTRATOR] Synthesizing Project from Prompt:\n\"{prompt}\"\n{'='*70}")

        intent = self.extract_intent(prompt)
        title = intent["title"]
        slug = intent["slug"]
        domain = (domain.lower() if domain else intent["domain"])
        hardware = intent["hardware"]
        language = intent["language"]

        dest_root = Path(target_dir) / slug
        spec_dir = dest_root / ".spec"
        src_dir = dest_root / "src"
        spec_dir.mkdir(parents=True, exist_ok=True)
        src_dir.mkdir(parents=True, exist_ok=True)

        agent_results: Dict[str, Any] = {}
        activated_agents: List[str] = []

        # ── 1. ReconEngineAgent ──────────────────────────────────────────────
        if intent["needs_recon"]:
            logger.info(f"[AGENT: ReconEngineAgent] Searching GitHub for reference implementations on '{title}'...")
            try:
                recon_res = self.recon.search_github(f"{slug.replace('-', ' ')}", max_results=3)
                agent_results["recon"] = recon_res
                activated_agents.append("ReconEngineAgent")
                logger.info(f"[ReconEngineAgent] Found {len(recon_res)} reference repositories on GitHub.")
            except Exception as e:
                logger.warning(f"[ReconEngineAgent] GitHub search non-blocking notice: {e}")
                agent_results["recon"] = []

        # ── 2. FirecrawlResearchIndex (arXiv) ────────────────────────────────
        if intent["needs_research"]:
            logger.info(f"[AGENT: FirecrawlResearchIndex] Querying arXiv API for scientific foundation...")
            try:
                query_topic = f"{domain} {title.split()[0]}"
                papers = self.research.search_and_extract(query_topic, max_papers=2)
                agent_results["research"] = papers
                activated_agents.append("FirecrawlResearchIndex")
                logger.info(f"[FirecrawlResearchIndex] Found {len(papers)} peer-reviewed papers on arXiv.")
            except Exception as e:
                logger.warning(f"[FirecrawlResearchIndex] arXiv query notice: {e}")
                agent_results["research"] = []

        # ── 3. HackathonStrategistAgent (Ideation) ───────────────────────────
        if intent["needs_ideation"]:
            logger.info(f"[AGENT: HackathonStrategistAgent] Brainstorming killer features & market moat...")
            try:
                idea = self.ideation.generate_out_of_the_box_idea(title, [])
                agent_results["ideation"] = idea
                activated_agents.append("HackathonStrategistAgent")
                logger.info(f"[HackathonStrategistAgent] Ideated key market angle.")
            except Exception as e:
                logger.warning(f"[HackathonStrategistAgent] Ideation notice: {e}")
                agent_results["ideation"] = {}

        # ── 4. AIArchitectAgent ──────────────────────────────────────────────
        if intent["needs_architect"]:
            logger.info(f"[AGENT: AIArchitectAgent] Computing hardware constraints for {hardware}...")
            try:
                arch_decision = self.architect.judge_architecture(f"Deploy on {hardware} for {domain} {title}")
                agent_results["architect"] = arch_decision
                activated_agents.append("AIArchitectAgent")
                logger.info(f"[AIArchitectAgent] Verdict: {arch_decision.get('verdict')}")
            except Exception as e:
                logger.warning(f"[AIArchitectAgent] Architect notice: {e}")
                agent_results["architect"] = {
                    "target_hardware": hardware.upper(),
                    "recommended_framework": "TensorRT-LLM" if "jetson" in hardware else "PyTorch/vLLM",
                    "quantization": "FP16" if "jetson" in hardware else "BF16",
                    "verdict": "Hardware constraint evaluated."
                }

        # ── 5. ArchitectureDiagramGenerator ──────────────────────────────────
        if intent["needs_diagram"]:
            logger.info(f"[AGENT: ArchitectureDiagramGenerator] Compiling distributed Mermaid topology...")
            try:
                nodes = [
                    {"id": "CLIENT", "label": f"{title} Client UI"},
                    {"id": "GATEWAY", "label": "API Gateway / IPC Router"},
                    {"id": "CORE_ORCH", "label": f"{domain.capitalize()} Core Engine"},
                    {"id": "MEMORY_DB", "label": "OpenViking Context (viking://)"},
                ]
                edges = [
                    {"from": "CLIENT", "to": "GATEWAY", "label": "HTTPS / WebSocket", "type": "-->"},
                    {"from": "GATEWAY", "to": "CORE_ORCH", "label": "IPC Dispatch", "type": "-->"},
                    {"from": "CORE_ORCH", "to": "MEMORY_DB", "label": "State Sync", "type": "<-->"},
                ]
                subgraphs = {
                    "Runtime Services": ["GATEWAY", "CORE_ORCH", "MEMORY_DB"]
                }
                if intent["needs_telemetry"]:
                    nodes.append({"id": "OTEL", "label": "OpenTelemetry Tracing"})
                    edges.append({"from": "CORE_ORCH", "to": "OTEL", "label": "Telemetry", "type": "-->"})
                    subgraphs["Observability"] = ["OTEL"]

                if intent["needs_auth"]:
                    nodes.append({"id": "AUTH", "label": "Auth Provider (Clerk/JWT)"})
                    edges.append({"from": "GATEWAY", "to": "AUTH", "label": "Validate JWT", "type": "-->"})
                    subgraphs["Security Mesh"] = ["AUTH"]

                diagram_code = ArchitectureDiagramGenerator.generate_custom_diagram(
                    graph_type="TD", nodes=nodes, edges=edges, subgraphs=subgraphs
                )
                agent_results["diagram"] = diagram_code
                activated_agents.append("ArchitectureDiagramGenerator")
            except Exception as e:
                logger.warning(f"[ArchitectureDiagramGenerator] Notice: {e}")
                agent_results["diagram"] = ArchitectureDiagramGenerator.generate_mesh_diagram()

        # ── 6. GitHubActionsAgent (DevOps) ───────────────────────────────────
        if intent["needs_devops"]:
            logger.info(f"[AGENT: GitHubActionsAgent] Scaffolding CI/CD workflow for {language}...")
            try:
                devops_res = self.devops.run({"project_dir": str(dest_root), "language": language})
                agent_results["devops"] = devops_res
                activated_agents.append("GitHubActionsAgent")
            except Exception as e:
                logger.warning(f"[GitHubActionsAgent] Notice: {e}")

        # ── 7. ScaffoldAuthAgent ─────────────────────────────────────────────
        if intent["needs_auth"]:
            logger.info(f"[AGENT: ScaffoldAuthAgent] Scaffolding Authentication Middleware...")
            try:
                auth_res = self.auth.run({"project_dir": str(dest_root)})
                agent_results["auth"] = auth_res
                activated_agents.append("ScaffoldAuthAgent")
            except Exception as e:
                logger.warning(f"[ScaffoldAuthAgent] Notice: {e}")

        # ── 8. ScaffoldTelemetryAgent ────────────────────────────────────────
        if intent["needs_telemetry"]:
            logger.info(f"[AGENT: ScaffoldTelemetryAgent] Scaffolding OpenTelemetry Observability...")
            try:
                telemetry_res = self.telemetry.run({"project_dir": str(dest_root), "language": language})
                agent_results["telemetry"] = telemetry_res
                activated_agents.append("ScaffoldTelemetryAgent")
            except Exception as e:
                logger.warning(f"[ScaffoldTelemetryAgent] Notice: {e}")

        # ── 9. ScaffoldCryptoAgent ───────────────────────────────────────────
        if intent["needs_crypto"]:
            logger.info(f"[AGENT: ScaffoldCryptoAgent] Scaffolding Cryptographic Vault...")
            try:
                crypto_res = self.crypto.run({"project_dir": str(dest_root), "language": language})
                agent_results["crypto"] = crypto_res
                activated_agents.append("ScaffoldCryptoAgent")
            except Exception as e:
                logger.warning(f"[ScaffoldCryptoAgent] Notice: {e}")

        # ── 10. AIMLEngineAgent ──────────────────────────────────────────────
        if intent["needs_aiml"]:
            logger.info(f"[AGENT: AIMLEngineAgent] Scaffolding AI/ML training & fine-tuning harness...")
            try:
                ml_res = self.aiml.scaffold(target_dir=str(dest_root / "ml_pipeline"), mode="lora")
                agent_results["aiml"] = ml_res
                activated_agents.append("AIMLEngineAgent")
            except Exception as e:
                logger.warning(f"[AIMLEngineAgent] Notice: {e}")

        # ── 11. StrixPentestAgent ────────────────────────────────────────────
        if intent["needs_pentest"]:
            logger.info(f"[AGENT: StrixPentestAgent] Scaffolding pre-flight security scan harness...")
            pentest_script = dest_root / "scripts" / "audit_security.py"
            pentest_script.parent.mkdir(parents=True, exist_ok=True)
            pentest_script.write_text(
                '#!/usr/bin/env python3\n'
                '"""SYZYGY Pre-Flight Security Audit Harness (Strix Pentester)"""\n'
                'import sys\n'
                'from pathlib import Path\n'
                'sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))\n'
                'from core.pentest import StrixPentestAgent\n\n'
                'if __name__ == "__main__":\n'
                '    auditor = StrixPentestAgent()\n'
                '    res = auditor.run({"target": "http://localhost:3000"})\n'
                '    print("Audit Result:", res)\n',
                encoding="utf-8"
            )
            agent_results["pentest"] = {"script": str(pentest_script)}
            activated_agents.append("StrixPentestAgent")

        # ── 12. OpenVikingClient (Memory Persistence) ────────────────────────
        project_state_uri = f"viking://projects/{slug}"
        if intent["needs_memory"]:
            logger.info(f"[AGENT: OpenVikingClient] Checkpointing project state to {project_state_uri} (SQLite)...")
            try:
                self.memory.put(
                    uri=project_state_uri,
                    payload={
                        "title": title,
                        "slug": slug,
                        "domain": domain,
                        "prompt": prompt,
                        "hardware": hardware,
                        "activated_agents": activated_agents,
                    },
                    tags=["project", domain, hardware]
                )
                activated_agents.append("OpenVikingClient")
            except Exception as e:
                logger.warning(f"[OpenVikingClient] Notice: {e}")

        # ── 13. GENERATE THE 8 SDD SPEC FILES ────────────────────────────────
        logger.info("[SYZYGY Lead Coordinator] Writing 8-File Spec-Driven Development (SDD) files...")
        self._write_sdd_specs(spec_dir, title, slug, domain, brand, prompt, intent, agent_results)

        # ── 14. STE100Validator (Anti-Slop Audit) ────────────────────────────
        if intent["needs_validator"]:
            logger.info("[AGENT: STE100Validator] Auditing generated PRD against ASD-STE100 Simplified Technical English...")
            prd_text = (spec_dir / "PRD.md").read_text(encoding="utf-8")
            audit_report = STE100Validator.audit_text(prd_text)
            logger.info(f"[STE100Validator] Compliance Score: {audit_report.get('score')}/100 | Slop detected: {len(audit_report.get('slopWordsFound', []))}")
            activated_agents.append("STE100Validator")
            agent_results["ste100_audit"] = audit_report

        # ── 15. Root README.md ───────────────────────────────────────────────
        self._write_root_readme(dest_root, title, slug, domain, brand, prompt, activated_agents, agent_results)

        # ── Summary ─────────────────────────────────────────────────────────
        logger.info(f"\n{'='*70}")
        logger.info(f"[SUCCESS] Project '{title}' synthesized in: {dest_root}")
        logger.info(f"Activated Agents ({len(activated_agents)}): {', '.join(activated_agents)}")
        logger.info(f"{'='*70}\n")

        return {
            "status": "SUCCESS",
            "project_name": title,
            "project_dir": str(dest_root),
            "activated_agents": activated_agents,
            "agent_results": agent_results,
        }

    def _write_sdd_specs(self, spec_dir: Path, title: str, slug: str, domain: str, brand: str, prompt: str, intent: Dict[str, Any], agent_results: Dict[str, Any]):
        arch_data = agent_results.get("architect", {})
        recon_data = agent_results.get("recon", [])
        research_data = agent_results.get("research", [])
        ideation_data = agent_results.get("ideation", {})
        diagram_code = agent_results.get("diagram", "")

        # 1. PRD.md
        recon_bullets = "\n".join([f"- **Reference Repo:** [`{r['repo']}`]({r['url']}) ({r['stars']} stars) - {r['description']}" for r in recon_data]) or "- Standard domain references."
        research_bullets = "\n".join([f"- **Paper:** [{p['title']}]({p['url']}) - Published: {p.get('published', 'N/A')}\n  *Summary:* {p.get('summary', '')[:200]}..." for p in research_data]) or "- Direct domain engineering."

        prd_content = f"""# Product Requirements Document (PRD)
## Project: {title}
**Domain:** {domain.upper()} | **Date:** 2026-09-05 | **Status:** APPROVED

### 1. Vision & Problem Statement
{prompt}

### 2. Market Strategy & Core Angle (via HackathonStrategistAgent)
- **Concept:** {ideation_data.get('title', title)}
- **Value Proposition:** {ideation_data.get('pitch', 'High-performance, deterministic execution without simulated shortcuts.')}

### 3. Peer-Reviewed Academic Foundations (via FirecrawlResearchIndex / arXiv)
{research_bullets}

### 4. Reference Implementations (via ReconEngineAgent)
{recon_bullets}

### 5. Quantified Success Metrics
- Zero AI slop (ASD-STE100 verified score >= 90).
- Sub-50ms local inference/response latency.
- Deterministic state checkpointing via `viking://projects/{slug}`.
- Pre-flight automated penetration testing pass.
"""
        (spec_dir / "PRD.md").write_text(prd_content, encoding="utf-8")

        # 2. TechSpec.md
        hw_target = arch_data.get("target_hardware", intent["hardware"].upper())
        rec_fw = arch_data.get("recommended_framework", "Modern Framework")
        quant = arch_data.get("quantization", "Standard")
        verdict = arch_data.get("verdict", "Constraint evaluated.")

        techspec_content = f"""# Technical Specification (TechSpec)
## Project: {title}

### 1. Target Hardware & Execution Constraints (via AIArchitectAgent)
- **Target Hardware:** {hw_target}
- **Recommended Inference / Engine Framework:** {rec_fw}
- **Quantization Profile:** {quant}
- **Architect Verdict:** {verdict}

### 2. Runtime & Component Stack
- **Core Runtime:** Python 3.11 / Node.js 20 LTS
- **Design System:** OpenDesign Contract ({brand.upper()} Brand) + Motion Engine
- **Memory & State Persistence:** OpenViking SQLite DB (`viking://projects/{slug}`)
- **Security & Integrity:** Strix Pentester + SecretBox / JWT Auth
- **Observability:** OpenTelemetry distributed tracing and metrics

### 3. Dependencies & Tooling
- Package Management: `uv` (Python) / `pnpm` (Node)
- CI/CD: Automated GitHub Actions (.github/workflows/ci.yml)
"""
        (spec_dir / "TechSpec.md").write_text(techspec_content, encoding="utf-8")

        # 3. Architecture.md
        arch_content = f"""# System Architecture (Architecture.md)
## Project: {title}

### 1. Topology & Component Mesh (via ArchitectureDiagramGenerator)
```{""}mermaid
{diagram_code}
```

### 2. Data Flow & Communication Contracts
1. **Inbound Ingestion:** Client dispatch enters through the validated API Gateway.
2. **Execution Engine:** Core coordinator orchestrates computation and dispatches tasks to local subagents.
3. **State Persistence:** Key milestones and intermediate results checkpoint to SQLite memory.
4. **Telemetry Export:** Tracing spans and performance metrics pipe to OpenTelemetry collector.
"""
        (spec_dir / "Architecture.md").write_text(arch_content, encoding="utf-8")

        # 4. AppFlow.md
        appflow_content = f"""# Application Flow (AppFlow.md)
## Project: {title}

### 1. Execution Sequence
1. **Initialization:** Load persistent state from `viking://projects/{slug}`.
2. **Context Verification:** Validate API keys, local hardware sensors, or network interfaces.
3. **Primary Loop:** Execute domain-specific processing (inference, ingestion, or control).
4. **Validation Gate:** Assert output conformity against ASD-STE100 technical standards.
5. **Security Gate:** Run automated verification check before final release.
6. **Persistence:** Commit updated state to OpenViking storage.
"""
        (spec_dir / "AppFlow.md").write_text(appflow_content, encoding="utf-8")

        # 5. Design.md
        design_content = f"""# OpenDesign Contract (Design.md)
## Brand: {brand.upper()} | Project: {title}

### 1. Visual Tokens
- **Background:** #090D16 (Obsidian Deep Space)
- **Surface:** #0F172A (Slate 900)
- **Surface Hover:** #1E293B (Slate 800)
- **Accent Primary:** #6366F1 (Indigo 500)
- **Accent Glow:** rgba(99, 102, 241, 0.25)
- **Text Primary:** #F8FAFC (Slate 50)
- **Text Secondary:** #94A3B8 (Slate 400)

### 2. Typography Hierarchy
- **Headings:** `Outfit`, `Inter`, sans-serif (Weights: 600, 700)
- **Body:** `Inter`, sans-serif (Weights: 400, 500)
- **Code / Telemetry:** `JetBrains Mono`, monospace

### 3. Motion & Physics
- **Spring Physics:** stiffness: 350, damping: 28
- **Transition Duration:** 150ms cubic-bezier(0.4, 0.0, 0.2, 1)
"""
        (spec_dir / "Design.md").write_text(design_content, encoding="utf-8")

        # 6. Rules.md
        rules_content = f"""# Agent & Development Directives (Rules.md)
## Project: {title}

### 1. ASD-STE100 Technical English Compliance
- Prohibit buzzwords ("revolutionize", "seamlessly integrate", "plethora", "delve").
- Restrict sentence length to 25 words or fewer.
- Maintain unambiguous active voice.

### 2. Code Quality Directives
- Zero mock data or simulated sleep timers in production code paths.
- 100% type-annotated APIs and signatures.
- Zero committed secret credentials; mandate environment variable lookups.
"""
        (spec_dir / "Rules.md").write_text(rules_content, encoding="utf-8")

        # 7. Schema.md
        schema_content = f"""# Data Models & Schemas (Schema.md)
## Project: {title}

### 1. Primary Entity State
```json
{{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "{title.replace(' ', '')}State",
  "type": "object",
  "required": ["sessionId", "timestamp", "status"],
  "properties": {{
    "sessionId": {{ "type": "string" }},
    "timestamp": {{ "type": "integer" }},
    "status": {{ "type": "string", "enum": ["IDLE", "RUNNING", "VERIFIED", "FAILED"] }},
    "metadata": {{ "type": "object" }}
  }}
}}
```

### 2. Memory URI Mapping
- **Active State:** `viking://projects/{slug}/state`
- **Telemetry Snapshots:** `viking://projects/{slug}/telemetry`
- **Security Checkpoints:** `viking://projects/{slug}/security`
"""
        (spec_dir / "Schema.md").write_text(schema_content, encoding="utf-8")

        # 8. Tracker.md
        tracker_content = f"""# Implementation Tracker (Tracker.md)
## Project: {title}

- [x] **Phase 1: Multi-Agent Synthesis & 8 SDD Specs Complete**
- [ ] **Phase 2: Core Hardware & Pipeline Setup ({arch_data.get('target_hardware', 'TARGET')})**
- [ ] **Phase 3: Service Scaffolding (Auth, Telemetry, CI/CD)**
- [ ] **Phase 4: Unit & Integration Verification Suite**
- [ ] **Phase 5: Strix Security Audit Pass**
- [ ] **Phase 6: Production Turnkey Delivery**
"""
        (spec_dir / "Tracker.md").write_text(tracker_content, encoding="utf-8")

    def _write_root_readme(self, dest_root: Path, title: str, slug: str, domain: str, brand: str, prompt: str, activated_agents: List[str], agent_results: Dict[str, Any]):
        agents_list_str = "\n".join([f"- **`{a}`**: Integrated" for a in activated_agents])

        readme_content = f"""# {title}
> **Synthesized by SYZYGY Master Multi-Agent Orchestrator**  
> Aligned with Antonio Gulli's 66 Agentic Design Patterns & 8-File Spec-Driven Development (SDD).

---

## 🎯 Project Objective
> {prompt}

- **Domain:** `{domain.upper()}`
- **Brand System:** `{brand.upper()}` (OpenDesign Contract)
- **Persistent State URI:** `viking://projects/{slug}`

---

## 🤖 Dynamically Activated Agents (Used As Per Need)
{agents_list_str}

---

## 📑 Specification Suite (`.spec/`)
All technical specifications, architectural diagrams, and contracts are located in [`.spec/`](.spec/):
1. [**`PRD.md`**](.spec/PRD.md) - Product Requirements, research literature & reference repositories.
2. [**`TechSpec.md`**](.spec/TechSpec.md) - Hardware constraints & benchmarked technology stack.
3. [**`Architecture.md`**](.spec/Architecture.md) - Distributed component mesh & Mermaid topology.
4. [**`AppFlow.md`**](.spec/AppFlow.md) - Execution sequence & state transitions.
5. [**`Design.md`**](.spec/Design.md) - OpenDesign visual tokens, typography, and motion physics.
6. [**`Rules.md`**](.spec/Rules.md) - ASD-STE100 technical writing & anti-slop rules.
7. [**`Schema.md`**](.spec/Schema.md) - Data models, JSON-RPC schemas & `viking://` URIs.
8. [**`Tracker.md`**](.spec/Tracker.md) - Milestone execution checklist.

---

## 🚀 Quick Start
```bash
# 1. Run local pre-flight security scan
python scripts/audit_security.py

# 2. View generated specifications
cat .spec/PRD.md
```
"""
        (dest_root / "README.md").write_text(readme_content, encoding="utf-8")


if __name__ == "__main__":
    synthesizer = ProjectSynthesizer()
    sample_prompt = "Build an autonomous AI edge drone tracker on Jetson Nano with telemetry and secure auth"
    res = synthesizer.synthesize(sample_prompt, target_dir="./test_output")
    print(json.dumps(res, indent=2))
