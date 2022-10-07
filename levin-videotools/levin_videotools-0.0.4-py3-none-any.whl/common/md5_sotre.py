import hashlib
import os
import sqlite3
from dataclasses import dataclass

_SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS md5_tbl (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gmt_create TEXT NOT NULL,
    md5_val TEXT NOT NULL,
    file_name TEXT NOT NULL
);

CREATE UNIQUE INDEX IF NOT EXISTS unique_md5_idx ON md5_tbl (md5_val);
"""

_READ_FILE_BUFFER = 8192


# 获取文件的md5值
def get_file_md5(file_name):
    md5 = hashlib.md5()
    with open(file_name, "rb") as f:
        while True:
            data = f.read(_READ_FILE_BUFFER)
            if not data:
                break
            md5.update(data)

    return md5.hexdigest()


@dataclass
class Md5Item:
    id: int
    gmt_create: str
    md5_val: str
    file_name: str


class Md5Store:
    def __init__(self, data_store=None):
        if data_store:
            self._data_store = data_store
        else:
            self._data_store = "data/md5_store.db"

        if not os.path.exists(os.path.dirname(self._data_store)):
            os.makedirs(os.path.dirname(self._data_store))

        self._conn = sqlite3.connect(self._data_store)

    def check_exists(self, md5_val):
        query_sql = f"""
        SELECT id, gmt_create, md5_val, file_name
        FROM md5_tbl
        WHERE md5_val = '{md5_val}'
        """
        cursor = self._select(query_sql)
        row = cursor.fetchone()
        if row:
            return Md5Item(
                id=row[0],
                gmt_create=row[1],
                md5_val=row[2],
                file_name=row[3]
            )
        return None

    def check_exists_file(self, file_name):
        md5_val = get_file_md5(file_name)
        result = self.check_exists(md5_val)
        if not result:
            result = Md5Item(
                id=None,
                gmt_create=None,
                md5_val=md5_val,
                file_name=None,
            )
        return result

    def check_or_insert(self, file_name):
        check_result = self.check_exists_file(file_name)
        if check_result.id:
            return check_result
        self.insert_md5_item(check_result.md5_val, file_name)
        return False

    def insert_md5_item(self, md5_val, file_name):
        insert_sql = f"""
        INSERT INTO md5_tbl(gmt_create, md5_val, file_name)
        VALUES (DATETIME('now','localtime')  , '{md5_val}', '{file_name}')
        """
        self._execute_commit(insert_sql)

    # 创建书签表
    def init(self):
        self._conn.executescript(_SQL_CREATE_TABLE)
        self._conn.commit()

    # 关闭数据库连接
    def close(self):
        self._conn.close()

    def _execute_commit(self, sql):
        self._conn.execute(sql)
        self._conn.commit()

    def _select(self, query_sql):
        cursor = self._conn.cursor()
        return cursor.execute(query_sql)
