# add_task.py

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

def check_and_add_project_id_column(conn):
    """
    Sprawdź, czy tabela tasks zawiera kolumnę project_id, a jeśli nie, dodaj ją.
    :param conn: Obiekt Connection do bazy danych
    :return: None
    """
    try:
        # Utwórz kursor
        cur = conn.cursor()

        # Sprawdź, czy tabela tasks zawiera kolumnę project_id
        cur.execute("SELECT project_id FROM tasks LIMIT 1;")
        conn.commit()
        print("Kolumna project_id już istnieje w tabeli tasks.")
    except sqlite3.Error:
        # Jeśli kolumna project_id nie istnieje, dodaj ją
        cur.execute("ALTER TABLE tasks ADD COLUMN project_id INTEGER;")
        conn.commit()
        print("Pomyślnie dodano kolumnę project_id do tabeli tasks.")
    except Exception as e:
        print(f"Błąd podczas sprawdzania i dodawania kolumny project_id: {e}")

def check_and_create_projects_table(conn):
    """
    Sprawdź, czy tabela projects istnieje, a jeśli nie, utwórz ją.
    :param conn: Obiekt Connection do bazy danych
    :return: None
    """
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1 FROM projects LIMIT 1;")
    except sqlite3.Error:
        # Jeśli tabela projects nie istnieje, utwórz ją
        create_projects_sql = """
        -- projects table
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            nazwa TEXT NOT NULL,
            start_date TEXT,
            end_date TEXT
        );
        """
        cur.execute(create_projects_sql)
        conn.commit()
        print("Pomyślnie utworzono tabelę projects.")
    except Exception as e:
        print(f"Błąd podczas sprawdzania istnienia tabeli projects: {e}")

def add_project(conn, project):
    """
    Create a new project into the projects table
    :param conn: Connection object
    :param project: Tuple with project data
    :return: project id
    """
    try:
        check_and_create_projects_table(conn)

        sql = '''INSERT INTO projects(nazwa, start_date, end_date)
                 VALUES(?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Błąd podczas dodawania projektu: {e}")
        return None

def add_task(conn, task):
    """
    Create a new task into the tasks table
    :param conn: Connection object
    :param task: Tuple with task data
    :return: task id
    """
    try:
        check_and_add_project_id_column(conn)
        check_and_create_projects_table(conn)

        sql = '''INSERT INTO tasks(project_id, nazwa, opis, status, start_date, end_date)
                 VALUES(?, ?, ?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid
    except sqlite3.Error as e:
        print(f"Błąd podczas dodawania zadania: {e}")
        return None

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(current_dir, "database.db")

    conn = create_connection(db_file)

    # Wywołaj funkcję sprawdzania i dodawania kolumny project_id
    check_and_add_project_id_column(conn)

    project = ("Powtórka z angielskiego", "2020-05-11 00:00:00", "2020-05-13 00:00:00")
    pr_id = add_project(conn, project)

    if pr_id is not None:
        # Wywołaj funkcję sprawdzania i dodawania kolumny project_id
        check_and_add_project_id_column(conn)

        task = (
            pr_id,
            "Czasowniki regularne",
            "Zapamiętaj czasowniki ze strony 30",
            "started",
            "2020-05-11 12:00:00",
            "2020-05-11 15:00:00"
        )

        task_id = add_task(conn, task)

        if task_id is not None:
            print(pr_id, task_id)

    conn.close()