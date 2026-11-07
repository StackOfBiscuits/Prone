# File Allocation Table Prone

import sqlite3

conn = sqlite3.connect("fatp.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS FATP (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        read INTEGER DEFAULT 1,
        write INTEGER DEFAULT 1,
        execute INTEGER DEFAULT 1,
        creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        last_modified DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()


def get_file_entry(filename):
    cursor.execute("""
        SELECT * FROM FATP WHERE filename = ?
    """, (filename,))

    file = cursor.fetchone()

    # File doesn't exist
    if file is None:
        return None

    # Check read permission
    if file[2] == 0:
        raise PermissionError(f"Read access denied: {filename}")

    return file


def create_file(filename):
    cursor.execute("""
        INSERT INTO FATP (filename, read, write, run)
        VALUES (?, 1, 1, 0)
    """, (filename,))

    conn.commit()

    return get_file_entry(filename)


def write_to_file(filename):
    file = get_file_entry(filename)

    # Check file exists
    if file is None:
        file = create_file(filename)

    # Check write permission
    if file[3] == 0:
        raise PermissionError(f"Write access denied: {filename}")

    return True