"""
SYZYGY Memory Layer: SQLite Persistent Agent Context
Replaces the in-memory dict with a real SQLite database.
"""

import time
import sqlite3
import json
from typing import Dict, Any, Optional, List
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "syzygy_memory.db"

class OpenVikingClient:
    def __init__(self, base_uri: str = "viking://"):
        self.base_uri = base_uri
        self.conn = sqlite3.connect(DB_PATH)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                uri TEXT PRIMARY KEY,
                timestamp INTEGER,
                payload TEXT,
                tags TEXT
            )
        ''')
        self.conn.commit()

    def put(self, uri: str, payload: Dict[str, Any], tags: Optional[List[str]] = None) -> Dict[str, Any]:
        """Store context record at specified viking:// URI in SQLite."""
        timestamp = int(time.time())
        payload_str = json.dumps(payload)
        tags_str = json.dumps(tags or [])
        
        cursor = self.conn.cursor()
        cursor.execute(
            'INSERT OR REPLACE INTO memory (uri, timestamp, payload, tags) VALUES (?, ?, ?, ?)',
            (uri, timestamp, payload_str, tags_str)
        )
        self.conn.commit()
        return {"status": "STORED", "uri": uri, "timestamp": timestamp}

    def get(self, uri: str) -> Optional[Dict[str, Any]]:
        """Retrieve context record from viking:// URI."""
        cursor = self.conn.cursor()
        cursor.execute('SELECT timestamp, payload, tags FROM memory WHERE uri = ?', (uri,))
        row = cursor.fetchone()
        if row:
            return {
                "uri": uri,
                "timestamp": row[0],
                "payload": json.loads(row[1]),
                "tags": json.loads(row[2])
            }
        return None

    def list_prefix(self, prefix: str) -> List[Dict[str, Any]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT uri, timestamp, payload, tags FROM memory WHERE uri LIKE ?', (f'{prefix}%',))
        rows = cursor.fetchall()
        
        results = []
        for row in rows:
            results.append({
                "uri": row[0],
                "timestamp": row[1],
                "payload": json.loads(row[2]),
                "tags": json.loads(row[3])
            })
        return results
