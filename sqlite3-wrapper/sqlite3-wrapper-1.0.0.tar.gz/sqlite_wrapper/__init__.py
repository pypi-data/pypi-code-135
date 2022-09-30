import re
import os
import sqlite3
import time
import datetime as dt
import numpy as np
import pandas as pd

from typing import Union, List, Optional


def measure_exec_time(func):
    def time_it(*args, **kwargs):
        time_started = time.time()
        func(*args, **kwargs)
        time_elapsed = time.time()
        print(f"""{func.__name__} complete: wall time is {int((time_elapsed - time_started) * 1000)} milliseconds""")

    return time_it


class Sqlite3Wrapper:
    def __init__(self, db_name: str = 'etf_analytics', db_dir: Optional[str] = None):
        """
        SQLite3 wrapper.

        :param db_name: Database to connect and perform read/write operations on.
        :param db_dir: Directory where database nested in the event that the call
        to the database is made in a separate directory where the database is
        nested.
        """
        self.db_name = (
            f'{db_dir}{os.sep}{db_name}.db' if isinstance(db_dir, str) else f'{db_name}.db') if not re.search(
            '^:memory:$', db_name) else db_name
        self.con = sqlite3.connect(self.db_name)
        self.cur = None

    @staticmethod
    def sql_datatype_conversion(value: Union[int, float, bool, str, dt.datetime]) -> str:
        """
        Converting value type to sql type in string format.
        :param value: Value to interpret sql type
        :return: sql type to cast value
        """
        if isinstance(value, str):
            sql_type = 'varchar'
        elif isinstance(value, int) or isinstance(value, np.int64):
            sql_type = 'int'
        elif isinstance(value, bool):
            sql_type = 'bool'
        elif isinstance(value, float) or isinstance(value, np.float64):
            sql_type = 'float'
        elif isinstance(value, dt.datetime):
            sql_type = 'datetime'
        else:
            sql_type = 'varchar(100)'

        return sql_type

    def reset_con(self):
        """
        Reset database connection.
        :return:
        """
        self.con = sqlite3.connect(self.db_name)

    def set_cursor(self):
        """
        Setting sqlite3 cursor.
        :return:
        """
        self.cur = self.con.cursor()

    def close(self):
        """
        Closing database connection.
        :return:
        """
        self.con.close()

    @measure_exec_time
    def execute(self, query: str):
        """
        Activate cursor execute query.
        :param query: SQL query string.
        :return:
        """
        self.set_cursor()

        self.cur.execute(query)

        self.con.commit()

    def set_primary_key_constraint(self, table_name: str, primary_key: str):
        """
        Setting primary key constraint on existing table.
        :param table_name: Table name to set primary key on.
        :param primary_key: Column to set as primary key.
        :return:
        """
        query = f"ALTER TABLE {table_name} ADD PRIMARY KEY ({primary_key})"
        self.execute(query)

    def fetch_all_table_names(self) -> List[str]:
        """
        Fetch all table names in sqlite3 database.
        :return:
        """
        query = "SELECT name FROM sqlite_master WHERE type='table'"

        self.execute(query=query)

        result = self.cur.fetchall()

        return list(map(lambda x: x[0], result))

    def fetch_frame(self) -> pd.DataFrame:
        try:
            rows = self.cur.fetchall()
            cols = list(map(lambda x: x[0], self.cur.description))
        except AttributeError as error:
            raise error

        return pd.DataFrame(data=rows, columns=cols)

    def drop_table(self, table_name: str):
        """
        Drop table from database.
        :param table_name: Table name to drop from database.
        :return:
        """
        query = f"DROP TABLE {table_name}"

        print(f'Are you sure you want to drop table "{table_name}" from database "{self.db_name}"?')

        user_action = input('Enter Y/N')
        if user_action == 'Y':
            self.execute(query)
        else:
            pass

    def write_to_db(self, table_name: str, data: pd.DataFrame, primary_key_cols: List[str] = None):
        """
        Creates table in database (if table doesn't exist already) and inserts or replaces values
        in table potentially based on primary key constraints.

        :param table_name: Table name for which to insert or replace values into
        :param data: Data to perform a string based insert.
        :param primary_key_cols: Column name to set primary key constraint on.
        :return:
        """
        df_ = data

        if not isinstance(df_, pd.DataFrame) or df_.empty:
            raise AssertionError

        # note: only inspects the datatype of the first element of string based batch inserted data columns
        inspect_idx = 0
        create_table_col_string = ', '.join(
            list(map(lambda x: f'{x} {self.sql_datatype_conversion(df_.iloc[inspect_idx, :][x])}', df_.columns)))

        # setting primary key when creating table
        if isinstance(primary_key_cols, str):
            create_table_col_string += f", PRIMARY KEY ({', '.join(primary_key_cols)})"

        if table_name not in self.fetch_all_table_names():
            query = f"CREATE TABLE {table_name}({create_table_col_string})"
            self.execute(query)
        else:
            pass

        entries = ["(" + ", ".join(f"'{val}'" for val in row) + ")" for row in df_.values]
        argument_string = ", ".join(entries)
        cols = ", ".join([f'"{col}"' for col in df_.columns])

        try:
            query = f"INSERT OR REPLACE INTO {table_name}({cols}) VALUES " + argument_string
            self.execute(query)
        except Exception as error:
            self.con.rollback()
            raise Exception(error)

    def read_from_db(self, table_name: str, cols: List[str] = None) -> pd.DataFrame:
        """
        Read existing tables from database.

        :param table_name: Table name to read data from.
        :param cols: Specific columns to fetch.
        :return: Returns tabular data in pd.DataFrame format.
        """
        if cols is None:
            cols = ['*']

        query = f"SELECT {', '.join(cols)} FROM {table_name}"

        self.execute(query)

        return self.fetch_frame()
