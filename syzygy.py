#!/usr/bin/env python3
"""
SYZYGY: Master Multi-Agent Autonomous Engineering CLI & Scaffolding Engine
Aligned with Antonio Gulli's 66 Agentic Design Patterns, OpenDesign, and 8-File Spec-Driven Development.
"""

import os
import sys
import json
import argparse
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] [SYZYGY] %(message)s')
logger = logging.getLogger("SYZYGY")

BASE_DIR = Path(__file__).resolve().parent

# Ensure core and modules can be imported
sys.path.insert(0, str(BASE_DIR))

try:
    from core.orchestrator import OrchestratorEngine
    from core.memory import OpenVikingClient
    from core.research import FirecrawlResearchIndex
    from core.presenter import PPTMasterDeckGenerator
    from core.diagrammer import ArchitectureDiagramGenerator
    from core.pentest import StrixPentestAgent
    from core.validator import STE100Validator
    from core.synthesizer import ProjectSynthesizer
except ImportError:
    pass

class SyzygyCLI:
    @staticmethod
    def init_project(prompt_or_name: str, domain: Optional[str] = None, brand: str = "linear", target_dir: str = "."):
        """
        Synthesizes a new project from prompt or name using all agents as per need,
        following the 8-File Spec-Driven Development (SDD) Architecture.
        """
        synthesizer = ProjectSynthesizer()
        res = synthesizer.synthesize(prompt=prompt_or_name, target_dir=target_dir, brand=brand, domain=domain)
        return res.get("project_dir", target_dir)


