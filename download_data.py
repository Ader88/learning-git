# download_data.py

import sqlite3
import os

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn

def select_all(conn, table):
    """
    Query all rows from the specified table.
    :param conn: Connection object
    :param table: Table name
    :return: List of rows
    """
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table};")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error during SELECT ALL from {table}: {e}")
        return None

def select_where(conn, table, **conditions):
    """
    Query rows from the specified table based on the provided conditions.
    :param conn: Connection object
    :param table: Table name
    :param conditions: Dictionary of conditions (column=value)
    :return: List of rows
    """
    try:
        cur = conn.cursor()
        condition_str = " AND ".join(f"{k} = {v!r}" for k, v in conditions.items())
        cur.execute(f"SELECT * FROM {table} WHERE {condition_str};")
        rows = cur.fetchall()
        return rows
    except sqlite3.Error as e:
        print(f"Error during SELECT WHERE from {table}: {e}")
        return None

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_dir, "database.db")

    conn = create_connection(db_file)

    # Testy

    # Wszystkie projekty
    print("Wszystkie projekty:")
    print(select_all(conn, "projects"))

    # Wszystkie zadania
    print("\nWszystkie zadania:")
    print(select_all(conn, "tasks"))

    # Wszystkie zadania dla projektu o id 1
    print("\nWszystkie zadania dla projektu o id 1:")
    print(select_where(conn, "tasks", project_id=1))

    # Wszystkie zadania ze statusem ended
    print("\nWszystkie zadania ze statusem ended:")
    print(select_where(conn, "tasks", status="ended"))

    conn.close()