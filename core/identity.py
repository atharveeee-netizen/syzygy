"""
ClerkAuthAgent
Domain: Authentication & Identity
Stack: Clerk + RBAC / Auth.js
"""
import logging
import os

logger = logging.getLogger("SYZYGY.ClerkAuthAgent")

class ClerkAuthAgent:
    def __init__(self):
        logger.info("Initializing ClerkAuthAgent for Identity & Session Management.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        logger.info(f"Executing identity scaffolding in {project_dir}")
        
        middleware_path = os.path.join(project_dir, "middleware.ts")
        middleware_content = """import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

const isPublicRoute = createRouteMatcher(['/sign-in(.*)', '/sign-up(.*)', '/', '/api/webhook(.*)']);

export default clerkMiddleware(async (auth, request) => {
  if (!isPublicRoute(request)) {
    await auth.protect();
  }
});

export const config = {
  matcher: [
    '/((?!_next|[^?]*\\\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/(api|trpc)(.*)',
  ],
};
"""
        with open(middleware_path, "w", encoding="utf-8") as f:
            f.write(middleware_content)
            
        logger.info(f"Generated Clerk auth middleware at {middleware_path}")
        return {"status": "SUCCESS", "module": "identity", "files": [middleware_path]}
