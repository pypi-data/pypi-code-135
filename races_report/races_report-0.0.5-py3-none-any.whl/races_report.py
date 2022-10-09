import os
from datetime import datetime, timedelta
from functools import total_ordering
from typing import List, Dict
from dataclasses import dataclass

from prettytable import PrettyTable

from races_report.custom_exceptions import OpenFileException, DriverNotFound


@total_ordering
@dataclass
class Driver:
    abbr: str
    name: str
    company: str
    start_time: datetime = None
    end_time: datetime = None
    rank: int = None

    @property
    def lap_time(self) -> timedelta:
        """
        Returns the lap time
        :return:
        """
        result_time = None
        if self.start_time and self.end_time and self.end_time > self.start_time:
            result_time = self.end_time - self.start_time
        return result_time

    def __lt__(self, other) -> bool:
        if self.lap_time:
            if other.lap_time:
                return self.lap_time < other.lap_time
            return True
        else:
            return False

    @property
    def dtime(self) -> str:
        lap_time_str = 'error' if self.lap_time is None else str(self.lap_time)[:-3]
        return lap_time_str


class Data:
    def __init__(self, path: str):
        """
        Constructor accepts command line arguments
        :param path:
        """
        self.path = path

    def _open_file(self, file_name: str) -> List[str]:
        """
        Open a file and return its contents as text
        :param file_name: file name to open
        :return: string
        """
        try:
            with open(os.path.join(self.path, file_name), 'r', encoding='UTF-8') as f:
                return f.read().strip().split("\n")
        except IOError as err:
            raise OpenFileException(f'{err.args[1]}')

    def _parse_logs(self, file_name: str) -> Dict[str, datetime]:
        """
        Parses information from files about the start and finish of the race into dictionaries
        :param file_name: file name with information about the start and finish times of the race
        :return: dict
        """
        file = self._open_file(file_name)
        return {row[:3]: datetime.strptime(row.rstrip()[3:], "%Y-%m-%d_%H:%M:%S.%f") for row in file}

    def _parse_abbr(self, file_name: str) -> Dict[str, List[str]]:
        """
        Parses information from a file about drivers and commands into a list of lists
        :param file_name: name of the file with information about the drivers of the race
        :return: Driver
        """
        file = self._open_file(file_name)
        return {row[:3]: row.rstrip().split('_') for row in file}

    def load(self) -> List[Driver]:
        """
        Create the list with result of the race for each driver
        :return: List[List[str]]
        """
        drivers: dict = self._parse_abbr('abbreviations.txt')
        start: dict = self._parse_logs('start.log')
        end: dict = self._parse_logs('end.log')
        full_list = []
        for abbr in drivers:
            full_list.append(Driver(*drivers[abbr], start.get(abbr), end.get(abbr)))
        return full_list


class Report:
    """class Report is designed to generate a races_report on the results of the preliminary races of Formula 1"""

    def __init__(self, path: str, driver: str, ordering: str):
        """
        Constructor accepts command line arguments
        :param like this 'report/results', 'Fernando Alonso', desc
        """
        self.path = path
        self.driver = driver
        self.desc_ordering = ordering == 'desc'

    @staticmethod
    def _sort_list(unsorted_list: List[Driver]) -> List[Driver]:
        """
        Sorts in ascending order all results and add drivers ranking
        :unsorted_list: list prepared for sorting
        :return: List[Driver]
        """
        sorted_list = sorted(unsorted_list)
        for idx, record in enumerate(sorted_list, 1):
            record.rank = idx
        return sorted_list

    def _get_driver_report(self, full_dict: Dict[str, Driver]) -> PrettyTable:
        """
        Returns a report with the result of a specific driver
        :param full_dict: dict with results of all drivers
        :return: PrettyTable
        """
        driver_info = full_dict.get(self.driver)
        if driver_info:
            row = [driver_info.rank, driver_info.name, driver_info.company, driver_info.dtime]
        else:
            raise DriverNotFound(f'{self.driver} not found.')
        table = _create_table([row])
        return table

    @staticmethod
    def _get_report(good_list: List[Driver], error_list: List[Driver]) -> PrettyTable:
        """
        Returns a report with the results of all drivers
        :param good_list: top 15 results
        :param error_list: other results
        :return: PrettyTable
        """
        rows = [[record.rank, record.name, record.company, record.dtime] for record in good_list]
        good_list.extend(error_list)
        rows.append(_create_empty_line(good_list))
        err_rows = [[record.rank, record.name, record.company, record.dtime] for record in error_list]
        rows.extend(err_rows)
        table = _create_table(rows)
        return table

    def build_report(self) -> PrettyTable:
        """
        Builds a races_report depending on the command line arguments
        :return: PrettyTable
        """
        data = Data(self.path).load()
        sorted_list = self._sort_list(data)
        good_list = [row for row in sorted_list if row.dtime != 'error']
        error_list = [row for row in sorted_list if row.dtime == 'error']
        length = len(good_list)
        good_list_15 = good_list[:15] if length > 15 else good_list
        error_list_15 = good_list[15:].extend(error_list) if length > 15 else error_list
        good_list_15.reverse() if self.desc_ordering else good_list_15

        if self.driver:
            full_dict = {record.name: record for record in sorted_list}
            report = self._get_driver_report(full_dict)
        else:
            report = self._get_report(good_list_15, error_list_15)
        return report


def _create_empty_line(index_list: List[Driver]) -> List[str]:
    """
    Returns a list-formatted string representing a horizontal line in a table
    :param index_list: list ready for output as a table
    :return: like this [ '--', '-----------', '-------------', '--------']
    """
    line_record = ['--']
    for column_name in ('name', 'company'):
        column_len = max(map(lambda row: len(getattr(row, column_name)), index_list))
        line_record.append('-' * column_len)
    line_record.append('--------------')
    return line_record


def _create_table(sorted_index_list: List[List[str]]) -> PrettyTable:
    """
    Generates a report in the form of a table
    :param sorted_index_list: list ready for output as a table
    :return: PrettyTable
    """
    table = PrettyTable()
    table.field_names = ["rank", "name", "company", "time"]
    for record in sorted_index_list:
        table.add_row(record)
    return table
