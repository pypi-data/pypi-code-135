"""_summary_
"""

import pandas as pd
from iopatent.exceptions import CsvReadError, CsvWriteError


def read_csv(*args, **kwargs) -> pd.DataFrame:
    """_summary_

    Returns:
        pd.DataFrame: _description_
    """
    try:
        return pd.read_csv(*args, **kwargs)
    except Exception as e:
        raise CsvReadError('Unable to read csv file') from e


def to_csv(df, *args, **kwargs) -> None:
    """_summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        return df.to_csv(*args, **kwargs)
    except Exception as e:
        raise CsvWriteError('Unable to save csv file') from e