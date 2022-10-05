from typing import Union

import pandas as pd

from a_pandas_ex_plode_tool import (
    explode_lists_and_tuples_in_column,
    qq_ds_merge_multiple_dfs_and_series_on_index,
)
from pandas.core.base import PandasObject
from a_pandas_ex_df_to_string import ds_to_string


try:
    from rapidfuzz import fuzz, process
except Exception:
    from fuzzywuzzy import fuzz, process


def compare_values_in_column_against_list(
    df: [pd.Series],
    list_to_compare: list[str],
    limit: int = 5,
    merge_with_series: bool = True,
    partial_full_weighted: str = "weighted",
) -> pd.DataFrame:
    """
    df111 = df.Name.s_fuzz_from_list(
        list_to_compare=["Johannes", "Paulo", "Kevin"],
        limit=2,
        merge_with_series=True,
        partial_full_weighted="partial",
    )
    df222 = df.Name.s_fuzz_from_list(
        list_to_compare=["John", "Johannes", "Paulo", "Kevin"],
        limit=3,
        merge_with_series=False,
        partial_full_weighted="full",
    )
    df333 = df.Name.s_fuzz_from_list(
        list_to_compare=["Maria", "Anna"],
        limit=1,
        merge_with_series=False,
        partial_full_weighted="partial",
    )
    df333
            fuzz_string_0 fuzz_match_0 fuzz_index_0
    0           Maria         60.0            0
    1           Maria    44.444444            0
    2            Anna         75.0            1
    3           Maria         40.0            0
    4           Maria         40.0            0
    ..            ...          ...          ...
    886         Maria         40.0            0
    887         Maria         80.0            0
    888         Maria         60.0            0
    889         Maria         40.0            0
    890         Maria         60.0            0
    [891 rows x 3 columns]

        Parameters:
            df: [pd.Series]
            list_to_compare: list
                The strings you want to be compared
            limit: int
                How many results do you want to have?
                Each result will have 3 columns [string, match, position in column]
                (default=5)
            partial_full_weighted: str
                weighted = fuzz.WRatio
                full = fuzz.ratio
                partial = fuzz.partial_ratio
                (default="weighted")
            merge_with_series: str
                (default=True)
        Returns:
            pd.DataFrame
    """
    algor = get_algor(partial_full_weighted)

    tmpcolumn = "TEEEEEEEEEEEEEEEEEEEMMMMP______________"
    df_ = df.copy()
    df_ = df_.to_frame().copy()
    column = df_.columns[0]
    df_[tmpcolumn] = df_.index.copy()
    df_ = df_.reset_index(drop=True)
    df_col_as_string = ds_to_string(df_[column]).to_frame()
    dframe = explode_lists_and_tuples_in_column(
        df_col_as_string[column].apply(
            lambda x: process.extract(x, list_to_compare, scorer=algor, limit=limit)
        )
    )
    goodresults = []
    for ini, col in enumerate(dframe):
        r1 = explode_lists_and_tuples_in_column(dframe[col])
        r1.columns = [f"fuzz_string_{ini}", f"fuzz_match_{ini}", f"fuzz_index_{ini}"]
        goodresults.append(r1.copy())

    if merge_with_series:
        df_ = qq_ds_merge_multiple_dfs_and_series_on_index(df_, goodresults)
        df_.index = df_[tmpcolumn].__array__().copy()
        df_ = df_.drop(columns=[tmpcolumn])
    else:
        originalindex = df_[tmpcolumn].__array__().copy()
        df_ = qq_ds_merge_multiple_dfs_and_series_on_index(
            goodresults[0], (goodresults[1:])
        )
        df_.index = originalindex

    return df_


