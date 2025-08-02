import os
import contextlib
import mysql.connerctor


@contextlib.contextmanager
def get_mysql_conn(db):
    """
    Context manager to automatically close DB connection.
    We retrieve credentials from Environment variables
    """
    conn = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST'),
        user=os.environ.get('MYSQL_USER'),
        password=os.environ.get('MYSQL_PWD'),
        database=db
    )

    try:
        yield conn
    finally:
        conn.close()
