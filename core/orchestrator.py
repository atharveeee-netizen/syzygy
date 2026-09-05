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
    "browser-use": {
        "repo":  "https://github.com/browser-use/browser-use",
        "path":  VENDOR_DIR / "browser-use",
        "docs":  "https://docs.browser-use.com",
        "install": "pip install browser-use",
        "run":   "python -m browser_use",
    },
    "deepseek-harness": {
        "repo":  "https://github.com/deepseek-ai/deepseek-harness",
        "path":  VENDOR_DIR / "deepseek-harness",
        "docs":  "https://github.com/deepseek-ai/deepseek-harness#readme",
        "install": "npm install",
        "run":   "npm start",
    },
    "unsloth": {
        "repo":  "https://github.com/unslothai/unsloth",
        "path":  VENDOR_DIR / "unsloth",
        "docs":  "https://github.com/unslothai/unsloth#readme",
        "install": "pip install unsloth",
        "run":   "python -m unsloth",
    },
    "axolotl": {
        "repo":  "https://github.com/axolotl-ai-cloud/axolotl",
        "path":  VENDOR_DIR / "axolotl",
        "docs":  "https://axolotl-ai-cloud.github.io/axolotl/",
        "install": "pip install axolotl",
        "run":   "accelerate launch -m axolotl.cli.train",
    },
    "vllm": {
        "repo":  "https://github.com/vllm-project/vllm",
        "path":  VENDOR_DIR / "vllm",
        "docs":  "https://docs.vllm.ai",
        "install": "pip install vllm",
        "run":   "python -m vllm.entrypoints.openai.api_server",
    },
    "firecrawl": {
        "repo":  "https://github.com/mendableai/firecrawl",
        "path":  VENDOR_DIR / "firecrawl",
        "docs":  "https://docs.firecrawl.dev",
        "install": "pip install firecrawl-py",
        "run":   "firecrawl",
    },
    "letta": {
        "repo":  "https://github.com/letta-ai/letta",
        "path":  VENDOR_DIR / "letta",
        "docs":  "https://docs.letta.com",
        "install": "pip install letta",
        "run":   "letta server",
    },
    "strix": {
        "repo":  "https://github.com/usestrix/strix",
        "path":  VENDOR_DIR / "strix",
        "docs":  "https://github.com/usestrix/strix#readme",
        "install": "pip install strix",
        "run":   "strix scan",
    },
    "motion": {
        "repo":  "https://github.com/motiondivision/motion",
        "path":  VENDOR_DIR / "motion",
        "docs":  "https://motion.dev/docs",
        "install": "npm install motion",
        "run":   None,  # Library, not a CLI tool
    },
    "nnsight": {
        "repo":  "https://github.com/ndif-team/nnsight",
        "path":  VENDOR_DIR / "nnsight",
        "docs":  "https://nnsight.net/documentation",
        "install": "pip install nnsight",
        "run":   "python -m nnsight",
    },
    "supabase-cli": {
        "repo":  "https://github.com/supabase/cli",
        "path":  VENDOR_DIR / "supabase-cli",
        "docs":  "https://supabase.com/docs/reference/cli",
        "install": "npm install supabase --save-dev",
        "run":   "supabase start",
    },
    "wagmi": {
        "repo":  "https://github.com/wevm/wagmi",
        "path":  VENDOR_DIR / "wagmi",
        "docs":  "https://wagmi.sh",
        "install": "npm install wagmi viem",
        "run":   None,  # Library
    },
    "foundry": {
        "repo":  "https://github.com/foundry-rs/foundry",
        "path":  VENDOR_DIR / "foundry",
        "docs":  "https://book.getfoundry.sh",
        "install": "curl -L https://foundry.paradigm.xyz | bash",
        "run":   "forge test",
    },
    "sentry-javascript": {
        "repo":  "https://github.com/getsentry/sentry-javascript",
        "path":  VENDOR_DIR / "sentry-javascript",
        "docs":  "https://docs.sentry.io/platforms/javascript/",
        "install": "npm install @sentry/node",
        "run":   None,  # Library
    },
    "libsodium": {
        "repo":  "https://github.com/jedisct1/libsodium",
        "path":  VENDOR_DIR / "libsodium",
        "docs":  "https://doc.libsodium.org",
        "install": "pip install pynacl",
        "run":   None,  # Library
    },
    "hono": {
        "repo":  "https://github.com/honojs/hono",
        "path":  VENDOR_DIR / "hono",
        "docs":  "https://hono.dev/docs",
        "install": "npm install hono",
        "run":   None,  # Library
    },
    "clerk-javascript": {
        "repo":  "https://github.com/clerk/javascript",
        "path":  VENDOR_DIR / "clerk-javascript",
        "docs":  "https://clerk.com/docs",
        "install": "npm install @clerk/nextjs",
        "run":   None,  # Library
    },
    "ppt-master": {
        "repo":  "https://github.com/hugohe3/ppt-master",
        "path":  VENDOR_DIR / "ppt-master",
        "docs":  "https://github.com/hugohe3/ppt-master#readme",
        "install": "pip install ppt-master",
        "run":   "python -m ppt_master",
    },
    "free-for-dev": {
        "repo":  "https://github.com/ripienaar/free-for-dev",
        "path":  VENDOR_DIR / "free-for-dev",
        "docs":  "https://free-for.dev",
        "install": None,  # Reference list only
        "run":   None,
    },
    "public-apis": {
        "repo":  "https://github.com/public-apis/public-apis",
        "path":  VENDOR_DIR / "public-apis",
        "docs":  "https://github.com/public-apis/public-apis#readme",
        "install": None,  # Reference list only
        "run":   None,
    },
    "cline": {
        "repo":  "https://github.com/cline/cline",
        "path":  VENDOR_DIR / "cline",
        "docs":  "https://github.com/cline/cline#readme",
        "install": "npm install -g cline",
        "run":   "cline",
    },
}


