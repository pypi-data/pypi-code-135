import pandas as pd
from pathlib import Path
from datetime import datetime
from typing import Union
from .exceptions import SetupError, MissingColumn


class Lookup:
    def __init__(
        self,
        dataset: Union[str, pd.DataFrame, Path] = None,
        term_1_column: str = "Term 1",
        term_2_column: str = "Term 2",
        start_date_column: Union[str, dict] = "Start Date",
        end_date_column: Union[str, dict] = "End Date",
    ):
        if (
            not isinstance(dataset, str)
            and not isinstance(dataset, pd.DataFrame)
            and not isinstance(dataset, Path)
        ):
            raise SetupError(
                "You need to specify a `dataset` as a path (str or Path) to a file readable as a Pandas DataFrame, or a Pandas DataFrame."
            )

        if not isinstance(term_1_column, str):
            raise SetupError("Term 1 column name needs to be passed as a string.")

        if not isinstance(term_2_column, str):
            raise SetupError("Term 2 column name needs to be passed as a string.")

        self.term_1_column = term_1_column
        self.term_2_column = term_2_column

        if not isinstance(start_date_column, str) and not isinstance(
            start_date_column, dict
        ):
            raise SetupError(
                "Start Date column name needs to be passed as a string or a dict following structure {year_column_name: year_format_str, month_column_name: month_format_str, day_column_name: day_format_str,}."
            )

        if not isinstance(end_date_column, str) and not isinstance(
            end_date_column, dict
        ):
            raise SetupError(
                "End Date column name needs to be passed as a string or a dict following structure {year_column_name: year_format_str, month_column_name: month_format_str, day_column_name: day_format_str,}."
            )

        if isinstance(dataset, str) or isinstance(dataset, Path):
            self.data = pd.read_csv(dataset)
        else:
            self.data = dataset

        if (
            isinstance(start_date_column, str)
            and not start_date_column in self.data.columns
        ):
            raise MissingColumn(
                f"Start Date column ('{start_date_column}') does not exist in dataset."
            )

        if (
            isinstance(end_date_column, str)
            and not end_date_column in self.data.columns
        ):
            raise MissingColumn(
                f"End Date column ('{end_date_column}') does not exist in dataset."
            )

        if isinstance(start_date_column, str):
            self.data[start_date_column] = pd.to_datetime(self.data[start_date_column])
        elif isinstance(start_date_column, dict):
            year, month, day = start_date_column.items()
            start_date_column = "Start Date"
            self.data[start_date_column] = self.data.apply(
                lambda row: self._get_date(row, year, month, day), axis=1
            )
            self.data.drop([year[0], month[0], day[0]], axis=1, inplace=True)
        else:
            # This should never happen since we check above for str or dict type for start_date_column
            pass

        if isinstance(end_date_column, str):
            self.data[end_date_column] = pd.to_datetime(self.data[end_date_column])
        elif isinstance(end_date_column, dict):
            year, month, day = end_date_column.items()
            end_date_column = "End Date"
            self.data[end_date_column] = self.data.apply(
                lambda row: self._get_date(row, year, month, day), axis=1
            )
            self.data.drop([year[0], month[0], day[0]], axis=1, inplace=True)
        else:
            # This should never happen since we check above for str or dict type for start_date_column
            pass

        if isinstance(end_date_column, str):
            self.data[end_date_column] = pd.to_datetime(self.data[end_date_column])
        elif isinstance(end_date_column, dict):
            year_column, month_column, day_column = end_date_column
        else:
            pass  # This should never happen since we check above for str or dict type for end_date_column

        self.start_date_column = start_date_column
        self.end_date_column = end_date_column

    def left_translate(self, term_1: str, date: Union[str, pd.Timestamp]) -> list:
        date = self._correct_date(date, "left_translate")

        return self.data[
            (self.data[self.start_date_column] <= date)
            & (self.data[self.end_date_column] >= date)
            & (self.data[self.term_1_column] == term_1)
        ][self.term_2_column].to_list()

    def right_translate(self, term_2: str, date: Union[str, pd.Timestamp]) -> list:
        date = self._correct_date(date, "right_translate")

        return self.data[
            (self.data[self.start_date_column] <= date)
            & (self.data[self.end_date_column] >= date)
            & (self.data[self.term_2_column] == term_2)
        ][self.term_1_column].to_list()

    @staticmethod
    def _get_date(row: pd.Series, year: tuple, month: tuple, day: tuple) -> datetime:
        def clean(string):
            return string.replace(".", "").strip()

        year_column, year_format = year
        month_column, month_format = month
        day_column, day_format = day
        return datetime.strptime(
            f"{row[year_column]} {clean(row[month_column])} {row[day_column]}",
            f"{year_format} {month_format} {day_format}",
        )

    @staticmethod
    def _correct_date(date: Union[str, pd.Timestamp], func: str = None) -> pd.Timestamp:
        if isinstance(date, str):
            date = pd.Timestamp.fromisoformat(date)
        elif isinstance(date, pd.Timestamp):
            pass
        else:
            raise SetupError(
                f"Date passed to {func} must be a string or a Pandas Timestamp object."
            )

        return date
