import contextlib
import sqlalchemy as sa
import os
import pandas as pd


@contextlib.contextmanager
def get_db_connection() -> str:
    """
    Generates a db connection to an instance on an SQL Server
    and manages it's lifecycle
    Note - requires the OS ENV VAR outlines in .env.example
    Note - requires ODBC Driver 17 for SQL Server to be installed
    at the OS level
    """

    conn = None

    connection_url = sa.engine.URL.create(
        'mssql+pyodbc',
        username=os.getenv('NAV_SERVER_USERNAME'),
        password=os.getenv('NAV_SERVER_PASSWORD'),
        host=os.getenv('NAV_SERVER'),
        database=os.getenv('NAV_DATABASE'),
        query={'driver': 'ODBC Driver 17 for SQL Server'}
    )

    engine = sa.create_engine(connection_url)
    conn = engine.connect()

    try:
        yield conn
    except Exception as e:
        print(f" errrorr {e}")
    finally:
        conn.close()


def run_query(query) -> pd.DataFrame:
    """
    Runs a query and returns a pandas dataframe of the result
    Note - querys are responsbilbe for naming the column correctly
    using AS statements
    """

    with get_db_connection() as conn:
        query_result = pd.read_sql_query(query, conn)

    df = pd.DataFrame(query_result)
    df.rename(columns=df.iloc[0]).drop(df.index[0])
    return df
