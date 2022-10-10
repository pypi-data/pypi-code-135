"""
Scripts to import data from csv to database.
"""
import csv
import os.path

import mariadb
from rich import print as rprint

from sensamag_utility.csv_schema import CSVSchema


def import_csv_to_db(conn: mariadb.Connection, path: str):
    """
    Import provided .csv file to sensamag DB.

    Parameters:
        conn(mariadb.Connection): Connection to mariadb database.
        path(str): Path to .csv file to import.
    """
    if os.path.isdir(path):
        path = os.path.join(path, "data.csv")
    try:
        rprint(f"> Importing: {path}")
        with open(path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rprint(f"> File loaded from {path}")
            if not all(field.value in reader.fieldnames for field in CSVSchema):
                raise Exception(
                    "Not all fields are present in the CSV file. "
                    'Run "sensamag csvschema" to see column names.'
                )
            cur = conn.cursor(named_tuple=True)
            for row in reader:
                try:
                    __parse_row(cur, row)
                except Exception as exception:
                    raise Exception(
                        f"> [bold red] Error parsing row:[/] {row}"
                    ) from exception
            conn.commit()
            rprint(
                f"> [bold green]Successfully imported [yellow]{reader.line_num}[/] rows!"
            )
    except Exception as exception:
        raise Exception(f"Error importing .csv from {path}") from exception


def __parse_row(cur: mariadb.Cursor, row: dict) -> None:
    """
    Execute SQL statement and add csv row to database.
    :param cur: cursor from connection object.
    :param row: row with data from csv file.
    """
    ref_name = row[CSVSchema.REFERENCE_NAME.value].strip()
    ref_id = row[CSVSchema.REFERENCE_ID.value].strip()
    cont_text = row[CSVSchema.CONTENT_TEXT.value]
    cont_id = row[CSVSchema.CONTENT_ID.value].strip()
    lang_name = row[CSVSchema.LANGUAGE_NAME.value].strip()
    lang_id = row[CSVSchema.LANGUAGE_ID.value].strip()

    # 1) Text Reference:
    # If id and name provided -> Update ref name
    if ref_id and ref_name:
        cur.execute(
            "UPDATE textreferences SET Name = ? WHERE Id = ?", (ref_name, ref_id)
        )
    # if only id provided -> read existing reference from database
    elif ref_id:
        cur.execute("SELECT Id, Name FROM textreferences WHERE Id = ?", (ref_id,))
        ref_name = cur.next()[1]
    # if only name provided -> create new reference
    elif ref_name:
        # Check if name already in database
        cur.execute("SELECT Id, Name FROM textreferences WHERE Name = ?", (ref_name,))
        check_result = cur.next()
        if check_result:
            ref_id = check_result[0]
        # If name is new then create new reference
        else:
            cur.execute("INSERT INTO textreferences (Name) VALUES (?)", (ref_name,))
            ref_id = cur.lastrowid

    # 2) Language
    # Verify language name and id
    if lang_id and lang_name:
        cur.execute(
            "SELECT Id, Name FROM localizationlanguages WHERE Id = ?", (lang_id,)
        )
        lang_db = cur.next()[1]
        if lang_name.casefold() != lang_db.casefold():
            raise ValueError(
                "Language name from CSV do not match ones in DB!"
                f"\n For id: {lang_id}. Language from csv: "
                f"{lang_name}, language from db: {lang_db}"
            )
    # If language name provided but not ID -> get ID from DB
    elif lang_name and not lang_id:
        cur.execute(
            "SELECT Id, Name FROM localizationlanguages WHERE Name = ?", (lang_name,)
        )
        result = cur.next()
        lang_id = result[0] if result else None

    # 3) Text Content
    # If id provided -> update existing content entry
    if cont_id:
        # Search existing by id
        cur.execute(
            "SELECT Id, Text, TextReferences_Id, Language_Id "
            "FROM textcontents WHERE Id = ?",
            (cont_id,),
        )
        content_result = cur.next()
        # Exception on search by id failed
        if not content_result:
            raise Exception(f"Could not find text content by Id: {cont_id}!")
        # Update content_id with data from CSV
        cur.execute(
            "UPDATE textcontents SET Text = ?, TextReferences_Id = ?, Language_Id = ? "
            "WHERE Id = ?",
            (
                cont_text if cont_text else content_result[1],
                ref_id if ref_id else content_result[2],
                lang_id if lang_id else content_result[3],
                cont_id,
            ),
        )
    # If text provided but not id -> create new content entry with provided text
    elif cont_text:
        if not lang_id or not ref_id:
            raise Exception(
                f"To create new text content entry - "
                f"lang_id and ref_id must be provided!"
                f"\nProvided: lang_id: {lang_id}, ref_id: {ref_id}."
            )
        cur.execute(
            "INSERT INTO textcontents (name, text, TextReferences_Id, Language_Id) "
            "VALUES (?, ?, ?, ?)",
            (ref_name, cont_text, ref_id, lang_id),
        )
