"""
Package with CLI entry points.
"""
import typer
from typer import Typer

from sensamag_utility import exporter, language
from sensamag_utility.connection_manager import ConnectionManager
from sensamag_utility.csv_schema import CSVSchema
from sensamag_utility.drop_table import delete_text_table, drop_text_table
from sensamag_utility.importer import import_csv_to_db

app = Typer(no_args_is_help=True)
connection_manager = ConnectionManager()


@app.callback(invoke_without_command=True)
def connection(
    user: str = None,
    password: str = None,
    host: str = None,
    port: int = None,
    database: str = None,
) -> None:
    """
    Override default connection params.
    :param user: MariaDB username.
    :param password: password.
    :param host: ip address of MariaDB server.
    :param port: port of MariaDB server.
    :param database: name of the database to connect.
    """
    connection_manager.set_connection(user, password, host, port, database)


@app.command()
def importdb(path: str = typer.Option(..., prompt=True)) -> None:
    """
    Import *.CSV file to MariaDB.
    :param path: path to *.csv file or folder with data.csv
    """
    with connection_manager.get_connection() as conn:
        import_csv_to_db(conn, path)


@app.command()
def addlang(
    name: str = typer.Option(..., prompt=True),
    culture: str = typer.Option(..., prompt=True),
    priority: int = typer.Option(..., prompt=True),
) -> None:
    """
    Add new language to MariaDB.
    :param name: name of new language (example: German)
    :param culture: culture name of new language (example: de-DE)
    :param priority: priority of new language (example: 5)
    """
    with connection_manager.get_connection() as conn:
        language.add_language(conn, name, culture, priority)


@app.command()
def exportdb(path: str = typer.Option(..., prompt=True)) -> None:
    """
    Export text data from MariaDB to data.csv file.
    :param path: path to *.csv or folder.
    """
    with connection_manager.get_connection() as conn:
        exporter.export_db(conn, path)


@app.command()
def droptables() -> None:
    """
    Drop "Text References" and "Text Contents" DataTables in MariaDB.
    """
    with connection_manager.get_connection() as conn:
        drop_text_table(conn)


@app.command()
def deletetables() -> None:
    """
    Delete all rows in "Text References" and "Text Contents" but keep tables.
    """
    with connection_manager.get_connection() as conn:
        delete_text_table(conn)


@app.command()
def removelang(langid: int = typer.Option(..., prompt=True)) -> None:
    """
    Remove language from MariaDB table.
    :param langid: ID of language to remove.
    """
    with connection_manager.get_connection() as conn:
        language.remove_language(conn, langid)


@app.command()
def listlang() -> None:
    """
    Print to console a list of languages in MariaDB table.
    """
    with connection_manager.get_connection() as conn:
        language.list_languages(conn)


@app.command()
def csvschema() -> None:
    """
    Print default csv column names.
    """
    CSVSchema.print_schema()
