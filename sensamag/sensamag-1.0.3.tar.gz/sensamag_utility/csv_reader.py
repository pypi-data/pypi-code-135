"""
Scripts to read a file as CSV file.
"""
import csv
import os


def read_data(path: str) -> list:
    """
    Read file as CSV and return list of rows.
    :param path: path to file to read.
    :return: rows from the file as list.
    """
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            # skip empty lines
            if not row[reader.fieldnames[0]]:
                continue
            data.append(row)
        return data


def write_data(path: str, data, columns) -> None:
    """
    Write data to file.
    :param path: path to new file.
    :param data: data to write.
    :param columns: column names for csv header.
    """
    if os.path.isdir(path):
        path = os.path.join(path, "data.csv")
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
