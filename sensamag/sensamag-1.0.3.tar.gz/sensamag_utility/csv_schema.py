"""
CSV schema for typification.
"""
from enum import Enum

from rich import print as rprint
from rich.table import Table


class CSVSchema(Enum):
    """
    This is a CSV schema, values are column names in CSV file.
    """

    REFERENCE_NAME = "Reference"
    CONTENT_TEXT = "Content"
    LANGUAGE_NAME = "Language"
    REFERENCE_ID = "ReferenceId"
    CONTENT_ID = "ContentId"
    LANGUAGE_ID = "LanguageId"

    @staticmethod
    def print_schema() -> None:
        """
        Print CSV schema to console.
        """
        table = Table("Field", "CSV Column", title="CSV Schema")
        for field in CSVSchema:
            table.add_row(field.name, field.value)

        rprint(table)
