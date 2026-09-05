"""
ScaffoldAuthAgent
Domain: Authentication & Identity Boilerplate Scaffolding
Note: This is a SCAFFOLDING tool. It generates boilerplate for Auth integrations.
"""
import logging
import os

logger = logging.getLogger("SYZYGY.ScaffoldAuthAgent")

class ScaffoldAuthAgent:
    def __init__(self):
        logger.info("Initializing ScaffoldAuthAgent for Identity & Session Management boilerplate.")

    def run(self, task):
        project_dir = task.get("project_dir", ".")
        logger.info(f"Executing identity scaffolding in {project_dir}")
        
        middleware_path = os.path.join(project_dir, "middleware.ts")
        middleware_content = """// SYZYGY Auth Middleware Boilerplate (Clerk)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server';

// Note: Ensure NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY is set in your .env.local

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
            
        logger.info(f"Generated Clerk auth middleware boilerplate at {middleware_path}")
        return {"status": "SUCCESS", "module": "identity", "files": [middleware_path]}
