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
        "web3": ("core.web3", "WagmiWeb3Agent")
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

if __name__ == "__main__":
    engine = OrchestratorEngine()
    print(engine.dispatch({"id": "task-001", "type": "backend"}))