class AgentRouter:
    """Dynamic Agent Routing Engine (Antonio Gulli Pattern #2 & #7).
    Routes task types to official vendor submodule entry points.
    """

    ROUTES = {
        "scrape":       "browser-use",
        "orchestrate":  "deepseek-harness",
        "train":        "unsloth",
        "finetune":     "axolotl",
        "serve":        "vllm",
        "research":     "firecrawl",
        "memory":       "letta",
        "security":     "strix",
        "pentest":      "strix",
        "web3":         "wagmi",
        "contract":     "foundry",
        "interpret":    "nnsight",
        "db":           "supabase-cli",
        "auth":         "clerk-javascript",
        "deck":         "ppt-master",
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
        os.system(f'cd "{path}" && npm install --silent && npm start -- --port {port}')

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
        os.system(f'pip install -e "{path}" --quiet')
        os.system(f'python -c "import asyncio; from browser_use import Agent; from langchain_openai import ChatOpenAI; asyncio.run(Agent(task=\'{task_description}\', llm=ChatOpenAI(model=\'gpt-4o\')).run())"')

    @staticmethod
    def launch_letta():
        """Launch Letta Agent Memory server using its official CLI."""
        path = PhysicalAgentEngine._check_vendor("letta")
        if not path:
            return
        info = VENDOR_CATALOG["letta"]
        logger.info(f"Launching official Letta server → {info['docs']}")
        os.system(f'pip install -e "{path}" --quiet && letta server')

    @staticmethod
    def launch_unsloth_train(config_path: str):
        """Run training via official Unsloth from vendor/unsloth."""
        path = PhysicalAgentEngine._check_vendor("unsloth")
        if not path:
            return
        info = VENDOR_CATALOG["unsloth"]
        logger.info(f"Launching official Unsloth → {info['docs']}")
        os.system(f'pip install -e "{path}" --quiet && python "{config_path}"')

    @staticmethod
    def launch_strix(target: str):
        """Run Strix security scan using its official entry point."""
        path = PhysicalAgentEngine._check_vendor("strix")
        if not path:
            return
        info = VENDOR_CATALOG["strix"]
        logger.info(f"Launching official Strix scan on {target} → {info['docs']}")
        os.system(f'pip install -e "{path}" --quiet && strix scan --target {target}')


if __name__ == "__main__":
    engine = OrchestratorEngine()
    print(json.dumps(engine.list_vendors(), indent=2))
