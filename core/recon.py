"""
ReconEngineAgent
Domain: Autonomous Reconnaissance — GitHub, Web, CAD/Simulation file discovery
Stack: GitHub REST API (unauthenticated) + Firecrawl (vendor/firecrawl) subprocess
"""

import json
import logging
import subprocess
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List, Optional

logger = logging.getLogger("SYZYGY.ReconEngine")

VENDOR_DIR = Path(__file__).resolve().parent.parent / "vendor"
GITHUB_API = "https://api.github.com"


class ReconEngineAgent:
    """
    Autonomous Reconnaissance Engine.
    Searches GitHub (live API) and the web (via firecrawl) for pre-existing
    codebases, hardware designs, PCB schematics, CAD files, and templates.

    All results are LIVE — zero hardcoded data.
    """

    def __init__(self, github_token: Optional[str] = None):
        self.headers = {"Accept": "application/vnd.github+json"}
        if github_token:
            self.headers["Authorization"] = f"Bearer {github_token}"

    # ── GitHub Search (live API, no auth required for 10 req/min) ──────────

    def search_github(self, query: str, topic: str = "", max_results: int = 5) -> List[Dict[str, Any]]:
        """Search GitHub repositories using the official REST API."""
        search_query = f"{query} {topic}".strip()
        params = urllib.parse.urlencode({
            "q": search_query,
            "sort": "stars",
            "order": "desc",
            "per_page": max_results,
        })
        url = f"{GITHUB_API}/search/repositories?{params}"
        logger.info(f"[ReconAgent] GitHub API → {url}")

        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            results = []
            for repo in data.get("items", []):
                results.append({
                    "repo": repo["full_name"],
                    "url": repo["html_url"],
                    "description": repo.get("description", ""),
                    "stars": repo["stargazers_count"],
                    "language": repo.get("language", ""),
                    "updated": repo.get("updated_at", ""),
                })
            logger.info(f"[ReconAgent] Found {len(results)} repos for '{search_query}'")
            return results

        except Exception as e:
            logger.error(f"[ReconAgent] GitHub API error: {e}")
            return [{"error": str(e), "query": search_query, "fix": "Check network or rate limit (60 req/hr unauthenticated)"}]

    # ── Web Search (via firecrawl subprocess) ─────────────────────────────

    def search_web(self, query: str, max_results: int = 3) -> List[Dict[str, Any]]:
        """
        Search the web using the cloned vendor/firecrawl tool.
        Falls back to a DuckDuckGo HTML scrape if firecrawl is not installed.
        """
        firecrawl_path = VENDOR_DIR / "firecrawl"
        logger.info(f"[ReconAgent] Web search for: '{query}'")

        # Try firecrawl first
        if firecrawl_path.exists():
            try:
                result = subprocess.run(
                    ["python", "-m", "firecrawl", "search", query, "--limit", str(max_results)],
                    capture_output=True, text=True, timeout=30, cwd=str(firecrawl_path)
                )
                if result.returncode == 0 and result.stdout.strip():
                    try:
                        return json.loads(result.stdout)
                    except json.JSONDecodeError:
                        return [{"source": "firecrawl", "raw_output": result.stdout.strip()}]
            except Exception as e:
                logger.warning(f"[ReconAgent] Firecrawl subprocess failed: {e}")

        # Fallback: DuckDuckGo Instant Answer API (free, no key)
        try:
            params = urllib.parse.urlencode({"q": query, "format": "json", "no_redirect": 1})
            url = f"https://api.duckduckgo.com/?{params}"
            req = urllib.request.Request(url, headers={"User-Agent": "SYZYGY-Recon/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))

            results = []
            # Abstract result
            if data.get("Abstract"):
                results.append({
                    "title": data.get("Heading", query),
                    "url": data.get("AbstractURL", ""),
                    "snippet": data["Abstract"],
                    "source": data.get("AbstractSource", "DuckDuckGo"),
                })
            # Related topics
            for topic in data.get("RelatedTopics", [])[:max_results]:
                if isinstance(topic, dict) and "Text" in topic:
                    results.append({
                        "title": topic.get("Text", "")[:100],
                        "url": topic.get("FirstURL", ""),
                        "source": "DuckDuckGo",
                    })
            if not results:
                results.append({"status": "NO_RESULTS", "query": query, "note": "Try a more specific query"})
            return results

        except Exception as e:
            logger.error(f"[ReconAgent] Web search fallback failed: {e}")
            return [{"error": str(e), "query": query}]

    # ── CAD & Simulation File Search (GitHub code search) ─────────────────

    def search_cad_and_simulation(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Search GitHub for CAD files (.step, .stl, .urdf, .xacro) using code search.
        Uses the GitHub REST API with extension filters.
        """
        extensions = ["step", "stl", "urdf", "xacro", "kicad_pcb", "FCStd"]
        all_results = []

        for ext in extensions[:3]:  # Limit to 3 extensions to avoid rate limits
            search_query = f"{query} extension:{ext}"
            params = urllib.parse.urlencode({
                "q": search_query,
                "per_page": min(max_results, 3),
            })
            url = f"{GITHUB_API}/search/code?{params}"

            try:
                req = urllib.request.Request(url, headers=self.headers)
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode("utf-8"))

                for item in data.get("items", []):
                    all_results.append({
                        "file": item.get("name", ""),
                        "path": item.get("path", ""),
                        "repo": item.get("repository", {}).get("full_name", ""),
                        "url": item.get("html_url", ""),
                        "extension": ext,
                        "source": "GitHub Code Search",
                    })
            except Exception as e:
                logger.warning(f"[ReconAgent] GitHub code search for .{ext} failed: {e}")

        if not all_results:
            all_results.append({"status": "NO_CAD_FILES", "query": query, "searched_extensions": extensions})

        logger.info(f"[ReconAgent] Found {len(all_results)} CAD/simulation files for '{query}'")
        return all_results

    # ── Main Orchestrator ─────────────────────────────────────────────────

    def execute_recon(self, task_description: str) -> Dict[str, Any]:
        """Main orchestrator for reconnaissance. All results are LIVE."""
        logger.info(f"[ReconAgent] === RECONNAISSANCE ENGINE STARTED ===")
        logger.info(f"[ReconAgent] Task: {task_description}")

        keywords = task_description.lower().replace("find", "").strip()

        report = {
            "query": task_description,
            "repositories": self.search_github(keywords),
            "articles": self.search_web(keywords),
        }

        # Auto-detect if CAD/robotics/PCB search is needed
        cad_triggers = ["cad", "robot", "sim", "pcb", "hardware", "3d print", "stl", "urdf", "kicad"]
        if any(trigger in keywords for trigger in cad_triggers):
            report["cad_and_simulation"] = self.search_cad_and_simulation(keywords)

        report["status"] = "COMPLETE"
        logger.info(f"[ReconAgent] === RECONNAISSANCE COMPLETE ===")
        return report


if __name__ == "__main__":
    agent = ReconEngineAgent()
    result = agent.execute_recon("find open source esp32 motor controller with pcb design")
    print(json.dumps(result, indent=2))
