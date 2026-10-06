import sqlite3
from utilitydb import setup_database


def run_query(conn, sql):
    return conn.execute(sql).fetchall()


def test_inner_join_pairs_readings_with_meters():
    conn = setup_database()

    sql = """
        SELECT
            m.meter_id,
            m.meter_number,
            r.reading_id,
            r.reading_value
        FROM meters AS m
        INNER JOIN readings AS r
            ON m.meter_id = r.meter_id
        ORDER BY r.reading_id
    """

    rows = run_query(conn, sql)

    assert len(rows) == 3
    assert rows[0][1] == "MTR-001"
    assert rows[1][1] == "MTR-002"
    assert rows[2][1] == "MTR-001"

    conn.close()


def test_left_join_finds_meters_without_readings():
    conn = setup_database()

    sql = """
        SELECT
            m.meter_id,
            m.meter_number
        FROM meters AS m
        LEFT JOIN readings AS r
            ON m.meter_id = r.meter_id
        WHERE r.reading_id IS NULL
        ORDER BY m.meter_id
    """

    rows = run_query(conn, sql)

    assert len(rows) == 2
    assert rows[0] == (3, "MTR-003")
    assert rows[1] == (4, "MTR-004")

    conn.close()
