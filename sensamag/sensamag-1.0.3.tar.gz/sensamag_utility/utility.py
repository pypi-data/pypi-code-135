"""
Basic utility package.
"""
from mariadb import Cursor
from rich import print as rprint
from rich.table import Table


def print_as_table(cur: Cursor, name: str = "Result") -> None:
    """
    Print result to console as table.
    :param cur: cursor from mariadb connection object.
    :param name: name of the table to print.
    """
    # Get column names from cursor
    table = Table(*[row[0] for row in cur.description], title=name)
    for row in cur:
        table.add_row(*[str(ele) for ele in row])
    rprint(table)
