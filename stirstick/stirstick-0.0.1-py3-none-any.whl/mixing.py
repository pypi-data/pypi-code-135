# the mixing module for stirstick
# herein lies all the functions for calculating two and three
# component mixing largely taken from Albarede (1995)
# "Intro to Geochemical Modeling"

import numpy as np
import pandas as pd
import warnings


def concentration_mixing_2c(c1, c2, resolution=0.1):
    """calculate the concentration of a two component mixture from the concentrations of two end-members

    Args:
        c1 (float): concentration of end-member 1
        c2 (float): concentration of end-member 2
        resolution (float, optional): The spacing of the array at which component
        fractions are generated. Defaults to 0.1 which creates the array:
        ndarray([0.0, 0.1, 0.2, 0.3, 0.4....1.0])

    Returns:
       array-like : the concentration of the mixture in the same shape as f. E.g., if f is a float, this will
       be a float and if f is an array it will be the same shape as the array
    """
    f = np.linspace(0,1, int(np.ceil(1/resolution))+1 )
    cm = c1 * f + c2 * (1 - f)
    df = pd.DataFrame({ "f_1": f,"concentration": cm,})
    return df


def concentration_mixing_3c(c1, c2, c3, resolution=0.1):
    """calculates the concentration of a mixture over a 2D mesh space given 3 end-member concentrations

    Args:
        c1 (float): concentration of end-member 1
        c2 (float): concentration of end-member 2
        c3 (float): concentration of end-member 3
        resolution (float, optional): The spacing of the array at which component
        fractions are generated. Defaults to 0.1 which creates the array:
        ndarray([0.0, 0.1, 0.2, 0.3, 0.4....1.0])
    Returns:
        pandas DataFrame: dataframe that contains 4 columns: concentration, f_1, f_2, f_3
        where each row represents every possible combination of component fractions that
        sum to unity with the specified resolution
    """
    if resolution < 0.01:
        warnings.warn(
            "Please pick a lower resolution (e.g., bigger number).\nYou don't need it and it your computer may explode"
        )

    if resolution > 0.5:
        warnings.warn(
            "Your resolution will return no values. Please pick a higher resolution (e.g., number < 0.5). \n"
        )

    f = np.linspace(0,1, int(np.ceil(1/resolution))+1 )
    a = np.array(np.meshgrid(f, f, f)).T.reshape(-1, 3)
    f_unity = a[a.sum(axis=1) == 1]
    cm = c1 * f_unity[:, 0] + c2 * f_unity[:, 1] + c3 * f_unity[:, 2]
    df = pd.concat(
        [pd.DataFrame(f_unity), pd.DataFrame(cm) ],
        axis="columns",
    )
    df.columns = ["f_1", "f_2", "f_3", "concentration" ]

    return df


def ratio_concentration_mixing_2c(df, resolution=0.1):
    """Calculate the concentration of a 2 end-member mixture between a ratio of two componenets
    and a concentration according to Albarede (1995) eq. 1.3.7

    Args:
        df (DataFrame): a 2 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |

        resolution (float, optional): The spacing of the array at which component
        fractions are generated. Defaults to 0.1 which creates the array:
        ndarray([0.0, 0.1, 0.2, 0.3, 0.4....1.0])

    Returns:
        pandas DataFrame: DataFrame with 3 columns: f1, c_mix, r_mix
        f1 = fraction of end-member 1 in the mixture
        c_mix = concentration of the mixture for corresponding f1 value
        r_mix = ratio value of the mixture for corresponding f1 value

        f_endmember1|component1_c_mix|component1_r_mix|
        -----------------------------------------------

        _c refers to the concentration of the mixture
        _r refers to the value of the ratio of the mixture

    """
    endmembers = df.index.tolist()

    concentrations = df[[column for column in df.columns if "_c" in column][0]]
    f = np.linspace(0,1, int(np.ceil(1/resolution))+1 )
    f = f[::-1]
    c1 = concentrations[0]
    c2 = concentrations[1]
    ratios = df[[column for column in df.columns if "_r" in column][0]]
    r1 = ratios[0]
    r2 = ratios[1]

    c_mixes = c1 * f + c2 * (1 - f)
    r_mixes = r1 * ((c1 * f) / c_mixes) + r2 * ((c2 * (1 - f)) / c_mixes)
    dff = pd.DataFrame([f, c_mixes, r_mixes]).T
    dff.columns = [
        f"f_{endmembers[0]}",
        f"{[column for column in df.columns if '_c' in column][0]}_mix",
        f"{[column for column in df.columns if '_r' in column][0]}_mix",
    ]

    return dff


