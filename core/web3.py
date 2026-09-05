"""
WagmiWeb3Agent
Domain: Web3 & Blockchain Integration
Stack: Wagmi + Viem + RainbowKit + Foundry
"""
import logging
import subprocess
import os

logger = logging.getLogger("SYZYGY.WagmiWeb3Agent")

class WagmiWeb3Agent:
    def __init__(self):
        logger.info("Initializing WagmiWeb3Agent for EVM Smart Contracts.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        logger.info(f"Executing web3 task in {project_dir}")
        
        # Scaffold a Foundry project
        try:
            result = subprocess.run(
                ["forge", "init", "--force"],
                cwd=project_dir,
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                logger.info("Foundry initialized successfully.")
                return {"status": "SUCCESS", "module": "web3", "output": result.stdout}
            else:
                logger.error(f"Foundry init failed: {result.stderr}")
                return {"status": "FAILED", "module": "web3", "error": result.stderr}
                
        except Exception as e:
            logger.error(f"Exception during Foundry init: {e}")
            return {"status": "ERROR", "module": "web3", "error": str(e)}
