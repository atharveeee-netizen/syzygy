"""
SYZYGY Research Agent: arXiv API Interface
Extracts papers from the official arXiv API. No fake DOIs.
"""

import logging
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from typing import Dict, Any, List

logger = logging.getLogger("SYZYGY.Research")

class FirecrawlResearchIndex:
    """
    Research agent that queries arXiv for real scientific papers.
    """
    def __init__(self, api_key: str = ""):
        self.api_key = api_key # Not needed for arXiv

    def search_and_extract(self, topic: str, max_papers: int = 3) -> List[Dict[str, Any]]:
        logger.info(f"Querying arXiv API for topic: '{topic}'")
        
        query = urllib.parse.quote(topic)
        url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_papers}&sortBy=relevance"
        
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "SYZYGY-Research/1.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                xml_data = resp.read()
            
            root = ET.fromstring(xml_data)
            namespace = {'atom': 'http://www.w3.org/2005/Atom'}
            
            results = []
            for entry in root.findall('atom:entry', namespace):
                title = entry.find('atom:title', namespace).text.strip().replace('\n', ' ')
                summary = entry.find('atom:summary', namespace).text.strip().replace('\n', ' ')
                link = entry.find('atom:id', namespace).text
                published = entry.find('atom:published', namespace).text
                
                authors = []
                for author in entry.findall('atom:author', namespace):
                    name = author.find('atom:name', namespace).text
                    authors.append(name)
                
                results.append({
                    "title": title,
                    "url": link,
                    "published": published,
                    "authors": authors,
                    "summary": summary
                })
            
            if not results:
                logger.warning(f"No papers found on arXiv for '{topic}'.")
                
            return results
            
        except Exception as e:
            logger.error(f"Failed to query arXiv: {e}")
            return [{"error": str(e), "topic": topic}]

if __name__ == "__main__":
    agent = FirecrawlResearchIndex()
    import json
    print(json.dumps(agent.search_and_extract("multi-agent reinforcement learning"), indent=2))