def compare_values_in_column_against_each_other(
    df: [pd.Series],
    limit: int = 5,
    merge_with_series: bool = True,
    partial_full_weighted="weighted",
) -> pd.DataFrame:
    """
    df11 = df.Name.s_fuzz_all_values_in_column(
        limit=5, merge_with_series=True, partial_full_weighted="weighted"
    )
    df22 = df.Name.s_fuzz_all_values_in_column(
        limit=2, merge_with_series=False, partial_full_weighted="full"
    )
    df33 = df.Name.s_fuzz_all_values_in_column(
        limit=1, merge_with_series=True, partial_full_weighted="partial"
    )

    df22

        0  Braund...     70.833333          477    Cann, ...     63.829787
    1  Angle,...     55.445545          518    Astor,...     53.061224
    2  Sinkko...     79.069767          747    Honkan...     77.272727
    3  Futrel...     77.142857          137    Potter...     52.873563
    4  Gilles...     84.615385          722    Saunde...     77.777778
    5  Bracke...     77.777778          221    Scanla...     76.470588
    6  O'Brie...     65.116279          552    Maisne...     58.536585
    7  Goodwi...     68.852459          386    Palsso...     67.857143
    8  Rosblo...     62.068966          254    Hockin...      59.52381
    9  Nasser...     74.074074          122    Astor,...     58.536585
      fuzz_index_1
    0         37
    1        700
    2        216
    3        879
    4         12
    5        468
    6        464
    7        374
    8        774
    9        700

        Parameters:
            df: [pd.Series]
            limit: int
                How many results do you want to have?
                Each result will have 3 columns [string, match, position in column]
                (default=5)
            partial_full_weighted: str
                weighted = fuzz.WRatio
                full = fuzz.ratio
                partial = fuzz.partial_ratio
                (default="weighted")
            merge_with_series: str
                (default=True)
        Returns:
            pd.DataFrame
    """
    algor = get_algor(partial_full_weighted)

    tmpcolumn = "TEEEEEEEEEEEEEEEEEEEMMMMP______________"
    df_ = df.copy()
    df_ = df_.to_frame().copy()
    column = df_.columns[0]
    df_[tmpcolumn] = df_.index.copy()
    df_ = df_.reset_index(drop=True)
    df_col_as_string = ds_to_string(df_[column]).to_frame()
    finalresults = [
        (
            x[0],
            x[1][0],
            x[1][1],
            process.extract(
                x[1][1],
                df_col_as_string[column].drop(index=x[1][0]),
                scorer=algor,
                limit=limit,
            ),
        )
        for x in enumerate(
            zip(df_col_as_string[column].index, df_col_as_string[column])
        )
    ]
    dframe = explode_lists_and_tuples_in_column(pd.DataFrame(finalresults)[3])
    goodresults = []
    for ini, col in enumerate(dframe):
        r1 = explode_lists_and_tuples_in_column(dframe[col])
        r1.columns = [f"fuzz_string_{ini}", f"fuzz_match_{ini}", f"fuzz_index_{ini}"]
        goodresults.append(r1.copy())
    if merge_with_series:
        df_ = qq_ds_merge_multiple_dfs_and_series_on_index(
            df_, goodresults, how="outer"
        )
        df_.index = df_[tmpcolumn].__array__().copy()
        df_ = df_.drop(columns=[tmpcolumn])
    else:
        originalindex = df_[tmpcolumn].__array__().copy()
        df_ = qq_ds_merge_multiple_dfs_and_series_on_index(
            goodresults[0], (goodresults[1:])
        )
        df_.index = originalindex
    return df_


def get_algor(partial_full_weighted: str):
    algor = fuzz.WRatio
    if partial_full_weighted == "full":
        algor = fuzz.ratio
    if partial_full_weighted == "partial":
        algor = fuzz.partial_ratio
    return algor


