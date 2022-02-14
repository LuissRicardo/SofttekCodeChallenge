from datetime import datetime
from sqlite3 import Connection, Cursor, Error, Row
from typing import Any

from database.connection import create_connection
from utils.datetime_utils import datetime_to_season


def execute_select_all(select_all_query: str) -> list[dict[str, Any]] | None:
    """ Executes a select all query and returns a list with the
    retrieved data.

    Returns `None` if an error occurs.

    :param select_all_query: Query to execute in the DB.
    :return: List that contains the data in the DB.
    """
    conn: Connection | None = create_connection()
    cursor: Cursor | None = None

    try:
        conn.row_factory = Row  # Sets the format of the rows as a dict-ish.
        cursor: Cursor = conn.cursor()

        cursor.execute(select_all_query)  # Execute the query
        return [dict(row) for row in cursor.fetchall()]  # Transform data to dicts.
    except Error as e:
        print(f"Error executing query: {e}")
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()


CUSTOMER_ORDER_STATUS_SELECT_QUERY: str = """
    SELECT DISTINCT
        order_number,
        (SELECT O.name
            FROM order_status as O
            WHERE O.order_status_id = (SELECT MAX(D.order_status_id)
                                            FROM customer_ord_lines AS D
                                            WHERE C.order_number = D.order_number)) as status
    FROM
        customer_ord_lines AS C;
"""


def get_customer_order_status_list() -> list[dict[str, Any]] | None:
    """ Returns the status of the customer orders. """
    return execute_select_all(CUSTOMER_ORDER_STATUS_SELECT_QUERY)


DETECTING_CHANGE_SELECT_QUERY: str = """
    SELECT date, was_rainy
    FROM (SELECT date, was_rainy, LAG(was_rainy) OVER(ORDER BY ROWID) AS "prev_was_rainy"
            FROM weather)
    WHERE was_rainy == 1 AND prev_was_rainy == 0;
"""


def get_detecting_change_list() -> list[dict[str, Any]] | None:
    """ Returns the list of detected changes in the weather. """
    data = execute_select_all(DETECTING_CHANGE_SELECT_QUERY)

    # `was_rainy` column contains an integer, transform it to
    # `True` if its truthy or `False` otherwise.
    def process_row(row: dict) -> dict:
        row["was_rainy"] = "True" if row["was_rainy"] else "False"
        return row

    return list(map(process_row, data))


SEASONS_PROBLEM_SELECT_QUERY = """
    SELECT C.ord_id, C.ord_dt FROM customer_orders AS C;
"""


def get_seasons_orders_list() -> list[dict[str, Any]] | None:
    """ Returns the list of orders and the season the order was made. """
    data = execute_select_all(SEASONS_PROBLEM_SELECT_QUERY)

    def process_row(row: dict) -> dict:
        season = datetime_to_season(datetime.fromisoformat(row["ord_dt"]))
        return {"ord_id": row["ord_id"], "season": season}

    return list(map(process_row, data))
