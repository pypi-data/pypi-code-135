from a_pandas_ex_df_to_string import ds_to_string
from pandas.core.base import PandasObject
import pandas as pd


def ds_drop_duplicates_without_pain(df, subset=None, keep="first", ignore_index=False):
    df2 = ds_to_string(df)
    if not isinstance(df, pd.Series):
        df22 = df2.drop_duplicates(
            subset=subset, keep=keep, inplace=False, ignore_index=ignore_index
        )
    else:
        df22 = df2.drop_duplicates(keep=keep, inplace=False)
    return df.loc[df22.index].copy()


def pd_add_drop_duplicates_without_pain():
    PandasObject.ds_drop_duplicates_without_pain = ds_drop_duplicates_without_pain
