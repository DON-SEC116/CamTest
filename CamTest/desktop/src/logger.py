import sqlite3
from datetime import datetime

class Logger:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        """Create table for storing test results."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS camera_tests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                camera_id INTEGER,
                os TEXT,
                resolution TEXT,
                frame_rate REAL,
                status TEXT
            )
        """)
        self.conn.commit()

    def log_result(self, result):
        """Log test result to database."""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO camera_tests (timestamp, camera_id, os, resolution, frame_rate, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().isoformat(),
            result["camera_id"],
            result["os"],
            result["resolution"],
            result["frame_rate"],
            result["status"]
        ))
        self.conn.commit()

    def __del__(self):
        self.conn.close()