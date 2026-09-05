"""
SYZYGY Memory Layer: OpenViking (viking://) & Persistent Agent Context
"""

import time
from typing import Dict, Any, Optional, List

class OpenVikingClient:
    def __init__(self, base_uri: str = "viking://"):
        self.base_uri = base_uri
        self._store: Dict[str, Any] = {}

    def put(self, uri: str, payload: Dict[str, Any], tags: Optional[List[str]] = None) -> Dict[str, Any]:
        """Store context record at specified viking:// URI."""
        record = {
            "uri": uri,
            "timestamp": int(time.time()),
            "payload": payload,
            "tags": tags or []
        }
        self._store[uri] = record
        return {"status": "STORED", "uri": uri, "timestamp": record["timestamp"]}

    def get(self, uri: str) -> Optional[Dict[str, Any]]:
        """Retrieve context record from viking:// URI."""
        return self._store.get(uri)

    def list_prefix(self, prefix: str) -> List[Dict[str, Any]]:
        return [record for uri, record in self._store.items() if uri.startswith(prefix)]
