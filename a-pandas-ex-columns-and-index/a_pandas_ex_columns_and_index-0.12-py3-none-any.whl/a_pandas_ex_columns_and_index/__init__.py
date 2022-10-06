import numpy as np
import regex
from natsort import ns, index_natsorted, natsorted
import pandas as pd
from typing import Union
from pandas.core.frame import DataFrame, Series

def change_places_2_columns(
    df: pd.DataFrame, column1: Union[str, float, int], column2: Union[str, float, int]
) -> pd.DataFrame:
    colsaslist = df.columns.to_list()
    indexof1 = colsaslist.index(column1)
    indexof2 = colsaslist.index(column2)
    coldict = {}
    for ini, col in enumerate(colsaslist):
        coldict[ini] = col
    coldict[indexof1] = column2
    coldict[indexof2] = column1
    finalcols = [x[1] for x in coldict.items()]
    return df.filter(finalcols).copy()


def qq_ds_sort_len(
    df: Union[pd.DataFrame, pd.Series],
    column: Union[str, float, int, None] = None,
    axis: int = 0,
    ascending: bool = True,
    kind: str = "quicksort",
    na_position: str = "last",
    ignore_index: bool = False,
    key=None,
) -> Union[pd.DataFrame, pd.Series]:
    df2 = df.copy()
    isseries = isinstance(df2, pd.Series)
    if isseries:
        df2 = df2.to_frame().copy()
    if column is None:
        column = df2.columns[0]
    df2["_____TMP_____INDEX"] = df2.index
    df2 = df2.reset_index(drop=True).copy()
    df3 = df2.reindex(
        df2[column]
        .astype(str)
        .apply(len)
        .sort_values(
            axis=axis,
            ascending=ascending,
            inplace=False,
            kind=kind,
            na_position=na_position,
            ignore_index=ignore_index,
            key=key,
        )
        .index
    ).copy()
    newindex = df3["_____TMP_____INDEX"].__array__().tolist().copy()
    df3 = df3.drop(columns=["_____TMP_____INDEX"])
    df3.index = newindex
    if isseries:
        return df3[df2.columns[0]]
    return df3


def qq_d_insert_column_before_column(
    df: pd.DataFrame,
    column_to_insert: Union[list, pd.Series, np.ndarray],
    name_of_new_column: Union[str, float, int],
    name_of_column_present_in_df: Union[str, float, int],
) -> pd.DataFrame:
    df2 = df.copy()
    collist = df2.columns.to_list()
    index_of_old_element = collist.index(name_of_column_present_in_df)
    collist.insert(index_of_old_element, name_of_new_column)
    df2[name_of_new_column] = column_to_insert
    return df2.filter(collist).copy()


def reverse_dataframe(
    df: Union[pd.DataFrame, pd.Series]
) -> Union[pd.Series, pd.DataFrame]:
    df2 = df.copy()
    is_series = isinstance(df2, pd.Series)
    if is_series:
        df2 = df2.to_frame().copy()
    df3 = (
        df2.assign(____helper___=list(reversed(range(len(df2)))))
        .sort_values(by="____helper___")
        .drop(columns="____helper___")
        .copy()
    )
    if is_series:
        return df3[df2.columns[0]]
    return df3


def add_prefix_to_column_when_regex(
    df: pd.DataFrame, prefix: str, regular_expression: str = ".*"
) -> pd.DataFrame:
    df2 = df.copy()
    regular_expression_ = regex.compile(regular_expression)
    df2.columns = [
        f"{prefix}{x}" if regular_expression_.search(str(x)) is not None else str(x)
        for x in df2.columns
    ]
    return df2


def add_prefix_to_index_when_regex(
    df: pd.DataFrame, prefix, regular_expression: str = ".*"
) -> pd.DataFrame:
    df2 = df.copy()
    regular_expression_ = regex.compile(regular_expression)
    df2.index = [
        f"{prefix}{x}" if regular_expression_.search(str(x)) is not None else str(x)
        for x in df2.index
    ]
    return df2


def regex_filter_index(
    df: pd.DataFrame, regular_expression: str = ".*"
) -> pd.DataFrame:
    regular_expression_ = regex.compile(regular_expression)
    newindex = [
        y
        for y, x in enumerate(df.index)
        if regular_expression_.search(str(x)) is not None
    ]
    return df.iloc[newindex].copy()


