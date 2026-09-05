"""
SYZYGY Lead Coordinator & Dynamic Agent Router
Delegates all execution to OFFICIAL vendor submodule entry points.
Zero hardcoded scripts. Zero simulated wrappers.
References: Antonio Gulli, Agentic Design Patterns, Chapters 2, 3, 4, 7 & Appendix G.
"""

import sys
import os
import json
import logging
import importlib
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger("SYZYGY.Orchestrator")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

VENDOR_DIR = Path(__file__).resolve().parent.parent / "vendor"

# ============================================================
# OFFICIAL VENDOR ENTRY POINTS
# Every command here delegates directly to the official repo.
# Run `python syzygy.py setup` first to clone all submodules.
# ============================================================
VENDOR_CATALOG = {
    # ── Orchestrators ──────────────────────────────────────────────────────
    "langgraph": {
        "repo":  "https://github.com/langchain-ai/langgraph",
        "path":  VENDOR_DIR / "langgraph",
        "docs":  "https://github.com/langchain-ai/langgraph#readme",
        "install": "pip install langgraph",
        "run":   None,
    },
    "crewai": {
        "repo":  "https://github.com/crewAIInc/crewAI",
        "path":  VENDOR_DIR / "crewAI",
        "docs":  "https://github.com/crewAIInc/crewAI#readme",
        "install": "pip install crewai",
        "run":   "crewai",
    },
    # ── Agents & Memory ────────────────────────────────────────────────────
    "browser-use": {
        "repo":  "https://github.com/browser-use/browser-use",
        "path":  VENDOR_DIR / "browser-use",
        "docs":  "https://docs.browser-use.com",
        "install": "pip install browser-use",
        "run":   "python -m browser_use",
    },
    "mem0ai": {
        "repo":  "https://github.com/mem0ai/mem0",
        "path":  VENDOR_DIR / "mem0",
        "docs":  "https://docs.mem0.ai",
        "install": "pip install mem0ai",
        "run":   None,
    },
    "letta": {
        "repo":  "https://github.com/letta-ai/letta",
        "path":  VENDOR_DIR / "letta",
        "docs":  "https://docs.letta.com",
        "install": "pip install letta",
        "run":   "letta server",
    },
    # ── AI Model Training & Inference ──────────────────────────────────────
    "deepseek-harness": {
        "repo":  "https://github.com/deepseek-ai/deepseek-harness",
        "path":  VENDOR_DIR / "deepseek-harness",
        "docs":  "https://github.com/deepseek-ai/deepseek-harness#readme",
        "install": "npm install",
        "run":   "npm start",
    },
    "lightning-hydra-template": {
        "repo":  "https://github.com/ashleve/lightning-hydra-template",
        "path":  VENDOR_DIR / "lightning-hydra-template",
        "docs":  "https://github.com/ashleve/lightning-hydra-template#readme",
        "install": "pip install -r requirements.txt",
        "run":   "python src/train.py",
    },
    "unsloth": {
        "repo":  "https://github.com/unslothai/unsloth",
        "path":  VENDOR_DIR / "unsloth",
        "docs":  "https://github.com/unslothai/unsloth#readme",
        "install": "pip install unsloth",
        "run":   "python -m unsloth",
    },
    "vllm": {
        "repo":  "https://github.com/vllm-project/vllm",
        "path":  VENDOR_DIR / "vllm",
        "docs":  "https://docs.vllm.ai",
        "install": "pip install vllm",
        "run":   "python -m vllm.entrypoints.openai.api_server",
    },
    "litellm": {
        "repo":  "https://github.com/BerriAI/litellm",
        "path":  VENDOR_DIR / "litellm",
        "docs":  "https://docs.litellm.ai",
        "install": "pip install litellm[proxy]",
        "run":   "litellm",
    },
    # ── Research & Scraping ────────────────────────────────────────────────
    "firecrawl": {
        "repo":  "https://github.com/mendableai/firecrawl",
        "path":  VENDOR_DIR / "firecrawl",
        "docs":  "https://docs.firecrawl.dev",
        "install": "pip install firecrawl-py",
        "run":   "firecrawl",
    },
    "scrapegraph-ai": {
        "repo":  "https://github.com/ScrapeGraphAI/Scrapegraph-ai",
        "path":  VENDOR_DIR / "scrapegraph-ai",
        "docs":  "https://scrapegraph-ai.readthedocs.io",
        "install": "pip install scrapegraphai",
        "run":   "python -m scrapegraphai",
    },
    "paper-search-mcp": {
        "repo":  "https://github.com/openags/paper-search-mcp",
        "path":  VENDOR_DIR / "paper-search-mcp",
        "docs":  "https://github.com/openags/paper-search-mcp#readme",
        "install": "pip install -e .",
        "run":   None,
    },
    # ── Security & Quality ─────────────────────────────────────────────────
    "strix": {
        "repo":  "https://github.com/usestrix/strix",
        "path":  VENDOR_DIR / "strix",
        "docs":  "https://github.com/usestrix/strix#readme",
        "install": "pip install strix",
        "run":   "strix scan",
    },
    "anti-ai-slop-writing": {
        "repo":  "https://github.com/jalaalrd/anti-ai-slop-writing",
        "path":  VENDOR_DIR / "anti-ai-slop-writing",
        "docs":  "https://github.com/jalaalrd/anti-ai-slop-writing#readme",
        "install": None,
        "run":   None,
    },
    # ── Infrastructure & DevOps ────────────────────────────────────────────
    "act": {
        "repo":  "https://github.com/nektos/act",
        "path":  VENDOR_DIR / "act",
        "docs":  "https://nektosact.com",
        "install": "brew install act", # Depends on OS, winget for windows
        "run":   "act",
    },
    "diagrams": {
        "repo":  "https://github.com/mingrammer/diagrams",
        "path":  VENDOR_DIR / "diagrams",
        "docs":  "https://diagrams.mingrammer.com",
        "install": "pip install diagrams",
        "run":   None,
    },
    # ── Web, Mobile & General ──────────────────────────────────────────────
    "supabase-cli": {
        "repo":  "https://github.com/supabase/cli",
        "path":  VENDOR_DIR / "supabase-cli",
        "docs":  "https://supabase.com/docs/reference/cli",
        "install": "npm install supabase --save-dev",
        "run":   "supabase start",
    },
    "ppt-master": {
        "repo":  "https://github.com/hugohe3/ppt-master",
        "path":  VENDOR_DIR / "ppt-master",
        "docs":  "https://github.com/hugohe3/ppt-master#readme",
        "install": "pip install ppt-master",
        "run":   "python -m ppt_master",
    },
    
    # ── Edge / On-Device Inference ─────────────────────────────────────────
    "llama.cpp": {
        "repo":  "https://github.com/ggml-org/llama.cpp",
        "path":  VENDOR_DIR / "llama.cpp",
        "docs":  "https://github.com/ggml-org/llama.cpp#readme",
        "install": "cmake -B build && cmake --build build --config Release",
        "run":   "./build/bin/llama-cli",
    },
    "whichllm": {
        "repo":  "https://github.com/Andyyyy64/whichllm",
        "path":  VENDOR_DIR / "whichllm",
        "docs":  "https://github.com/Andyyyy64/whichllm#readme",
        "install": "pip install whichllm",
        "run":   "python -m whichllm",
    },

    # ── Hardware / CAD / Robotics ──────────────────────────────────────────
    "awesome-cad": {
        "repo":  "https://github.com/mlightcad/awesome-cad",
        "path":  VENDOR_DIR / "awesome-cad",
        "docs":  "https://github.com/mlightcad/awesome-cad#readme",
        "install": None,
        "run":   None,
    },
    "mujoco": {
        "repo":  "https://github.com/google-deepmind/mujoco",
        "path":  VENDOR_DIR / "mujoco",
        "docs":  "https://mujoco.readthedocs.io",
        "install": "pip install mujoco",
        "run":   "python -m mujoco.viewer",
    },
}


