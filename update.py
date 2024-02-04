# update.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_tasks_table(conn):
    """Create the tasks table if it doesn't exist."""
    create_tasks_sql = """
    -- tasks table
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        status VARCHAR(15) NOT NULL,
        begin_date TEXT NOT NULL,
        end_date TEXT NOT NULL
    );
    """

    try:
        c = conn.cursor()
        c.execute(create_tasks_sql)
    except Error as e:
        print(e)

def update(conn, table, row_id, **kwargs):
    """
    Update specified columns in a row of the given table.
    :param conn: Connection object
    :param table: Table name
    :param row_id: Row id
    :param kwargs: Dictionary of columns and values to update
    :return: True if update is successful, False otherwise
    """
    if not kwargs:
        print("No columns specified for update.")
        return False

    parameters = ", ".join(f"{k} = ?" for k in kwargs)
    values = tuple(kwargs.values())
    values += (row_id,)

    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''

    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("Update successful.")
        return True
    except sqlite3.Error as e:
        print(f"Error during update: {e}")
        return False

if __name__ == "__main__":
    conn = create_connection("database.db")
    if conn:
        create_tasks_table(conn)

        update(conn, "tasks", 2, status="started")
        update(conn, "tasks", 2, status="started")

        conn.close()
