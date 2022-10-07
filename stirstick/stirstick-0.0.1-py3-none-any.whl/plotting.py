# the plotting module for stirstick
# herein lies all the functions for plotting two and three
# component misture models calculated in stirstick.mixing

import matplotlib.pyplot as plt


def plot_2concentration_mixture(
    mix_x,
    mix_y,
    f,
    annotate=False,
    plot_every=1,
    annotate_every=2,
    annotate_precision=2,
    annotate_direction="top",
    ax=None,
    **plt_kwargs,
):
    """plot the results from a mixture model between two endmember concentrations

    Args:
        mix_x (array-like): x-values of a mixture model to be plotted.
        (e.g., the 'concentration' column output from the
        mixing.concentration_mixing_2c())

        mix_y (array-like): y values of a mixture model to be plotted.
        (e.g., the 'concentration' column output from the
        mixing.concentration_mixing_2c())

        f (array-like): f values of component 1 (e.g., the 'f1' column
        output from the mixing.concentration_mixing_2c()).

        annotate (bool, optional): Whether or not to annotate points
        on the figure with the f value. Defaults to False.

        plot_every (int, optional): The frequency of markers to plot
        in the mixing model. Defaults to 1.

        annotate_every (int, optional): The frequency of annotations
        to plot on the figure. Only applicable if annotate = True.
        Defaults to 2.

        annotate_precision (int, optional): The precision of the
        label to annotate (e.g., how many decimal places to show)

        annotate_direction (str, optional): The direction relative
        to the mixing line to annotate. Options are 'right', 'left',
        'top', 'bottom'. Default is 'top'.

        ax (_type_, optional): The matplotlib axis object to plot on.
        Defaults to None.

    Returns:
        matplotlib axis object: Mixture model figure
    """
    if ax is None:
        ax = plt.gca()
    ax.plot(mix_x, mix_y, markevery=plot_every, **plt_kwargs)

    if annotate is True:

        if annotate_direction == "top":

            for x, y, label in zip(
                mix_x[::annotate_every],
                mix_y[::annotate_every],
                f[::annotate_every],
            ):

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x, y),
                    xytext=(-7, 20),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )

        elif annotate_direction == "right":

            for x, y, label in zip(
                mix_x[::annotate_every],
                mix_y[::annotate_every],
                f[::annotate_every],
            ):

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x, y),
                    xytext=(15, 0),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )
        elif annotate_direction == "left":

            for x, y, label in zip(
                mix_x[::annotate_every],
                mix_y[::annotate_every],
                f[::annotate_every],
            ):

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x, y),
                    xytext=(-32, 0),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )

        elif annotate_direction == "bottom":

            for x, y, label in zip(
                mix_x[::annotate_every],
                mix_y[::annotate_every],
                f[::annotate_every],
            ):

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x, y),
                    xytext=(-7, -25),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )

    return ax


def annotate_endmembers(df, x, y, box_kwargs=None, zorder=0, ax = None):
    """Add patches for each end-member in the mixing model

    Args:
        df (pandas DataFrame): pandas DataFrame representing the compositions
        of the end-members. This is the input for any of the functions in
        stirstick.mixing
        Ex: for two end-member model between concentration and ratio:
            Index|   Sr_c   | Sr87-88_r
            ----------------------------
            A    |          |
            ----------------------------
            B    |          |


            Note that the name of the label is taken from the index of the dataframe

        x (str): name of the column corresponding to the x values
        y (str): name of the column corresponding to the y values
        box_kwargs (dict, optional): dictionary of keyword arguments to customize
        the bounding box. This is analgous to the bbox = {} in plt.annotate.
        Defaults to None.
        zorder (int, optional): The plotting order. Defaults to being behind everything
        else. To plot on top choose zorder = 10. Defaults to 0.

    Returns:
        matplotlib axis: matplotlib axis with end-member patches added
    """
    if ax is None:
        ax = plt.gca()

    if box_kwargs is None:
        box_kwargs = {"boxstyle": "circle", "fc": "bisque", "alpha": 0.8, "pad": 0.25}

    for x, y, e in zip(df[x], df[y], df.index):
        ax.annotate(
            e, xy=(x, y), ha="center", va="center", bbox=box_kwargs, zorder=zorder
        )

    return ax


def plot_3concentration_mixture(
    df1,
    df2,
    mesh_every=1,
    border_every=1,
    mesh_kwargs={"marker": "", "ls": "-", "c": "k", "lw": 0.5},
    border_kwargs={"marker": ".", "mfc": "w", "ls": "-", "c": "k", "lw": 1},
    ax=None,
):
    """plot the results from a mixture model between three end-member concentrations

    Args:
        df1 (pandas DataFrame): x-axis concentrations to be plotted. This is the
        output from concentration_mixing_3c()

        df2 (pandas DataFrame): y-axis concentrations to be plotted. This is the
        output from concentration_mixing_3c()

        mesh_every (int, optional): the spacing of the lines in the 2D mesh that
        represent the mixing model. This is relative to the initial mixing model
        spacing. Defaults to 1.

        border_every (int, optional): the spacing of the markers in the lines that
        represent the borders of the mixing model. This is relative to the initial
        mixing model spacing. Defaults to 1.

        mesh_kwargs (dict, optional): dictionary of key word arguments to customize
        the lines in the 2D mesh. Inherits from matplotlib.pyplot.plot().
        Defaults to {}.

        border_kwargs (dict, optional): dictionary of key word arguments to customize
        the lines for the borders. Inherits from matplotlib.pyplot.plot().
        Defaults to {}.

        ax (matplotlib axis, optional): The matplotlib axis to plot on. If no axis is
        specified it defaults to the current axis. Defaults to None.

    Returns:
        matplotlib axis: matplotlib axis with the mixing model displayed
    """

    if ax is None:
        ax = plt.gca()

    for endmember in ["f_1", "f_2", "f_3"]:
        for val in df1.loc[:, "f_1"].unique()[::mesh_every]:
            ax.plot(
                df1[df1[endmember] == val]["concentration"],
                df2[df2[endmember] == val]["concentration"],
                **mesh_kwargs,
                zorder=0,
            )
        ax.plot(
            df1.loc[df1[endmember] == 0]["concentration"],
            df2.loc[df2[endmember] == 0]["concentration"],
            markevery=border_every,
            **border_kwargs,
        )

    return ax