def fuzz_matching_one_word(
    df: [pd.Series], word_to_search: str, partial_full_weighted: str = "weighted"
) -> pd.DataFrame:
    """
    df1 = df.Name.s_fuzz_one_word(
    word_to_search="Karolina", partial_full_weighted="weighted"
    )
    df2 = df.Name.s_fuzz_one_word(word_to_search="Karolina", partial_full_weighted="full")
    df3 = df.Name.s_fuzz_one_word(
        word_to_search="Karolina", partial_full_weighted="partial"
    )
    df1
                                                      Name fuzz_string_0  \
    0                              Braund, Mr. Owen Harris      Karolina
    1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)      Karolina
    2                               Heikkinen, Miss. Laina      Karolina
    3         Futrelle, Mrs. Jacques Heath (Lily May Peel)      Karolina
    4                             Allen, Mr. William Henry      Karolina
    5                                     Moran, Mr. James      Karolina
    6                              McCarthy, Mr. Timothy J      Karolina
    7                       Palsson, Master. Gosta Leonard      Karolina
    8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)      Karolina
    9                  Nasser, Mrs. Nicholas (Adele Achem)      Karolina
       fuzz_match_0
    0     41.538462
    1     33.750000
    2     60.000000
    3     33.750000
    4     42.750000
    5     30.000000
    6     27.692308
    7     45.000000
    8     45.600000
    9     42.750000

    df2
                                                      Name fuzz_string_0  \
    0                              Braund, Mr. Owen Harris      Karolina
    1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)      Karolina
    2                               Heikkinen, Miss. Laina      Karolina
    3         Futrelle, Mrs. Jacques Heath (Lily May Peel)      Karolina
    4                             Allen, Mr. William Henry      Karolina
    5                                     Moran, Mr. James      Karolina
    6                              McCarthy, Mr. Timothy J      Karolina
    7                       Palsson, Master. Gosta Leonard      Karolina
    8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)      Karolina
    9                  Nasser, Mrs. Nicholas (Adele Achem)      Karolina
       fuzz_match_0
    0     32.258065
    1     17.241379
    2     33.333333
    3     15.686275
    4     31.250000
    5     25.000000
    6     19.354839
    7     31.578947
    8     21.428571
    9     23.809524

    df3
                                                      Name fuzz_string_0  \
    0                              Braund, Mr. Owen Harris      Karolina
    1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)      Karolina
    2                               Heikkinen, Miss. Laina      Karolina
    3         Futrelle, Mrs. Jacques Heath (Lily May Peel)      Karolina
    4                             Allen, Mr. William Henry      Karolina
    5                                     Moran, Mr. James      Karolina
    6                              McCarthy, Mr. Timothy J      Karolina
    7                       Palsson, Master. Gosta Leonard      Karolina
    8    Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)      Karolina
    9                  Nasser, Mrs. Nicholas (Adele Achem)      Karolina
       fuzz_match_0
    0     46.153846
    1     37.500000
    2     66.666667
    3     37.500000
    4     46.153846
    5     33.333333
    6     30.769231
    7     50.000000
    8     50.000000
    9     40.000000

        Parameters:
            df: [pd.Series]
            word_to_search: str
            partial_full_weighted: str
                weighted = fuzz.WRatio
                full = fuzz.ratio
                partial = fuzz.partial_ratio
                (default="weighted")
        Returns:
            pd.DataFrame
    """
    tmpcolumn = "TEEEEEEEEEEEEEEEEEEEMMMMP______________"

    algor = get_algor(partial_full_weighted)
    df_ = df.copy()
    df_ = df_.to_frame().copy()
    column = df_.columns[0]
    columntocheck = column
    df_[tmpcolumn] = df_.index.copy()
    df_ = df_.reset_index(drop=True)
    resultdf = pd.DataFrame(
        process.extract(
            word_to_search,
            df_[columntocheck],
            scorer=algor,
            limit=len(df_[columntocheck]),
        )
    )
    resultdf = resultdf.set_index(2)
    resultdf.columns = [f"fuzz_string_0", f"fuzz_match_0"]
    df_ = qq_ds_merge_multiple_dfs_and_series_on_index(df_, [resultdf], how="outer")
    originalindex = df_[tmpcolumn].__array__().copy()
    df_ = df_.drop(columns=[tmpcolumn]).copy()
    df_.index = originalindex

    df_["fuzz_string_0"] = word_to_search

    return df_


