"""General module for parallelizing a dataframe apply function on a column (series) or entire row"""

import logging
from typing import Callable, Union
import numpy as np
import pandas as pd
from tqdm import tqdm
from multiprocessing import cpu_count
from pathos.multiprocessing import ProcessingPool as Pool
import os
from .logger import logger
tqdm.pandas()


def parallelize_dataframe(df: Union[pd.DataFrame, pd.Series], func: Callable, n_cores: int) -> pd.DataFrame:
    """Function used to split a dataframe in n sub dataframes, based on the number of cores we want to use."""
    if n_cores == 0:
        return func(df)
    n_cores = min(cpu_count(), len(df), n_cores)
    logging.debug(f"Parallelizing apply on df (rows: {len(df)}) with {n_cores} cores")
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    pool_res = pool.map(func, df_split)
    df = pd.concat(pool_res)
    return df

def get_default_n_cores() -> int:
    """Gets the default N_CORES if set by the PANDAS_PARALLEL_APPLY_N_CORES env variable, else set to 0 (serial)"""
    if "PANDAS_PARALLEL_APPLY_N_CORES" in os.environ:
        n_cores = int(os.environ["PANDAS_PARALLEL_APPLY_N_CORES"])
        logger.debug(f"N cores was set from the 'PANDAS_PARALLEL_APPLY_N_CORES' env variable to {n_cores}")
    else:
        n_cores = 0
        logger.debug(f"No 'PANDAS_PARALLEL_APPLY_N_CORES' env variable. Defaulting n_cores to 0 (serial)")
    assert isinstance(n_cores, int) and n_cores >= 0
    return n_cores
