from enum import Enum

from pydantic import BaseModel


class Margins(BaseModel):
    """
    Margins for the plot in cm.
    """

    top: int = 10
    bottom: int = 10
    left: int = 10
    right: int = 10


class Orientation(str, Enum):
    """
    Orientation of the plot.
    """

    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"


class Space(str, Enum):
    """
    Referenced space in the figure.
    """

    PAPER = "paper"
    PLOT = "plot"


class PaperSize(str, Enum):
    """
    Paper size for the plot.
    """

    A0 = "a0"
    A1 = "a1"
    A2 = "a2"
    A3 = "a3"
    A4 = "a4"
    A5 = "a5"
    B0 = "b0"
    B1 = "b1"
    B2 = "b2"
    B3 = "b3"
    B4 = "b4"
    B5 = "b5"
    LETTER = "letter"
    LEGAL = "legal"
