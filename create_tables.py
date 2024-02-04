# create_tables.py

import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
        return conn
    except Error as e:
        print(e)

    return conn

def execute_sql(conn, sql):
    """Execute SQL script."""
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def create_projects_table(conn):
    """Create the projects table if it doesn't exist."""
    create_projects_sql = """
    -- projects table
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY,
        nazwa TEXT NOT NULL,
        start_date TEXT,
        end_date TEXT
    );
    """

    execute_sql(conn, create_projects_sql)

def create_tasks_table(conn):
    """Create the tasks table if it doesn't exist."""
    create_tasks_sql = """
    -- tasks table
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        project_id INTEGER,
        nazwa VARCHAR(250) NOT NULL,
        opis TEXT,
        status VARCHAR(15) NOT NULL,
        start_date TEXT NOT NULL,
        end_date TEXT NOT NULL,
        FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    execute_sql(conn, create_tasks_sql)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_dir, "database.db")

    conn = create_connection(db_file)
    if conn is not None:
        create_projects_table(conn)
        create_tasks_table(conn)
        conn.commit()
        conn.close()
        print("Tables created successfully.")
