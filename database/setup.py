from sqlite3 import Connection, Cursor, Error

from database.connection import create_connection


def setup_database() -> bool:
    """ Initializes the database. """
    conn: Connection | None = create_connection()
    cursor: Cursor | None = None

    db_init_script_path: str = "./database/sql/database_init.sql"

    # Reads the SQL script that creates and populates the database.
    with open(db_init_script_path, "r") as db_init_file:
        db_init_sql = db_init_file.read()

    # Executes the script.
    try:
        cursor = conn.cursor()
        cursor.executescript(db_init_sql)
        conn.commit()
        return True
    except Error as e:
        print(f"Error initializing the database: {e}")
        return False
    finally:
        if conn:
            cursor.close()
            conn.close()
