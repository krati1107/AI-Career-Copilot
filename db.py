import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        skills TEXT,
        result TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(skills, result):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (skills, result) VALUES (?, ?)",
        (", ".join(skills), result)
    )

    conn.commit()
    conn.close()