class AgentRouter:
    """Dynamic Agent Routing Engine (Antonio Gulli Pattern #2 & #7).
    Routes task types to official vendor submodule entry points.
    """

    ROUTES = {
        "orchestrate":  "langgraph",
        "scrape":       "browser-use",
        "scrape_social":"scrapegraph-ai",
        "train":        "lightning-hydra-template",
        "serve":        "vllm",
        "edge":         "llama.cpp",
        "route":        "litellm",
        "research":     "paper-search-mcp",
        "memory":       "mem0ai",
        "security":     "strix",
        "pentest":      "strix",
        "diagram":      "diagrams",
        "ci":           "act",
        "db":           "supabase-cli",
        "deck":         "ppt-master",
        "cad":          "awesome-cad",
        "robotics":     "mujoco",
    }

    @classmethod
    def resolve_vendor(cls, task_type: str) -> Optional[Dict]:
        vendor_key = cls.ROUTES.get(task_type.lower())
        if not vendor_key:
            logger.warning(f"No vendor route for task type: '{task_type}'")
            return None
        return VENDOR_CATALOG.get(vendor_key)


class OrchestratorEngine:
    """SYZYGY Lead Coordinator. Dispatches tasks to official vendor tool entry points."""

    def __init__(self, session_id: str = "syzygy_default"):
        self.session_id = session_id
        self.state_uri = f"viking://session/active/{session_id}"
        logger.info(f"SYZYGY Orchestrator ready. Session: {self.state_uri}")

    def dispatch(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type", "general")
        logger.info(f"Dispatching task [{task.get('id', 'N/A')}] → type: {task_type}")

        vendor = AgentRouter.resolve_vendor(task_type)
        if not vendor:
            return {
                "status": "NO_ROUTE",
                "task_type": task_type,
                "available_routes": list(AgentRouter.ROUTES.keys()),
            }

        vendor_path = vendor["path"]
        if not vendor_path.exists():
            return {
                "status": "VENDOR_NOT_CLONED",
                "repo": vendor["repo"],
                "fix": "Run `python syzygy.py setup` to clone all vendor submodules.",
            }

        return {
            "status": "READY",
            "task_type": task_type,
            "vendor_repo": vendor["repo"],
            "vendor_path": str(vendor_path),
            "docs": vendor["docs"],
            "run_cmd": vendor["run"],
            "install_cmd": vendor["install"],
            "note": "Execute run_cmd from the vendor_path to launch the official tool.",
        }

    def list_vendors(self) -> Dict[str, Any]:
        """List all vendors and their clone status."""
        result = {}
        for name, info in VENDOR_CATALOG.items():
            result[name] = {
                "repo": info["repo"],
                "cloned": info["path"].exists(),
                "docs": info["docs"],
            }
        return result


class PhysicalAgentEngine:
    """
    Executes the OFFICIAL entry points of outsourced vendor repos.
    ZERO hardcoded scripts are written. We invoke what the official repo provides.
    """

    @staticmethod
    def _check_vendor(name: str) -> Optional[Path]:
        vendor = VENDOR_CATALOG.get(name)
        if not vendor:
            logger.error(f"Unknown vendor: {name}")
            return None
        path = vendor["path"]
        if not path.exists():
            logger.error(
                f"Vendor '{name}' not cloned. Run `python syzygy.py setup` first.\n"
                f"Official repo: {vendor['repo']}"
            )
            return None
        return path

    @staticmethod
    def launch_deepseek(port: int = 3080):
        """Launch DeepSeek Harness using its OFFICIAL npm start entry point."""
        path = PhysicalAgentEngine._check_vendor("deepseek-harness")
        if not path:
            return
        info = VENDOR_CATALOG["deepseek-harness"]
        logger.info(f"Launching official DeepSeek Harness → {info['docs']}")
        logger.info(f"Source: {info['repo']}")
        # Run official entry point: npm install (first time) then npm start
        subprocess.run(f'npm install --silent ; npm start -- --port {port}', shell=True, cwd=str(path))

    @staticmethod
    def launch_browser_use(task_description: str):
        """
        Launch Browser-Use using its OFFICIAL Python package API.
        Delegates directly to the cloned vendor/browser-use package.
        See official docs: https://docs.browser-use.com
        """
        path = PhysicalAgentEngine._check_vendor("browser-use")
        if not path:
            return
        info = VENDOR_CATALOG["browser-use"]
        logger.info(f"Launching official Browser-Use → {info['docs']}")
        logger.info(f"Task: {task_description}")

        # Install from the cloned submodule, then run via module
        subprocess.run(f'pip install -e "{path}" --quiet', shell=True)
        code = f"import asyncio; from browser_use import Agent; from langchain_openai import ChatOpenAI; asyncio.run(Agent(task='{task_description}', llm=ChatOpenAI(model='gpt-4o')).run())"
        subprocess.run(["python", "-c", code])

    @staticmethod
    def launch_letta():
        """Launch Letta Agent Memory server using its official CLI."""
        path = PhysicalAgentEngine._check_vendor("letta")
        if not path:
            return
        info = VENDOR_CATALOG["letta"]
        logger.info(f"Launching official Letta server → {info['docs']}")
        subprocess.run(f'pip install -e "{path}" --quiet ; letta server', shell=True)

    @staticmethod
    def launch_strix(target: str):
        """Run Strix security scan using its official entry point."""
        path = PhysicalAgentEngine._check_vendor("strix")
        if not path:
            return
        info = VENDOR_CATALOG["strix"]
        logger.info(f"Launching official Strix scan on {target} → {info['docs']}")
        subprocess.run(f'pip install -e "{path}" --quiet ; strix scan --target {target}', shell=True)


if __name__ == "__main__":
    engine = OrchestratorEngine()
    print(json.dumps(engine.list_vendors(), indent=2))
