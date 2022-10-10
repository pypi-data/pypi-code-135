"""
Scripts to drop data.
"""
import mariadb
from rich import print as rprint

from sensamag_utility import connection_manager


def drop_text_table(conn: mariadb.Connection) -> None:
    """
    Drop TextReferences and TextContents table from Database.
    :param conn: connection object
    """
    rprint("> Dropping textcontents and textreferences tables!")
    cur = conn.cursor()
    try:
        cur.execute("DROP TABLE textcontents")
        cur.execute("DROP TABLE textreferences")
        conn.commit()
        rprint(
            f"> [bold green]Dropping successfully [yellow]{cur.affected_rows}[/yellow] rows."
        )
    except mariadb.Error as exception:
        raise Exception("> Error dropping tables!") from exception


def delete_text_table(conn: mariadb.Connection) -> None:
    """
    DELETE all rows in TextReferences and TextContents but keep tables.
    :param conn: connection object
    """
    rprint("> Deleting all rows in textcontents and textreferences tables!")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM textcontents")
        cur.execute("ALTER TABLE textcontents AUTO_INCREMENT = 1")
        cur.execute("DELETE FROM textreferences")
        cur.execute("ALTER TABLE textreferences AUTO_INCREMENT = 1")
        conn.commit()
        rprint(
            f"> [bold green]Deleting successfully [yellow]{cur.affected_rows}[/yellow] rows."
        )
    except mariadb.Error as exception:
        raise Exception("> Error deleting tables!") from exception
