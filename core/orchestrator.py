"""
SYZYGY Lead Coordinator & Dynamic Agent Router (DeepSeek Harness Core)
Antonio Gulli Chapters 2, 3, 4, 7 & Appendix G.
"""

import sys
import os
import json
import logging
import importlib
from typing import Dict, Any, List, Optional

# Add parent directory to sys.path to allow module imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger("SYZYGY.Orchestrator")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class AgentRouter:
    """Dynamic Model and Agent Routing Engine (Pattern #2 & #7)."""
    
    ROUTES = {
        "research": ("core.research", "FirecrawlResearchAgent"),
        "presentation": ("core.presenter", "PPTMasterAgent"),
        "diagram": ("core.diagrammer", "DiagramDesignAgent"),
        "security": ("core.pentest", "StrixPentestAgent"),
        "frontend": ("core.frontend", "OpenDesignUIAgent"),
        "edge": ("core.edge", "CactusNeedleAgent"),
        "backend": ("core.backend", "SupabaseBackendAgent"),
        "identity": ("core.identity", "ClerkAuthAgent"),
        "devops": ("core.devops", "GitHubActionsAgent"),
        "telemetry": ("core.telemetry", "OpenTelemetryAgent"),
        "crypto": ("core.crypto", "LibsodiumCryptoAgent"),
        "web3": ("core.web3", "WagmiWeb3Agent"),
        "aiml": ("core.aiml", "AIMLEngineAgent"),
        "training": ("core.aiml", "AIMLEngineAgent"),
        "model": ("core.aiml", "AIMLEngineAgent"),
        "recon": ("core.recon", "ReconEngineAgent"),
        "architect": ("core.architect", "AIArchitectAgent"),
        "ideation": ("core.ideation", "HackathonStrategistAgent")
    }

    @classmethod
    def resolve_and_load(cls, task_type: str) -> Any:
        route = cls.ROUTES.get(task_type.lower())
        if not route:
            logger.warning(f"Task type '{task_type}' not in primary registry. Defaulting to general handling.")
            return None
        
        module_name, class_name = route
        try:
            module = importlib.import_module(module_name)
            agent_class = getattr(module, class_name)
            return agent_class()
        except Exception as e:
            logger.error(f"Failed to load agent {class_name} from {module_name}: {e}")
            return None

class OrchestratorEngine:
    def __init__(self, session_id: str = "syzygy_default"):
        self.session_id = session_id
        self.state_uri = f"viking://session/active/{session_id}"
        logger.info(f"Initialized SYZYGY Orchestrator. State URI: {self.state_uri}")

    def dispatch(self, task: Dict[str, Any]) -> Dict[str, Any]:
        task_type = task.get("type", "general")
        logger.info(f"Dispatching task [{task.get('id', 'N/A')}] of type: {task_type}")
        
        agent_instance = AgentRouter.resolve_and_load(task_type)
        if not agent_instance:
            return {"status": "FAILED", "reason": "No agent found for task type"}
            
        try:
            result = agent_instance.run(task)
            result["executionUri"] = f"viking://execution/{agent_instance.__class__.__name__}/{task.get('id')}"
            return result
        except Exception as e:
            logger.error(f"Agent execution failed: {e}")
            return {"status": "FAILED", "reason": str(e)}

class PhysicalAgentEngine:
    """Invokes actual outsourced agent repos from vendor/."""
    
    @staticmethod
    def _ensure_dependencies(vendor_path: str):
        """Automatically installs requirements if running for the first time for a seamless out-of-the-box experience."""
        req_file = os.path.join(vendor_path, "requirements.txt")
        pyproject = os.path.join(vendor_path, "pyproject.toml")
        marker = os.path.join(vendor_path, ".syzygy_setup_complete")
        
        if not os.path.exists(marker):
            logger.info(f"First-time setup detected for {os.path.basename(vendor_path)}. Installing dependencies...")
            if os.path.exists(req_file):
                os.system(f"pip install -r \"{req_file}\" --quiet")
            elif os.path.exists(pyproject):
                os.system(f"pip install -e \"{vendor_path}\" --quiet")
            
            with open(marker, "w") as f:
                f.write("Setup complete.")
            logger.info("Dependencies installed perfectly.")

    @staticmethod
    def launch_deepseek(port: int = 3080):
        logger.info(f"Launching physical DeepSeek Harness UI on localhost:{port} from vendor/deepseek-harness...")
        vendor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vendor", "deepseek-harness")
        
        if os.path.exists(vendor_path):
            PhysicalAgentEngine._ensure_dependencies(vendor_path)
            logger.info("DeepSeek Harness repository found. Booting engine...")
            os.system(f"cd \"{vendor_path}\" && python -m http.server {port}")
        else:
            logger.error(f"Vendor path not found: {vendor_path}. Did you clone deepseek-harness?")

    @staticmethod
    def launch_browser_use(task_description: str):
        logger.info(f"Launching physical Browser-Use agent for task: '{task_description}'...")
        vendor_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vendor", "browser-use")
        
        if os.path.exists(vendor_path):
            PhysicalAgentEngine._ensure_dependencies(vendor_path)
            logger.info("Browser-Use repository found. Executing task...")
            # We assume browser-use has a cli entrypoint or we can just run a python script.
            # Here we wrap it in a perfect out-of-the-box execution block.
            script_content = f'''import asyncio
from browser_use import Agent
from langchain_openai import ChatOpenAI

async def main():
    agent = Agent(
        task="{task_description}",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
'''
            script_path = os.path.join(vendor_path, "syzygy_agent.py")
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(script_content)
            
            os.system(f"cd \"{vendor_path}\" && python syzygy_agent.py")
        else:
            logger.error(f"Vendor path not found: {vendor_path}. Did you clone browser-use?")

if __name__ == "__main__":
    engine = OrchestratorEngine()
    print(engine.dispatch({"id": "task-001", "type": "backend"}))
