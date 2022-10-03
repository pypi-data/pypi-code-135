"""MongoDB数据连接"""

import re
from typing import List, Any, Type, Optional, Iterator, Dict
import pymongo
from vxutils.database import vxDataBase, vxDBTable
from vxutils.dataclass import (
    vxDataClass,
    vxFloatField,
    vxUUIDField,
    vxField,
    vxIntField,
    vxBoolField,
    vxDatetimeField,
)
from vxutils import logger


_query_convertors = {
    "=": lambda res: (res["col"], res["value"]),
    "==": lambda res: (res["col"], res["value"]),
    ">": lambda res: (res["col"], {"$gt": res["value"]}),
    "<": lambda res: (res["col"], {"$lt": res["value"]}),
    ">=": lambda res: (res["col"], {"$ge": res["value"]}),
    "<=": lambda res: (res["col"], {"$le": res["value"]}),
    "!=": lambda res: (res["col"], {"$ne": res["value"]}),
    "<>": lambda res: (res["col"], {"$ne": res["value"]}),
    "is": lambda res: (res["col"], res["value"]),
}

_query_regexs = [
    "(?P<col>\\w{1,})\\s*(?P<operate>[>,=,<][=]{0,1})\\s*(?P<value>\\S{1,}$)",
    "(?P<col>\\w{1,})\\s*(?P<operate>!=|<>)\\s*(?P<value>\\S{1,}$)",
    "(?P<col>\\w{1,})\\s{1,}(?P<operate>is|like)\\s{1,}(?P<value>\\S{1,}$)",
]

# TODO 标准化以及格式化 查询条件: [col] [operator] [value]

column_convertor_map = {
    vxFloatField: float,
    vxIntField: int,
    vxDatetimeField: float,
    vxBoolField: bool,
}


class vxMongoDBCollection(vxDBTable):
    """mongodb collection实例"""

    def __init__(
        self,
        table_name: str,
        primary_keys: List[str],
        datacls: Type[vxDataClass],
        db: vxDataBase,
    ) -> None:
        super().__init__(table_name, primary_keys, datacls, db.get_connection())
        for col, vxfield in datacls.__dict__.items():
            if not isinstance(vxfield, vxField):
                continue

    def save(self, obj: vxDataClass) -> None:
        """保存vxdata obj对象

        Arguments:
            obj {vxDataClass} -- vxdata obj对象
        """

        query = {key: obj[key] for key in self._primary_keys}
        self._db[self._table_name].update_one(query, {"$set": obj.message}, upsert=True)

    def savemany(self, *objs: List[vxDataClass]) -> None:
        """同时保存多个obj对象

        Arguments:
            objs {List[vxDataClass]} -- 多个obj对象
        """
        updaters = []

        for obj in objs:
            query = {key: obj[key] for key in self._primary_keys}
            updaters.append(
                pymongo.UpdateOne(query, {"$set": obj.message}, upsert=True)
            )
        self._db[self._table_name].bulk_write(updaters)

    def find(self, query=None) -> Iterator:
        if query is None:
            query = {}

        cur = self._db[self._table_name].find(query, {"_id": 0})

        for data in cur:
            yield self._datacls(**data)

    def delete(self, obj: Optional[vxDataClass]) -> None:
        """删除vxdata obj对象

        Arguments:
            obj {vxDataClass} -- obj

        Raises:
            ValueError -- 若 obj 类型不是table对应的dataclass，则抛出 ValueError

        """
        query = {col: obj[col] for col in self._primary_keys}
        if not query:
            raise ValueError

        self._db[self._table_name].delete_one(query)

    def deletemany(self, query) -> None:
        """按条件删除vxdata obj对象

        Arguments:
            conditions {List[str]} -- 查询条件,如: "id=3","age>=5"...

        Raises:
            ValueError -- 若 conditions 为空，则抛出异常。希望清空表格时，适用 truncate()接口

        """

        if not query:
            raise ValueError

        self._db[self._table_name].delete_many(query)

    def distinct(self, col_name: str, query=None) -> List:
        """去重后的数值列表

        Arguments:
            col_name {str} -- 去重后列表名称

        Returns:
            List -- 去重后的数值列表
        """

        return self._db[self._table_name].distinct(col_name, query)

    def truncate(self) -> None:
        """清空数据表"""
        logger.warning(f"truncate table : {self._table_name}")
        self._db[self._table_name].delete_many({})

    def create_table(self) -> None:
        """创建数据库表格"""
        self._db[self._table_name].drop_indexes()
        indexmodels = []
        for col in self._primary_keys:
            self._db[self._table_name].create_index(col)
            indexmodels.append((col, pymongo.ASCENDING))
        self._db[self._table_name].create_index(indexmodels)

    def drop_table(self) -> None:
        raise NotImplementedError


class vxMongoDB(vxDataBase):
    """mongodb 数据库"""

    def __init__(self, db_uri, db_name: str = "", **kwargs):
        super().__init__(db_uri, db_name, **kwargs)
        self._dbconn = pymongo.MongoClient(db_uri)
        self._wc_majority = pymongo.WriteConcern(w=1)
        try:
            self._dbconn.admin.command("replSetGetStatus")
            self._is_replica_set = True
        except pymongo.errors.OperationFailure:
            self._is_replica_set = False

    def create_table(
        self,
        table_name: str,
        primory_keys: List[str],
        vxdatacls: Type[vxDataClass],
        if_exists: str = "ignore",
    ) -> "vxDBTable":
        """创建数据表

        Arguments:
            table_name {str} -- 数据表名称
            primory_keys {List[str]} -- 表格主键
            vxdatacls {_type_} -- 表格数据格式
            if_exists {str} -- 如果table已经存在，若参数为ignore ，则忽略；若参数为 drop，则drop掉已经存在的表格，然后再重新创建

        Returns:
            vxDBTable -- 返回数据表格实例
        """
        if table_name not in self.__dict__:
            collection = vxMongoDBCollection(table_name, primory_keys, vxdatacls, self)
            self.__dict__[table_name] = collection
            self.__dict__[table_name].create_table()
        return self.__dict__[table_name]

    def drop_table(self, table_name: str) -> None:
        """删除数据表

        Arguments:
            table_name {str} -- 数据表名称
        """

        dbtable = self.__dict__.pop(table_name, None)
        if dbtable:
            dbtable.drop_table()

    def get_connection(self) -> None:
        return self._dbconn[self._dbname]


class vxTest(vxDataClass):
    id = vxUUIDField()
    name = vxField()
    money = vxFloatField(0, 2, 0, 100000)


if __name__ == "__main__":
    db = vxMongoDB("mongodb://uat:uat@127.0.0.1", "uat")
    testtable = db.create_table("tests", ["id"], vxTest, db)

    testtable.truncate()
    for i in range(10):
        t1 = vxTest(name="hello world", money=100)
        t2 = vxTest(name="hello world2", money=200)
        t3 = vxTest(name="hello world3", money=300)
        testtable.savemany(*[t1, t2, t3])

    for obj in testtable.query("money>200"):
        print(obj)
    # print(t1)
    # testtable.save(t1)
    # for obj in testtable.query("id=a50fdcef-d2a6-4604-9349-67c8f02ea681"):
    #    testtable.deletemany("id=a50fdcef-d2a6-4604-9349-67c8f02ea681")
