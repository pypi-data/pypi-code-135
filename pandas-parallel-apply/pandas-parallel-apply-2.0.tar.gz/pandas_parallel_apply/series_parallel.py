"""
Apply on series
Usage:
    standard => series.apply(f)
    parallel => SeriesParallel(series, n_cores).apply(f)
             => SeriesParallel(df[col], n_cores).apply(f)
"""
from typing import Callable
import pandas as pd
from functools import partial

from .utils import parallelize_dataframe, get_default_n_cores


def apply_on_series(series: pd.Series, f: Callable, pbar: bool = True) -> pd.Series:
    if pbar:
        return series.progress_apply(f)
    else:
        return series.apply(f)


class SeriesParallel:
    def __init__(self, series: pd.Series, n_cores: int = None, pbar: bool = True):
        if n_cores is None:
            n_cores = get_default_n_cores()
        self.series = series
        self.n_cores = n_cores
        self.pbar = pbar
    
    def apply(self, func: Callable) -> pd.Series:
        return parallelize_dataframe(self.series, partial(apply_on_series, f=func, pbar=self.pbar), self.n_cores)
