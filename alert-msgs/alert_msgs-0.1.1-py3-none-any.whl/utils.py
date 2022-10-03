import sys
from typing import Sequence

from .components import Table
from .settings import logger


def use_inline_tables(tables: Sequence[Table], inline_tables_max_rows: int) -> bool:
    """Check if tables are small enough to be displayed inline in the message.

    Args:
        tables (Sequence[Table]): All tables that are to be included in the message.
        inline_tables_max_rows (int): Max number of table rows that can be used in the message.

    Returns:
        bool: Whether inline tables should be used.
    """
    if sum([len(t.content) for t in tables]) < inline_tables_max_rows:
        return True
    return False


def attach_tables(tables: Sequence[Table], attachments_max_size_mb: int) -> bool:
    """Check if tables are small enough to be attached as files.

    Args:
        tables (Sequence[Table]): The tables that should be attached as files.
        attachments_max_size_mb (int): Max total size of all attachment files.

    Returns:
        bool: Whether files can should be attached.
    """
    tables_size_mb = sum([sys.getsizeof(t.content) for t in tables]) / 10**6
    if tables_size_mb < attachments_max_size_mb:
        logger.debug(f"Adding {len(tables)} tables as attachments.")
        return True
    else:
        logger.debug(
            f"Can not add tables as attachments because size {tables_size_mb}mb exceeds max {attachments_max_size_mb}"
        )
        return False



