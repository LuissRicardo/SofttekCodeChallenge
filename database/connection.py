import sqlite3
from sqlite3 import Connection, Error

DB_PATH: str = "./database/database.db"
""" The relative path to the database file. """


def create_connection() -> Connection | None:
    """ Returns a connection to the database.

        If an error happens, it returns `None`.
    """
    conn: Connection | None = None

    try:
        conn = sqlite3.connect(DB_PATH)
    except Error as e:
        print(f"Error connection to database: {e}")

    return conn