def series_to_dataframe(
    df: Union[pd.Series, pd.DataFrame]
) -> (Union[pd.Series, pd.DataFrame], bool):
    dataf = df.copy()
    isseries = False
    if isinstance(dataf, pd.Series):
        columnname = dataf.name
        dataf = dataf.to_frame()

        try:
            dataf.columns = [columnname]
        except Exception:
            dataf.index = [columnname]
            dataf = dataf.T
        isseries = True

    return dataf, isseries


def fuzz_compare_row_to_others(
    df: [pd.DataFrame, pd.Series],
    row_number: Union[int, str, tuple],
    loc_or_iloc: str = "loc",
    partial_full_weighted: str = "weighted",
    sort_values: bool = True,
) -> pd.DataFrame:
    """
    from a_pandas_ex_fuzz import pd_add_fuzzy_matching
    pd_add_fuzzy_matching()
    import pandas as pd
    df = pd.read_csv("https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv")
    df.ds_fuzz_compare_row_to_others(2,loc_or_iloc='iloc', partial_full_weighted='full', sort_values=True)
    Out[4]:
         PassengerId  Survived  Pclass  ... Cabin Embarked  aa_fuzz_match
    2              3         1       3  ...   NaN        S     100.000000
    216          217         1       3  ...   NaN        S      90.816327
    816          817         0       3  ...   NaN        S      88.118812
    382          383         0       3  ...   NaN        S      83.769634
    400          401         1       3  ...   NaN        S      83.769634
    ..           ...       ...     ...  ...   ...      ...            ...
    745          746         0       1  ...   B22        S      54.450262
    556          557         1       1  ...   A16        C      53.744493
    581          582         1       1  ...   C68        C      53.456221
    669          670         1       1  ...  C126        S      52.132701
    307          308         1       1  ...   C65        C      51.612903
    [891 rows x 13 columns]


        Parameters:
            df: [pd.DataFrame, pd.Series]
            row_number: Union[int,str,tuple]
                index of the row you want to compare with others
            loc_or_iloc: str
                Do you want to get the row with loc or iloc?
                (default="loc")

            partial_full_weighted: str
                weighted = fuzz.WRatio
                full = fuzz.ratio
                partial = fuzz.partial_ratio
                (default="weighted")
            sort_values: bool
                Return in descending order
                (default=True)
        Returns:
            pd.DataFrame
    """
    tmpcol = "___________a_string"
    df2, _ = series_to_dataframe(df)
    df3, _ = series_to_dataframe(df)
    df2[tmpcol] = ds_to_string(df2).apply(lambda x: str(x.__array__()), axis=1)
    if loc_or_iloc == "loc":
        #
        df3["aa_fuzz_match"] = fuzz_matching_one_word(
            df2[tmpcol],
            df2[tmpcol].loc[row_number],
            partial_full_weighted=partial_full_weighted,
        )["fuzz_match_0"].copy()
    else:
        df3["aa_fuzz_match"] = fuzz_matching_one_word(
            df2[tmpcol],
            df2[tmpcol].iloc[row_number],
            partial_full_weighted=partial_full_weighted,
        )["fuzz_match_0"].copy()

    if not sort_values:
        return df3
    return df3.sort_values(by="aa_fuzz_match", ascending=False)


def pd_add_fuzzy_matching():
    PandasObject.s_fuzz_one_word = fuzz_matching_one_word
    PandasObject.s_fuzz_all_values_in_column = (
        compare_values_in_column_against_each_other
    )
    PandasObject.s_fuzz_from_list = compare_values_in_column_against_list
    PandasObject.ds_fuzz_compare_row_to_others = fuzz_compare_row_to_others

