# File Allocation Table Prone

import sqlite3

conn = sqlite3.connect("fatp.db")

cursor = conn.cursor

cursor.execute("""
    CREATE TABLE IF NOT EXISTS FATP (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        read INTEGER,
        write INTEGER,
        run INTEGER,
        creation_date DATETIME,
        last_modified DATETIME
    )
""")