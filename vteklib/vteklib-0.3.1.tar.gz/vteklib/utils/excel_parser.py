import json

import numpy as np
import pandas
import pandas as pd
from collections import namedtuple
from functools import lru_cache


class ExcelFile:
    def __init__(self, excel_fp: str):
        self.df: pd.DataFrame = pandas.read_excel(excel_fp)
        self.all_series: list[DataSeries] = []

    def get_series(self):
        for col in self.df.columns:
            series_in_row: list[DataSeries] = []
            for i in self.df[col]:
                if type(i) == str:
                    s = DataSeries()
                    series_in_row.append(s)
                    s.name = i
                    s.data = []
                elif not pd.isna(i) and type(i) != str:
                    if len(series_in_row):
                        series_in_row[-1].data.append(i)
                    else:
                        continue
            for series in series_in_row:
                if len(series.data):
                    self.all_series.append(series)
        return self.all_series

    def to_json(self):
        names = dict()
        res = dict()
        for s in self.get_series():
            if s.name not in names.keys():
                res[s.name] = s.data
                names[s.name] = 1
            else:
                res[f"{s.name}({names[s.name]})"] = s.data
                names[s.name] += 1
        return json.dumps(res, ensure_ascii=False)


class DataSeries:
    __slots__ = ('name', 'data')
    name: str
    data: list

    def __init__(self):
        pass

    def __str__(self):
        return f"{self.name} {self.data}"


@lru_cache(None)
def get_data(path: str):
    ef = ExcelFile(path)
    series = ef.to_json()
    return series
