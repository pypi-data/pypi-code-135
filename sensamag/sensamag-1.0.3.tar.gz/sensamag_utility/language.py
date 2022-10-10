"""
Scripts to manipulate Language DataTable.
"""
import mariadb
from rich import print as rprint

from sensamag_utility.utility import print_as_table


def list_languages(conn: mariadb.Connection) -> None:
    """
    Print a list of languages to console.
    :param conn: connection object.
    """
    rprint("> Fetching languages table")
    cur = conn.cursor()
    try:
        cur.execute(
            """
        SELECT * FROM localizationlanguages
        """
        )
        print_as_table(cur, name="localizationlanguages")
        rprint(f"> [bold green]Fetched: {cur.affected_rows} rows")
    except mariadb.Error as exception:
        raise Exception("Error fetching languages!") from exception


def add_language(
    conn: mariadb.Connection, name: str, culture: str, priority: int
) -> None:
    """
    Add new language to the database.
    :param conn: connection object.
    :param name: name of the new language.
    :param culture: culture of the new language.
    :param priority: priority of the new language.
    """
    rprint(
        f"""
    > Adding new language:
    | > name: {name}
    | > culture: {culture}
    | > priority: {priority}
    """
    )
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO localizationlanguages (Name,Culture, Priority) VALUES (?, ?, ?)",
            (name, culture, priority),
        )
        conn.commit()
        rprint(
            f"> [bold green]Language {name} is added successfully with {cur.lastrowid} id"
        )
    except mariadb.Error as exception:
        raise Exception(
            f"Error adding new language with name: "
            f"{name}, culture: {culture}, priority: {priority}"
        ) from exception


def remove_language(conn: mariadb.Connection, lang_id: int) -> None:
    """
    Remove language from DB.
    :param conn: connection object.
    :param lang_id: id of the lang to remove.
    """
    rprint(f"> Removing language by id: {lang_id}")
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM localizationlanguages WHERE Id = (?)", (lang_id,))
        conn.commit()
        rprint(f"> [bold green]Language with id: {lang_id} is removed successfully!")
    except mariadb.Error as exception:
        raise Exception(f"Error removing language with id: {lang_id}") from exception