def ratio_concentration_mixing_3c(df, resolution=0.1):
    """calculate the concentration of a 3 end-member mixture between a ratio of two componenets
    and a concentration according to the extrapolation of Albarede (1995) eq. 1.3.7

    Args:
        df (DataFrame): a 3 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |
            ----------------------------
            C    |          |

        resolution (float, optional): The spacing of the array at which component
        fractions are generated. Defaults to 0.1 which creates the array:
        ndarray([0.0, 0.1, 0.2, 0.3, 0.4....1.0])

    Returns:
        pandas DataFrame: DataFrame with 5 columns: f1, f2, f3, c_mix, r_mix
        f1 = fraction of end-member 1 in the mixture
        f2 = fraction of end-member 2 in the mixture
        f3 = fraction of end-member 13 in the mixture
        c_mix = concentration of the mixture for corresponding f values
        r_mix = ratio value of the mixture for corresponding f values:

        f_endmember1|f_endmember2|f_endmember3|component1_c_mix|component1_r_mix|
        -------------------------------------------------------------------------
        _c refers to the concentration of the mixture
        _r refers to the value of the ratio of the mixture
    """
    if resolution < 0.01:
        warnings.warn(
            "Please pick a lower resolution (e.g., bigger number).\nYou don't need it and it your computer may explode"
        )

    if resolution > 0.5:
        warnings.warn(
            "Your resolution will return no values. Please pick a higher resolution (e.g., number < 0.5). \n"
        )

    endmembers = df.index.tolist()
    concentrations = df[[column for column in df.columns if "_c" in column][0]]
    c1 = concentrations[0]
    c2 = concentrations[1]
    c3 = concentrations[2]

    ratios = df[[column for column in df.columns if "_r" in column][0]]
    r1 = ratios[0]
    r2 = ratios[1]
    r3 = ratios[2]

    concentration_df = concentration_mixing_3c(c1, c2, c3, resolution=resolution)
    c_mixes = concentration_df["concentration"]
    f_unity = concentration_df.loc[:, ["f_1","f_2","f_3"]]

    r_mixes = (
        r1 * ((c1 * f_unity["f_1"]) / c_mixes)
        + r2 * ((c2 * f_unity["f_2"]) / c_mixes)
        + r3 * ((c3 * f_unity["f_3"]) / c_mixes)
    )

    dff = pd.concat(
        [f_unity, c_mixes, pd.DataFrame(r_mixes, columns=["ratio"])], axis="columns"
    )
    dff.columns = [f"f_{member}" for member in endmembers] + [
        f"{[column for column in df.columns if '_c' in column][0]}_mix",
        f"{[column for column in df.columns if '_r' in column][0]}_mix",
    ]

    return dff


def ratio_ratio_mixing_2c(df1, df2, resolution=0.1):
    """calculate the values of a two end-member mixture of ratios over a range
    of end-member fraction values


    Args:
        df1 (pandas DataFrame): Component 1. a 2 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |
        df2 (pandas DataFrame): Component 2. a 2 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |

        resolution (float, optional): The spacing of the array at which component
        fractions are generated. Defaults to 0.1 which creates the array:
        ndarray([0.0, 0.1, 0.2, 0.3, 0.4....1.0])

    Returns:
        pandas DataFrame: a pandas dataframe that has 5 columns by number of possible f values
        that sum to unity for a given resolution (e.g., 0.1 == 62, 0.01 == 5027):

        f_endmember1|  component1_c_mix | component1_r_mix |   component2_c_mix | component2_r_mix |

        _c refers to the concentration of the mixture
        _r refers to the value of the ratio of the mixture

    """
    endmembers = df1.index.tolist()
    a_mixes = ratio_concentration_mixing_2c(df1, resolution = resolution)
    b_mixes = ratio_concentration_mixing_2c(df2, resolution = resolution)

    df = pd.concat([a_mixes, b_mixes], axis="columns")
    df.columns = [
        f"f_{endmembers[0]}",
        f"{[column for column in df1.columns if '_c' in column][0]}_mix",
        f"{[column for column in df1.columns if '_r' in column][0]}_mix",
        "f1_drop",
        f"{[column for column in df2.columns if '_c' in column][0]}_mix",
        f"{[column for column in df2.columns if '_r' in column][0]}_mix",
    ]
    df.drop("f1_drop", axis="columns", inplace=True)

    return df


def ratio_ratio_mixing_3c(df1, df2, resolution=0.1):
    """calculate the values of a two end-member mixture of ratios over a range
    of end-member fraction values


    Args:
        df1 (pandas DataFrame): Component 1. a 3 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |
            ----------------------------
            C    |          |

        df2 (pandas DataFrame): Component 2. a 3 x 2 pandas DataFrame where columns correspond to values
        and rows correspond to end-member observations. Column for concentration values
        is denoted with "_c" and column for ratio values is denoted with "_r".

        Ex:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |
            ----------------------------
            C    |          |

        f (array-like): fraction of end-member 1. End-member 1 is the first row
        in the input DataFrame(df)


    Returns:
        pandas DataFrame: a pandas dataframe that has 5 columns by number of possible f values
        that sum to unity for a given resolution (e.g., 0.1 == 62, 0.01 == 5027):

        f_endmember1|f_endmember2|f_endmember3|component1_c_mix|component1_r_mix|component2_c_mix|component2_r_mix|

        _c refers to the concentration of the mixture
        _r refers to the value of the ratio of the mixture
    """
    if resolution < 0.01:
        warnings.warn(
            "Please pick a lower resolution (e.g., bigger number).\nYou don't need it and it your computer may explode"
        )

    if resolution > 0.5:
        warnings.warn(
            "Your resolution will return no values. Please pick a higher resolution (e.g., number < 0.5). \n"
        )

    component1_mixes = ratio_concentration_mixing_3c(df1, resolution)
    component2_mixes = ratio_concentration_mixing_3c(df2, resolution)

    dff = pd.concat([component1_mixes, component2_mixes], axis="columns")
    dff.drop(dff.columns[[5, 6, 7]], axis="columns", inplace=True)
    dff = pd.concat([component1_mixes.iloc[:, :3], dff], axis="columns")
    return dff
