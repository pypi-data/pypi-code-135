# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .idataappsrepo import IDataAppsRepo

from ..db import connect, Connection, transaction
from ..model import DataAppAttributes, DataAppField, DataAppProfile, PrincipalId


def get_id(dataapp_like: Union[int, DataAppProfile]) -> int:
    if isinstance(dataapp_like, DataAppProfile):
        return dataapp_like.id
    return int(dataapp_like)


def _next_id(conn: Connection) -> int:
    conn.execute("SELECT nextval('shapelets.id_gen')")
    return int(conn.fetchone()[0])


def _insert_dataapp(dataapp_id: int, details: DataAppAttributes, conn: Connection):
    conn.execute("""
            INSERT INTO dataapps 
            (id, name, version, description, creationDate, spec)
            VALUES (?, ?, ?, ?, ?, ?);
        """,
                 [
                     dataapp_id, details.name, details.version, details.description, details.creationDate, details.spec
                 ])


def _update_dataapp_by_id(dataapp_id: int, profile: Dict[str, Any], conn: Connection):
    pass


def _load_all(attributes: Set[DataAppField],
              skip: Optional[int],
              sort_by: Optional[List[Tuple[DataAppField, bool]]],
              limit: Optional[int],
              conn: Connection) -> List[DataAppProfile]:
    base_query = f"SELECT {', '.join(attributes)} FROM dataapps "
    if sort_by is not None:
        base_query += "ORDER BY "
        sort_expressions = [f"{s[0]} {'ASC' if s[1] else 'DESC'}" for s in sort_by]
        base_query += ', '.join(sort_expressions)
    if limit is not None:
        base_query += f" LIMIT {limit}"
    if skip is not None:
        base_query += f" OFFSET {skip}"

    conn.execute(base_query)
    result = []
    d = {}
    for r in conn.fetch_all():
        for idx, a in enumerate(attributes):
            d[a] = r[idx]
        result.append(DataAppProfile(**d))

    return result


def _load_dataapp_by_id(dataapp_id: int, conn: Connection) -> Optional[DataAppProfile]:
    conn.execute(""" 
        SELECT name, version, description, creationDate, spec
        FROM dataapps
        WHERE id = ?;
    """, [dataapp_id])

    record = conn.fetch_one()
    if record is None:
        return None

    return DataAppProfile(id=dataapp_id, name=record[0], version=record[1], description=record[2],
                          creationDate=record[3], spec=record[4])


def _load_dataapp_by_name(dataapp_name: str, conn: Connection) -> Optional[DataAppProfile]:
    conn.execute(""" 
        SELECT *
        FROM dataapps
        WHERE name = ?
        ORDER BY version;
    """, [dataapp_name])

    record = conn.fetch_one()
    if record is None:
        return None

    return DataAppProfile(id=record[0], name=record[1], version=record[2], description=record[3],
                          creationDate=record[4], spec=record[5])


def _delete_dataapp(dataapp_id: int, conn: Connection):
    conn.execute("DELETE FROM dataapps WHERE id = ?;", [dataapp_id]);


def _clear_all_dataapps(conn: Connection):
    conn.execute("DELETE FROM dataapps;")


def _get_dataapp_principals(dataapp_id: int, conn: Connection) -> List[PrincipalId]:
    conn.execute("SELECT scope, id FROM principals where id = ?;", [dataapp_id])
    records = conn.fetch_all()
    return [PrincipalId(scope=str(r[0]), id=str(r[1])) for r in records]


class DataAppsRepo(IDataAppsRepo):

    def create(self, details: DataAppAttributes) -> Optional[DataAppProfile]:
        with transaction() as conn:
            # dataapp_id = _next_id(conn)
            dataapp_id = details.name
            _insert_dataapp(dataapp_id, details, conn)
            return _load_dataapp_by_id(dataapp_id, conn)

    def load_by_id(self, dataapp_id: int) -> Optional[DataAppProfile]:
        with connect() as conn:
            return _load_dataapp_by_id(dataapp_id, conn)

    def load_by_name(self, dataapp_name: str) -> Optional[DataAppProfile]:
        with connect() as conn:
            return _load_dataapp_by_name(dataapp_name, conn)

    def load_by_principal(self, principal: PrincipalId) -> Optional[DataAppProfile]:
        pass

    def delete_by_name(self, dataapp_name: str):
        pass

    def delete_by_id(self, dataapp_id: int):
        with transaction() as conn:
            # _delete_all_principals_for_dataapp(dataapp_id, conn)
            _delete_dataapp(dataapp_id, conn)

    def load_all(self,
                 attributes: Set[DataAppField],
                 skip: Optional[int],
                 sort_by: Optional[List[Tuple[DataAppField, bool]]],
                 limit: Optional[int]) -> List[DataAppProfile]:
        with connect() as conn:
            return _load_all(attributes, sort_by, skip, limit, conn)

    def delete_all(self):
        with transaction() as conn:
            # _clear_all_principals(conn)
            _clear_all_dataapps(conn)