def regex_filter_columns(
    df: pd.DataFrame, regular_expression: str = ".*"
) -> pd.DataFrame:
    regular_expression_ = regex.compile(regular_expression)
    newcols = [x for x in df.columns if regular_expression_.search(str(x)) is not None]
    if any(newcols):
        return df[newcols].copy()
    return pd.Dataframe()


def columns_upper(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2.columns = [str(x).upper() for x in df2.columns]
    return df2


def index_upper(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2.index = [str(x).upper() for x in df2.index]
    return df2


def index_lower(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2.index = [str(x).lower() for x in df2.index]
    return df2


def columns_lower(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2.columns = [str(x).lower() for x in df2.columns]
    return df2


def make_columns_dot_compatible(
    df: pd.DataFrame, lowercase: bool = True
) -> pd.DataFrame:
    def name_ok(name):
        return name.isidentifier()

    allresults = []
    compiledregex = regex.compile(r"^\d+$")
    for variablenname in df.columns:
        variablenname_formatiert = str(variablenname).strip("-")
        variablenname_formatiert = regex.sub(r"[--]+", "_", variablenname_formatiert)
        variablenname_formatiert = regex.sub(r"\W+", "_", variablenname_formatiert)
        variablenname_formatiert = regex.sub(r"_+", "_", variablenname_formatiert)

        if compiledregex.search(variablenname_formatiert) is not None:
            variablenname_formatiert = "_" + variablenname_formatiert
        if lowercase:
            variablenname_formatiert = variablenname_formatiert.lower()
        allright = name_ok(variablenname_formatiert)

        if allright:

            allresults.append(variablenname_formatiert)
        else:
            print(f"Could not convert: {variablenname}")
            allresults.append(variablenname)
    df2 = df.copy()
    df2.columns = allresults
    return df2


def qq_d_sort_index(
    df: pd.DataFrame,
    parse_numbers_as_integers: bool = False,
    parse_numbers_as_floats: bool = False,
    ignore_signs_left_of_number: bool = False,
    not_ignore_signs_left_of_number: bool = False,
    sort_real_numbers: bool = False,
    not_search_for_exponents_in_float_number: bool = False,
    sort_numbers_after_non_numbers: bool = False,
    strings_as_filesystem_paths: bool = False,
    use_nfkd_unicode_normalization: bool = False,
    locale_aware: bool = False,
    locale_aware_only_alphabet: bool = False,
    locale_aware_only_number_sep: bool = False,
    ignore_case: bool = False,
    lowercase_first: bool = False,
    group_lower_and_uppercase: bool = False,
    uppercase_first: bool = False,
    nan_after_other_numbers: bool = False,
) -> pd.DataFrame:
    df2 = df.copy()
    df2["_____TMP_____INDEX"] = df2.index
    df2 = sort_whole_df_with_natsort(
        df2.copy(),
        "_____TMP_____INDEX",
        parse_numbers_as_integers=parse_numbers_as_integers,
        parse_numbers_as_floats=parse_numbers_as_floats,
        ignore_signs_left_of_number=ignore_signs_left_of_number,
        not_ignore_signs_left_of_number=not_ignore_signs_left_of_number,
        sort_real_numbers=sort_real_numbers,
        not_search_for_exponents_in_float_number=not_search_for_exponents_in_float_number,
        sort_numbers_after_non_numbers=sort_numbers_after_non_numbers,
        strings_as_filesystem_paths=strings_as_filesystem_paths,
        use_nfkd_unicode_normalization=use_nfkd_unicode_normalization,
        locale_aware=locale_aware,
        locale_aware_only_alphabet=locale_aware_only_alphabet,
        locale_aware_only_number_sep=locale_aware_only_number_sep,
        ignore_case=ignore_case,
        lowercase_first=lowercase_first,
        group_lower_and_uppercase=group_lower_and_uppercase,
        uppercase_first=uppercase_first,
        nan_after_other_numbers=nan_after_other_numbers,
    )
    return df2.drop(columns=["_____TMP_____INDEX"]).copy()


def qq_d_sort_columns(
    df: pd.DataFrame,
    ascending: bool = True,
    parse_numbers_as_integers: bool = False,
    parse_numbers_as_floats: bool = False,
    ignore_signs_left_of_number: bool = False,
    not_ignore_signs_left_of_number: bool = False,
    sort_real_numbers: bool = False,
    not_search_for_exponents_in_float_number: bool = False,
    sort_numbers_after_non_numbers: bool = False,
    strings_as_filesystem_paths: bool = False,
    use_nfkd_unicode_normalization: bool = False,
    locale_aware: bool = False,
    locale_aware_only_alphabet: bool = False,
    locale_aware_only_number_sep: bool = False,
    ignore_case: bool = False,
    lowercase_first: bool = False,
    group_lower_and_uppercase: bool = False,
    uppercase_first: bool = False,
    nan_after_other_numbers: bool = False,
) -> pd.DataFrame:
    searchalgo = pd_natsearch(
        parse_numbers_as_integers=parse_numbers_as_integers,
        parse_numbers_as_floats=parse_numbers_as_floats,
        ignore_signs_left_of_number=ignore_signs_left_of_number,
        not_ignore_signs_left_of_number=not_ignore_signs_left_of_number,
        sort_real_numbers=sort_real_numbers,
        not_search_for_exponents_in_float_number=not_search_for_exponents_in_float_number,
        sort_numbers_after_non_numbers=sort_numbers_after_non_numbers,
        strings_as_filesystem_paths=strings_as_filesystem_paths,
        use_nfkd_unicode_normalization=use_nfkd_unicode_normalization,
        locale_aware=locale_aware,
        locale_aware_only_alphabet=locale_aware_only_alphabet,
        locale_aware_only_number_sep=locale_aware_only_number_sep,
        ignore_case=ignore_case,
        lowercase_first=lowercase_first,
        group_lower_and_uppercase=group_lower_and_uppercase,
        uppercase_first=uppercase_first,
        nan_after_other_numbers=nan_after_other_numbers,
    )
    newcolumsn = natsorted(df.columns, alg=searchalgo)
    if ascending is False:
        newcolumsn = reversed(newcolumsn)
    return df.filter(newcolumsn).copy()


def pd_natsearch(
    parse_numbers_as_integers: bool = False,
    parse_numbers_as_floats: bool = False,
    ignore_signs_left_of_number: bool = False,
    not_ignore_signs_left_of_number: bool = False,
    sort_real_numbers: bool = False,
    not_search_for_exponents_in_float_number: bool = False,
    sort_numbers_after_non_numbers: bool = False,
    strings_as_filesystem_paths: bool = False,
    use_nfkd_unicode_normalization: bool = False,
    locale_aware: bool = False,
    locale_aware_only_alphabet: bool = False,
    locale_aware_only_number_sep: bool = False,
    ignore_case: bool = False,
    lowercase_first: bool = False,
    group_lower_and_uppercase: bool = False,
    uppercase_first: bool = False,
    nan_after_other_numbers: bool = False,
) -> int:
    all_ops = []
    if parse_numbers_as_integers is True:
        all_ops.append(ns.__dict__["_member_map_"]["INT"])

    if parse_numbers_as_floats is True:
        all_ops.append(ns.__dict__["_member_map_"]["FLOAT"])

    if ignore_signs_left_of_number is True:
        all_ops.append(ns.__dict__["_member_map_"]["UNSIGNED"])

    if not_ignore_signs_left_of_number is True:
        all_ops.append(ns.__dict__["_member_map_"]["SIGNED"])

    if sort_real_numbers is True:
        all_ops.append(ns.__dict__["_member_map_"]["REAL"])

    if not_search_for_exponents_in_float_number is True:
        all_ops.append(ns.__dict__["_member_map_"]["NOEXP"])

    if sort_numbers_after_non_numbers is True:
        all_ops.append(ns.__dict__["_member_map_"]["NUMAFTER"])

    if strings_as_filesystem_paths is True:
        all_ops.append(ns.__dict__["_member_map_"]["PATH"])

    if use_nfkd_unicode_normalization is True:
        all_ops.append(ns.__dict__["_member_map_"]["COMPATIBILITYNORMALIZE"])

    if locale_aware is True:
        all_ops.append(ns.__dict__["_member_map_"]["LOCALE"])

    if locale_aware_only_alphabet is True:
        all_ops.append(ns.__dict__["_member_map_"]["LOCALEALPHA"])

    if locale_aware_only_number_sep is True:
        all_ops.append(ns.__dict__["_member_map_"]["LOCALENUM"])

    if ignore_case is True:
        all_ops.append(ns.__dict__["_member_map_"]["IGNORECASE"])

    if lowercase_first is True:
        all_ops.append(ns.__dict__["_member_map_"]["LOWERCASEFIRST"])

    if group_lower_and_uppercase is True:
        all_ops.append(ns.__dict__["_member_map_"]["GROUPLETTERS"])

    if uppercase_first is True:
        all_ops.append(ns.__dict__["_member_map_"]["CAPITALFIRST"])

    if nan_after_other_numbers is True:
        all_ops.append(ns.__dict__["_member_map_"]["NANLAST"])
    searchalgo = None
    if len(all_ops) > 0:
        searchalgo = all_ops[0]
    if len(all_ops) == 1:
        searchalgo = searchalgo
    if len(all_ops) > 1:
        for sec in all_ops[1:]:
            searchalgo = searchalgo | sec
    return searchalgo


def sort_whole_df_with_natsort(
    df: pd.DataFrame,
    column: Union[str, float, int],
    parse_numbers_as_integers: bool = False,
    parse_numbers_as_floats: bool = False,
    ignore_signs_left_of_number: bool = False,
    not_ignore_signs_left_of_number: bool = False,
    sort_real_numbers: bool = False,
    not_search_for_exponents_in_float_number: bool = False,
    sort_numbers_after_non_numbers: bool = False,
    strings_as_filesystem_paths: bool = False,
    use_nfkd_unicode_normalization: bool = False,
    locale_aware: bool = False,
    locale_aware_only_alphabet: bool = False,
    locale_aware_only_number_sep: bool = False,
    ignore_case: bool = False,
    lowercase_first: bool = False,
    group_lower_and_uppercase: bool = False,
    uppercase_first: bool = False,
    nan_after_other_numbers: bool = False,
) -> pd.DataFrame:
    searchalgo = pd_natsearch(
        parse_numbers_as_integers=parse_numbers_as_integers,
        parse_numbers_as_floats=parse_numbers_as_floats,
        ignore_signs_left_of_number=ignore_signs_left_of_number,
        not_ignore_signs_left_of_number=not_ignore_signs_left_of_number,
        sort_real_numbers=sort_real_numbers,
        not_search_for_exponents_in_float_number=not_search_for_exponents_in_float_number,
        sort_numbers_after_non_numbers=sort_numbers_after_non_numbers,
        strings_as_filesystem_paths=strings_as_filesystem_paths,
        use_nfkd_unicode_normalization=use_nfkd_unicode_normalization,
        locale_aware=locale_aware,
        locale_aware_only_alphabet=locale_aware_only_alphabet,
        locale_aware_only_number_sep=locale_aware_only_number_sep,
        ignore_case=ignore_case,
        lowercase_first=lowercase_first,
        group_lower_and_uppercase=group_lower_and_uppercase,
        uppercase_first=uppercase_first,
        nan_after_other_numbers=nan_after_other_numbers,
    )
    if searchalgo is not None:

        df2 = df.copy().sort_values(
            by=column,
            key=lambda x: np.argsort(index_natsorted(df[column], alg=searchalgo)),
        )
        return df2.copy()
    else:
        df2 = df.copy().sort_values(
            by=column, key=lambda x: np.argsort(index_natsorted(df[column]))
        )
        return df2.copy()


def pd_add_index_and_columns():
    DataFrame.d_swap_2_columns = change_places_2_columns
    DataFrame.ds_sort_by_str_length = qq_ds_sort_len
    Series.ds_sort_by_str_length = qq_ds_sort_len

    DataFrame.d_insert_column_before_another = qq_d_insert_column_before_column
    DataFrame.ds_reverse = reverse_dataframe
    Series.ds_reverse = reverse_dataframe

    DataFrame.d_add_prefix_to_column_when_regex_match = (
        add_prefix_to_column_when_regex
    )
    DataFrame.d_add_prefix_to_index_when_regex_match = add_prefix_to_index_when_regex
    DataFrame.d_filter_df_by_regex_in_index = regex_filter_index
    DataFrame.d_filter_df_by_regex_in_columns = regex_filter_columns
    DataFrame.d_columns_upper = columns_upper
    DataFrame.d_index_upper = index_upper
    DataFrame.d_index_lower = index_lower
    DataFrame.d_columns_lower = columns_lower
    DataFrame.d_make_columns_dot_compatible = make_columns_dot_compatible
    DataFrame.d_natsort_index = qq_d_sort_index
    DataFrame.d_natort_columns = qq_d_sort_columns
    DataFrame.d_natsort_df_by_column = sort_whole_df_with_natsort
