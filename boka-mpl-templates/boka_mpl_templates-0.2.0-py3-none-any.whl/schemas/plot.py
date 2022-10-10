from typing import Any, Dict, List, Literal, Optional, Union

import numpy as np
from papersize import SIZES
from pydantic import BaseModel, Field, FilePath, validator, root_validator
from pydantic.color import Color

from boka_mpl_templates import PaperSize, Margins


def _convert_color(color: Color) -> str:
    """Convert color to hex string."""
    if isinstance(color, Color):
        return color.as_hex()
    else:
        return color


class LineKwargs(BaseModel):
    """Line plot kwargs."""
    label: str = Field(..., description="Label to appear in legend")
    color: Color = Field("black", description="Line color")
    linestyle: Literal[
        "-", "--", "-.", ":", " ", "", "solid", "dashed", "dashdot", "dotted"
    ] = Field("-", description="Line style of plot")
    linewidth: float = Field(0.8, lt=5.0, gt=0.1, description="Line width of plot")
    marker: Optional[Literal[
        ".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P",
        ]] = Field(None, description="Marker style of plot")
    markersize: float = Field(6.0, lt=10.0, gt=0.1, description="Marker size of plot")
    markerfacecolor: Color = Field("black", description="Marker face color")
    markeredgecolor: Color = Field("black", description="Marker edge color")
    markeredgewidth: float = Field(1.0, lt=5.0, gt=0.1, description="Marker edge width")
    alpha: float = Field(1.0, lt=1.0, gt=0.0, description="Alpha value")
    zorder: int = Field(1, description="Zorder of plot")

    _normalize_color = validator("color", allow_reuse=True)(_convert_color)


class ScatterKwargs(BaseModel):
    """Scatter plot kwargs."""
    label: str = Field(..., description="Label to appear in legend")
    color: Union[
        Color, List[Union[float, None]]
    ] = "black"
    cmap: Any = None
    norm: Any = None
    edgecolor: Color = None  # Field("black", description="Edge color of marker")
    edgewidth: float = Field(None, lt=5.0, gt=0.1, description="Edge width of marker")
    size: int = Field(100, gt=1, lt=150, description="Marker size")
    marker: Literal["^", "v", "<", ">", "o", "x"] = None

    _normalize_c = validator("color", allow_reuse=True)(_convert_color)
    _normalize_edgecolor = validator("edgecolor", allow_reuse=True)(_convert_color)


class BarKwargs(BaseModel):
    """Bar plot kwargs."""
    label: str = Field(..., description="Label to appear in legend")
    width: Optional[float] = Field(0.5, gt=0.1, lt=2, description="Width of bar")
    bottom: List[float] = Field(
        ..., description="List to indicate y position of bottom bar"
    )
    color: List[str] = Field(..., description="List of bar colors")
    hatch: Optional[Literal["...", "..", "\\", "/"]] = Field(
        None, description="Hatch style"
    )
    # _normalize_color = validator("color", allow_reuse=True)(_convert_color)


class TextKwargs(BaseModel):
    """Text plot kwargs."""
    text_name: str = Field(None, description="Label to appear in legend")
    color: Color = Field("black", description="Text color")
    fontsize: int = Field(12, description="Font size of text")
    fontweight: Literal["normal", "bold"] = Field("normal", description="Font weight")
    fontstyle: Literal["normal", "italic"] = Field("normal", description="Font style")
    rotation: int = Field(0, description="Rotation of text")
    horizontalalignment: Literal[
        "center", "right", "left"
    ] = Field("center", description="Horizontal alignment of text")
    verticalalignment: Literal[
        "center", "top", "bottom", "baseline"
    ] = Field("center", description="Vertical alignment of text")

    _normalize_color = validator("color", allow_reuse=True)(_convert_color)


class AxKwargs(BaseModel):
    """Axes kwargs."""
    xlim: Optional[List[float]]
    xlabel: Optional[str]
    ylim: Optional[List[float]]
    ylabel: Optional[str]
    xticks: Optional[List[float]]
    yticks: Optional[List[float]]
    xticklabels: Optional[List[str]]
    yticklabels: Optional[List[str]]


class LegendKwargs:
    pass


class Plot(BaseModel):
    """Plot schema."""
    ax: str
    plot_name: str
    type: Literal["plot", "scatter", "axvline", "axhline", "bar"] = "plot"
    x_data: List[float] = None
    y_data: List[float] = None
    args: List[List[Union[float, None]]] = None
    kwargs: Optional[Union[LineKwargs, ScatterKwargs, BarKwargs]]


class PlotContainer(BaseModel):
    """Plot container schema."""
    shared_y_data: List[float]
    plots: List[Plot]


class Twiny(BaseModel):
    """Twiny schema."""
    twin: str
    kwargs: AxKwargs


class Axes(BaseModel):
    """Axes schema."""
    widths: List[float]
    kwargs: Dict[str, AxKwargs]
    twiny: Optional[Dict[str, Twiny]]

    @property
    def num(self):
        return len(self.widths)

    @validator("widths")
    def validate_widths(cls, v):
        assert sum(v) == 1.0, "sum of all widths must be 1"
        return v


class Layout(BaseModel):
    papersize: PaperSize = PaperSize.A4
    margins: Margins = Margins()
    logo: Optional[FilePath]


class HeaderRowData(BaseModel):
    """Header row data schema."""
    title: str
    value: str
    unit: Optional[str]
    seperator: Optional[str] = Field(":", description="Seperator between title and value")
    text_kwargs: TextKwargs = TextKwargs()


class HeaderData(BaseModel):
    """Header data schema."""
    pointid: str
    row_spacing: float = 5.0
    general_titles: List[str] = ["CLIENT", "ENGINEER", "AC", "CONTRACTOR", "PROJECT"]
    general_values: List[str] = ["", "", "", "", ""]
    location_titles: List[str] = ["AREA", "SUBAREA", "EASTING", "NORTHING", "ELEVATION"]
    location_values: List[str] = ["", "", "", "", ""]
    location_units: List[str] = ["", "", "m", "m", "m+MSL"]
    version_titles: List[str] = [
        "CPT DATE",
        "PRINT DATE",
        "PREPARED BY",
        "CHECKED BY",
        "APPROVED BY",
    ]
    version_values: List[str] = ["", "", "", "", ""]


class PlotProps(BaseModel):
    """
    Plot properties schema.

    This schema is used to define the properties of the plots to be generated.
    """
    plots: PlotContainer
    axes: Axes
    layout: Layout
    info: HeaderData
