from typing import Union, Tuple

import matplotlib.pyplot as plt


def fig_to_ax(fig, ax, coords):
    """
    Convert coordinates from figure to axis.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure
    ax : matplotlib.axes.Axes
        The axis
    coords : tuple
        The coordinates to convert

    Returns
    -------
    tuple
        The converted coordinates
    """
    display_coords = fig.transFigure.transform(coords)
    inv = ax.transAxes.inverted()
    return inv.transform(display_coords)


def ax_to_fig(fig, ax, coords):
    """
    Convert coordinates from axis to figure.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure
    ax : matplotlib.axes.Axes
        The axis
    coords : tuple
        The coordinates to convert

    Returns
    -------
    tuple
        The converted coordinates
    """
    display_coords = ax.transAxes.transform(coords)
    inv = fig.transFigure.inverted()
    return inv.transform(display_coords)


def cm2inch(cm: Union[float, Tuple[float]]) -> Union[float, Tuple[float]]:
    """
    Convert centimeters to inches.

    Parameters
    ----------
    cm : float or tuple
        The centimeters to convert

    Returns
    -------
    float or tuple
        The converted inches or tuple of converted inches
    """
    inch = 2.54
    if isinstance(cm, tuple):
        return tuple(i / inch for i in cm)
    else:
        return cm / inch
