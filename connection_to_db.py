#conection_to_db.py`

import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, SQLite version: {sqlite3.sqlite_version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_connection_in_memory():
    """Create a database connection to a SQLite in-memory database."""
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        print(f"Connected, SQLite version: {sqlite3.sqlite_version}")
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file_path = os.path.join(current_dir, "database.db")
    create_connection(db_file_path)
    create_connection_in_memory()