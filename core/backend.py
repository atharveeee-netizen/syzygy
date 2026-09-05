"""
SupabaseBackendAgent
Domain: Backend Architecture & APIs
Stack: Supabase + Hono (Edge Functions)
"""
import logging
import subprocess
import os

logger = logging.getLogger("SYZYGY.SupabaseBackendAgent")

class SupabaseBackendAgent:
    def __init__(self):
        logger.info("Initializing SupabaseBackendAgent for Backend & Edge Functions.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        logger.info(f"Executing Supabase initialization in {project_dir}")
        
        try:
            # We use subprocess to run the supabase CLI (assuming npx is available)
            # using shell=True for npx resolution on Windows
            result = subprocess.run(
                ["npx", "supabase", "init"],
                cwd=project_dir,
                capture_output=True,
                text=True,
                shell=True
            )
            
            if result.returncode == 0:
                logger.info("Supabase initialized successfully.")
                return {"status": "SUCCESS", "module": "backend", "output": result.stdout}
            else:
                logger.error(f"Supabase init failed: {result.stderr}")
                return {"status": "FAILED", "module": "backend", "error": result.stderr}
                
        except Exception as e:
            logger.error(f"Exception during Supabase init: {e}")
            return {"status": "ERROR", "module": "backend", "error": str(e)}
