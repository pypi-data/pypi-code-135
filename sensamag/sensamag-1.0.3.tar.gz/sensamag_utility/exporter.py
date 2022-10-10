"""
Scripts to export data from database to CSV file.
"""
import mariadb
from rich import print as rprint

from sensamag_utility.csv_reader import write_data
from sensamag_utility.csv_schema import CSVSchema as Schema


def export_db(conn: mariadb.Connection, path: str) -> None:
    """
    Export database text data to *.csv file.
    :param conn: connection object.
    :param path: path to *.csv file to create.
    """
    rprint(f"> Exporting data to: {path}")
    cur = conn.cursor(dictionary=True)
    try:
        cur.execute(
            f"""
        SELECT textreferences.Name AS {Schema.REFERENCE_NAME.value},
            textcontents.Text AS {Schema.CONTENT_TEXT.value},
            localizationlanguages.Name AS {Schema.LANGUAGE_NAME.value},
            textcontents.TextReferences_Id AS {Schema.REFERENCE_ID.value},
            textcontents.Id AS {Schema.CONTENT_ID.value},
            textcontents.Language_Id AS {Schema.LANGUAGE_ID.value}
        FROM textcontents INNER JOIN (localizationlanguages, textreferences)
            ON textcontents.Language_Id = localizationlanguages.Id
            AND textcontents.TextReferences_Id = textreferences.Id
        """
        )
        headers = [row[0] for row in cur.description]
        write_data(path, cur, headers)
        rprint(
            f"> [bold green]Successfully written "
            f"[yellow]{cur.affected_rows}[/] rows to [yellow]{path}[/]! "
        )
    except mariadb.Error as exception:
        raise Exception("Error exporting data!") from exception