def plot_2ratio_mixture(
    df,
    x,
    y,
    annotate=False,
    plot_every=1,
    annotate_every=2,
    annotate_precision=2,
    annotate_direction="top",
    ax=None,
    **plt_kwargs,
):
    """plot the results from a mixture model of two end-members of either
    ratio vs. concentration or ratio vs. ratio.

    Args:
        df (pandas DataFrame): pandas DataFrame. This is the output from the
        conentration_ratio_mixing_2c() or ratio_ratio_mixing_2c() functions

        x (str): name of the column correpsonding to the x variable

        y (str): name of the column corresponding to the y variable

        annotate (bool, optional): Whether or not to annotate points
        on the figure with the f value. Defaults to False.

        plot_every (int, optional): The frequency of markers to plot
        in the mixing model. Defaults to 1.

        annotate_every (int, optional): The frequency of annotations
        to plot on the figure. Only applicable if annotate = True.
        Defaults to 2.

        annotate_precision (int, optional): The precision of the
        label to annotate (e.g., how many decimal places to show)

        annotate_direction (str, optional): The direction relative
        to the mixing line to annotate. Options are 'right', 'left',
        'top', 'bottom'. Default is 'top'.

        ax (_type_, optional): The matplotlib axis object to plot on.
        Defaults to None.

    Returns:
        matplotlib axis object: Mixture model figure

    """
    if ax is None:
        ax = plt.gca()

    ax.plot(df[x], df[y], markevery=plot_every, **plt_kwargs)
    endmember = [column for column in df.columns if "f_" in column][0]

    if annotate is True:

         for x_val, y_val, label in zip(
                df[x][::annotate_every],
                df[y][::annotate_every],
                df[endmember][::annotate_every],
            ):

            if annotate_direction == "top":

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x_val, y_val),
                    xytext=(-7, 20),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )

            elif annotate_direction == "right":

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x_val, y_val),
                    xytext=(15, 0),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )
            elif annotate_direction == "left":

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x_val, y_val),
                    xytext=(-32, 0),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )

            elif annotate_direction == "bottom":

                ax.annotate(
                    text=f"{label:.{annotate_precision}}",
                    xy=(x_val, y_val),
                    xytext=(-7, -25),
                    arrowprops={"arrowstyle": "-"},
                    textcoords="offset pixels",
                )
    ax.set_xlabel(x.replace("_mix", ""))
    ax.set_ylabel(y.replace("_mix", ""))

    return ax


def plot_3ratio_mixture(
    df,
    x,
    y,
    mesh_every=1,
    border_every=1,
    mesh_kwargs={"marker": "", "ls": "-", "c": "k", "lw": 0.5},
    border_kwargs={"marker": ".", "mfc": "w", "ls": "-", "c": "k", "lw": 1},
    ax=None,
):
    """plot the results from a mixture model with three end-members of either
        ratio vs. concentration or ratio vs. ratio.

    Args:
        df (pandas DataFrame): pandas DataFrame. This is the output from the
        conentration_ratio_mixing_2c() or ratio_ratio_mixing_2c() functions

        x (str): name of the column correpsonding to the x variable

        y (str): name of the column corresponding to the y variable

        mesh_every (int, optional): the spacing of the lines in the 2D mesh that
        represent the mixing model. This is relative to the initial mixing model
        spacing. Defaults to 1.

        border_every (int, optional): the spacing of the markers in the lines that
        represent the borders of the mixing model. This is relative to the initial
        mixing model spacing. Defaults to 1.

        mesh_kwargs (dict, optional): dictionary of key word arguments to customize
        the lines in the 2D mesh. Inherits from matplotlib.pyplot.plot().
        Defaults to {}.

        border_kwargs (dict, optional): dictionary of key word arguments to customize
        the lines for the borders. Inherits from matplotlib.pyplot.plot().
        Defaults to {}.

        ax (matplotlib axis, optional): The matplotlib axis to plot on. If no axis is
        specified it defaults to the current axis. Defaults to None.

    Returns:
        matplotlib axis: matplotlib axis with the mixing model displayed

    """
    if ax is None:
        ax = plt.gca()

    endmembers = [f"{column}" for column in df.columns if "f_" in column]
    for endmember in endmembers:
        for val in df.loc[:, endmembers[0]].unique()[::mesh_every]:
            ax.plot(
                df[df[endmember] == val][x],
                df[df[endmember] == val][y],
                **mesh_kwargs,
                zorder=0,
            )
        ax.plot(
            df.loc[df[endmember] == 0][x],
            df.loc[df[endmember] == 0][y],
            markevery=border_every,
            **border_kwargs,
        )

    ax.set_xlabel(x.replace("_mix", ""))
    ax.set_ylabel(y.replace("_mix", ""))

    return ax
