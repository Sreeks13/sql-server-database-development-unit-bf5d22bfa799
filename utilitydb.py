import sqlite3

DB_NAME = "utility.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def setup_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS meters (
            meter_id INTEGER PRIMARY KEY,
            meter_number TEXT NOT NULL,
            location TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            reading_id INTEGER PRIMARY KEY,
            meter_id INTEGER NOT NULL,
            reading_value REAL NOT NULL,
            reading_date TEXT NOT NULL,
            FOREIGN KEY (meter_id) REFERENCES meters(meter_id)
        )
    """)

    cur.execute("DELETE FROM readings")
    cur.execute("DELETE FROM meters")

    cur.executemany(
        "INSERT INTO meters (meter_id, meter_number, location) VALUES (?, ?, ?)",
        [
            (1, "MTR-001", "Building A"),
            (2, "MTR-002", "Building B"),
            (3, "MTR-003", "Building C"),
            (4, "MTR-004", "Building D")
        ]
    )

    cur.executemany(
        """INSERT INTO readings
           (reading_id, meter_id, reading_value, reading_date)
           VALUES (?, ?, ?, ?)""",
        [
            (1, 1, 1250.5, "2026-10-01"),
            (2, 2, 980.25, "2026-10-01"),
            (3, 1, 1275.75, "2026-10-02")
        ]
    )

    conn.commit()
    return conn


if __name__ == "__main__":
    setup_database()
    print("Database created successfully.")