def main():
    parser = argparse.ArgumentParser(description="SYZYGY Master Multi-Agent Engineering CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # init command
    init_parser = subparsers.add_parser("init", help="Synthesize new project from prompt or name with all agents per need")
    init_parser.add_argument("prompt", help="Natural language prompt or project name")
    init_parser.add_argument("--domain", choices=["web", "distributed", "ai", "hackathon", "edge", "robotics", "security"], default=None, help="Project technical domain override")
    init_parser.add_argument("--brand", choices=["linear", "apple", "stripe", "supabase"], default="linear", help="Design system brand contract")
    init_parser.add_argument("--dir", default=".", help="Target root directory")

    # new command (natural language prompt synthesis)
    new_parser = subparsers.add_parser("new", help="Synthesize new project from natural language prompt with all agents per need")
    new_parser.add_argument("prompt", help="Natural language prompt or project description")
    new_parser.add_argument("--domain", choices=["web", "distributed", "ai", "hackathon", "edge", "robotics", "security"], default=None, help="Project technical domain override")
    new_parser.add_argument("--brand", choices=["linear", "apple", "stripe", "supabase"], default="linear", help="Design system brand contract")
    new_parser.add_argument("--dir", default=".", help="Target root directory")

    # project command (alias for new)
    project_parser = subparsers.add_parser("project", help="Synthesize new project from natural language prompt with all agents per need")
    project_parser.add_argument("prompt", help="Natural language prompt or project description")
    project_parser.add_argument("--domain", choices=["web", "distributed", "ai", "hackathon", "edge", "robotics", "security"], default=None, help="Project technical domain override")
    project_parser.add_argument("--brand", choices=["linear", "apple", "stripe", "supabase"], default="linear", help="Design system brand contract")
    project_parser.add_argument("--dir", default=".", help="Target root directory")

    # research command
    res_parser = subparsers.add_parser("research", help="Extract academic papers and equations via Firecrawl Index")
    res_parser.add_argument("topic", help="Research topic or scientific domain")
    res_parser.add_argument("--max", type=int, default=3, help="Maximum papers to extract")

    # deck command
    deck_parser = subparsers.add_parser("deck", help="Generate native vector PowerPoint presentation (.pptx)")
    deck_parser.add_argument("title", help="Deck presentation title")
    deck_parser.add_argument("--out", default="presentation.pptx", help="Output file path")

    # validate command
    val_parser = subparsers.add_parser("validate", help="Audit text against ASD-STE100 anti-slop rules")
    val_parser.add_argument("text", help="Text string to audit")

    # audit command
    sec_parser = subparsers.add_parser("audit", help="Run Strix autonomous security pentest")
    sec_parser.add_argument("--target", default="http://localhost:3000", help="Target URL or endpoint")

    # train command (AI/ML Foundation Model Engineering)
    train_parser = subparsers.add_parser("train", help="AI/ML training, LoRA/QLoRA scaffolding & hyperparameter validation")
    train_parser.add_argument("--mode", choices=["lora", "qlora", "scratch", "validate"], default="lora", help="Training architecture mode")
    train_parser.add_argument("--dir", default="./ml_pipeline", help="Target directory for training harness")
    train_parser.add_argument("--lr", type=float, default=2e-4, help="Learning rate")
    train_parser.add_argument("--rank", type=int, default=16, help="LoRA rank (r)")
    train_parser.add_argument("--alpha", type=int, default=32, help="LoRA alpha (scaling)")

    # recon command
    recon_parser = subparsers.add_parser("recon", help="Autonomous reconnaissance for pre-existing templates and PCBs")
    recon_parser.add_argument("query", help="What to search for (e.g., 'ESP32 motor controller PCB')")

    # architect command
    architect_parser = subparsers.add_parser("architect", help="Hardware-aware AI Architect to judge deployment strategies")
    architect_parser.add_argument("constraints", help="Deployment constraints (e.g., 'deploy on esp32')")

    # ideate command
    ideate_parser = subparsers.add_parser("ideate", help="Hackathon strategist for out-of-the-box ideas")
    ideate_parser.add_argument("theme", help="Hackathon theme or topic")

    # scrape command (Physical Browser-Use)
    scrape_parser = subparsers.add_parser("scrape", help="Launch physical Browser-Use AI Agent to scrape/navigate the web autonomously")
    scrape_parser.add_argument("task", help="The navigation or scraping task description")

    # orchestrate command (Physical DeepSeek Harness)
    orch_parser = subparsers.add_parser("orchestrate", help="Boot up the physical DeepSeek Harness web daemon")
    orch_parser.add_argument("--port", type=int, default=3080, help="Port to run the orchestrator UI on")

    # setup command (Git Submodules)
    setup_parser = subparsers.add_parser("setup", help="Dynamically download all 22 Agent & Engine Submodules via git submodule")

    # vendors command (live status table)
    vendors_parser = subparsers.add_parser("vendors", help="List all 22 Champion Matrix repos and their clone status")

    args = parser.parse_args()

    if args.command in ["init", "new", "project"]:
        prompt_val = getattr(args, "prompt", getattr(args, "project_name", "syzygy-app"))
        SyzygyCLI.init_project(prompt_val, domain=args.domain, brand=args.brand, target_dir=args.dir)
    elif args.command == "research":
        from core.research import FirecrawlResearchIndex
        extractor = FirecrawlResearchIndex()
        res = extractor.search_and_extract(args.topic, max_papers=args.max)
        print(json.dumps(res, indent=2))
    elif args.command == "deck":
        from core.presenter import PPTMasterDeckGenerator
        gen = PPTMasterDeckGenerator(args.title)
        gen.add_slide(f"{args.title}: Overview", "EXECUTIVE SUMMARY", [
            "Generated via SYZYGY Autonomous Presentation Engine",
            "100% Native vector shapes and editable typography (no flat bitmaps)",
            "Aligned with SIH Grand Finale Winning Deck standard"
        ], metric_badge="Turnkey Vector")
        gen.add_slide("System Architecture & Data Mesh", "ARCHITECTURE", [
            "DeepSeek Harness Lead Coordinator (Antonio Gulli Ch 7)",
            "OpenViking hierarchical memory (viking://)",
            "Strix autonomous containerized security auditor"
        ])
        msg = gen.render_pptx(args.out)
        print(msg)
    elif args.command == "validate":
        from core.validator import STE100Validator
        res = STE100Validator.audit_text(args.text)
        print(json.dumps(res, indent=2))
    elif args.command == "audit":
        from core.pentest import StrixPentestAgent
        auditor = StrixPentestAgent()
        report = auditor.run({"target": args.target})
        print(json.dumps(report, indent=2))
    elif args.command == "train":
        from core.aiml import AIMLEngineAgent
        engine = AIMLEngineAgent()
        report = engine.run({
            "action": "validate" if args.mode == "validate" else "scaffold",
            "project_dir": args.dir,
            "mode": args.mode,
            "params": {
                "learning_rate": args.lr,
                "lora_r": args.rank,
                "lora_alpha": args.alpha,
                "mode": args.mode
            }
        })
        print(json.dumps(report, indent=2))
    elif args.command == "recon":
        from core.recon import ReconEngineAgent
        agent = ReconEngineAgent()
        report = agent.execute_recon(args.query)
        print(json.dumps(report, indent=2))
    elif args.command == "architect":
        from core.architect import AIArchitectAgent
        agent = AIArchitectAgent()
        report = agent.judge_architecture(args.constraints)
        print(report)
    elif args.command == "ideate":
        from core.ideation import HackathonStrategistAgent
        agent = HackathonStrategistAgent()
        report = agent.execute_ideation(args.theme)
        print(json.dumps(report, indent=2))
    elif args.command == "scrape":
        from core.orchestrator import PhysicalAgentEngine
        PhysicalAgentEngine.launch_browser_use(args.task)
    elif args.command == "orchestrate":
        from core.orchestrator import PhysicalAgentEngine
        PhysicalAgentEngine.launch_deepseek(port=args.port)
    elif args.command == "setup":
        logger.info("Initializing and fetching all Champion Matrix Submodules from official GitHub repos...")
        ret = os.system("git submodule update --init --recursive")
        if ret == 0:
            logger.info("Setup complete. All official repositories cloned into vendor/.")
        else:
            logger.error("git submodule update failed. Check your internet connection and try again.")
    elif args.command == "vendors":
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
        from core.orchestrator import OrchestratorEngine
        engine = OrchestratorEngine()
        vendors = engine.list_vendors()
        print(f"\n{'Tool':<25} {'Cloned':>8}  Official GitHub Repo")
        print("-" * 85)
        for name, info in vendors.items():
            status = "[YES]" if info["cloned"] else "[ NO]"
            print(f"{name:<25} {status:>8}  {info['repo']}")
        not_cloned = [n for n, i in vendors.items() if not i["cloned"]]
        if not_cloned:
            print(f"\n[!] {len(not_cloned)} repos not yet cloned. Run: python syzygy.py setup")
        else:
            print("\n[OK] All vendor repositories are cloned and ready.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
