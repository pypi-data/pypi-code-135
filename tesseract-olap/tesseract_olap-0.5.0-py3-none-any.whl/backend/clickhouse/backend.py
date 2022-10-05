import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator, AsyncIterator, Type, TypeVar, Union

import asynch
from asynch.cursors import Cursor, DictCursor
from asynch.errors import ClickHouseException

from tesseract_olap.backend import Backend
from tesseract_olap.backend.exceptions import UpstreamInternalError
from tesseract_olap.common import AnyDict
from tesseract_olap.query import DataQuery, MembersQuery
from tesseract_olap.query.exceptions import InvalidQuery
from tesseract_olap.schema import Schema

from .sqlbuild import dataquery_sql, membersquery_sql

logger = logging.getLogger("tesseract_olap.backend.clickhouse")

CursorType = TypeVar("CursorType", bound=Cursor)


class ClickhouseBackend(Backend):
    """Clickhouse Backend class

    This is the main implementation for Clickhouse of the core :class:`Backend`
    class.

    Must be initialized with a connection string with the parameters for the
    Clickhouse database. Then must be connected before used to execute queries,
    and must be closed after finishing use.
    """

    connection_string: str
    pool: Union[asynch.pool.Pool, None]

    def __init__(self, connection_string: str) -> None:
        self.connection_string = connection_string

    def __repr__(self) -> str:
        return f"ClickhouseBackend('{self.connection_string}')"

    async def connect(self, **kwargs) -> asynch.pool.Pool:
        pool = getattr(self, "pool", None)
        if pool is None:
            pool = await asynch.create_pool(dsn=self.connection_string)
        self.pool = pool
        return pool

    @asynccontextmanager
    async def acquire(
        self, curcls: Type[CursorType] = Cursor
    ) -> AsyncGenerator[CursorType, None]:
        pool = await self.connect()
        try:
            async with pool.acquire() as conn:
                async with conn.cursor(cursor=curcls) as cursor:
                    yield cursor
        except ClickHouseException as exc:
            raise UpstreamInternalError(str(exc)) from None

    def close(self):
        pool = getattr(self, "pool", None)
        if pool is not None:
            pool.close()

    async def wait_closed(self):
        pool = getattr(self, "pool", None)
        if pool is not None:
            await pool.wait_closed()

    async def execute(
        self, query: Union["DataQuery", "MembersQuery"], **kwargs
    ) -> AsyncIterator[AnyDict]:
        """
        Processes the requests in a :class:`DataQuery` or :class:`MembersQuery`
        instance, sends the query to the database, and returns an `AsyncIterator`
        to access the rows.
        Each iteration yields a tuple of the same length, where the first tuple
        defines the column names, and the subsequents are rows with the data in
        the same order as each column.
        """
        logger.debug("Execute query", extra={"query": query})

        if isinstance(query, MembersQuery):
            sql_builder, sql_params = membersquery_sql(query)
        elif isinstance(query, DataQuery):
            sql_builder, sql_params = dataquery_sql(query)
        else:
            raise InvalidQuery(
                "ClickhouseBackend only supports DataQuery and MembersQuery instances"
            )

        async with self.acquire(DictCursor) as cursor:
            # AsyncIterator must be fully consumed before returning because
            # async context closes connection prematurely
            await cursor.execute(query=sql_builder.get_sql(), args=sql_params)
            result = cursor.fetchall()
            for row in result:
                yield row

    async def ping(self) -> bool:
        """Checks if the current connection is working correctly."""
        async with self.acquire() as cursor:
            await cursor.execute("SELECT 1")
            result = cursor.fetchone()
            return result == (1,)

    async def validate_schema(self, schema: "Schema") -> None:
        """Checks all the tables and columns referenced in the schema exist in
        the backend.
        """
        # logger.debug("Schema %s", schema)
        # TODO: implement
        for cube in schema.cube_map.values():
            pass
        return None
