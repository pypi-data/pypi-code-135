from django.db.transaction import get_connection
from contextlib import ContextDecorator


class NoExtraQueryException(Exception):
    """Raise to prevent ORM to perform extra lazy queries."""

    # Allowing ORM to perform object-related extra queries can easily increase the number of DB
    # queries exponentially and also causes issues with asyncio


class FakeCursor:
    """Cursor that raises exception on any attempt of query."""

    def _do_not_execute(self, *args, **kwargs):
        raise NoExtraQueryException(f"Prevented execution of query: {args[0]}")

    def executemany(self, *args, **kwargs):
        self._do_not_execute(*args, **kwargs)

    def execute(self, *args, **kwargs):
        self._do_not_execute(*args, **kwargs)

    def close(self, *args, **kwargs):
        pass


class BlockExtraQueries(ContextDecorator):
    def __init__(self):
        self.original = None

    def stop_cursor(*args, **kwargs):
        return FakeCursor()

    def __enter__(self):
        connection = get_connection()
        self.original = connection.cursor
        setattr(connection, "cursor", self.stop_cursor)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        connection = get_connection()
        setattr(connection, "cursor", self.original)


block_extra_queries = BlockExtraQueries()
