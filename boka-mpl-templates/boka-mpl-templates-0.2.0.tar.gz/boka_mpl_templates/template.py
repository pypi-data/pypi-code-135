from io import BytesIO
from pathlib import Path
from typing import List, Optional

import matplotlib
import matplotlib.pyplot as plt
import papersize as ps
from PIL import Image

from boka_mpl_templates.footers import FooterBase
from boka_mpl_templates.headers import HeaderBase
from boka_mpl_templates.schemas.template import Margins, Orientation, PaperSize, Space

matplotlib.use("Agg")


class Template:
    def __init__(
        self,
        paper_size: PaperSize = PaperSize.A4,
        orientation: Orientation = Orientation.PORTRAIT,
        margins: Margins = Margins(),
        edge: bool = True,
    ):
        """
        Parameters
        ----------
        paper_size : PaperSize, optional
            The paper size, by default A4
        orientation : Orientation, optional
            The orientation of the paper, by default Portrait
        margins : Margins, optional
            The margins of the paper, by default Margins()
        edge : bool, optional
            Whether to add an edge to the figure, by default True

        Attributes
        ----------
        fig : matplotlib.figure.Figure
            The figure object.
        paper_space : matplotlib.axes.Axes
            The axes object representing the paper space.
        plot_space : matplotlib.axes.Axes
            The axes object representing the plot space. Not implemented yet.
        axes : dict
            A dictionary of axes objects.
        patches : dict
            A dictionary of patch objects.
        text : dict
            A dictionary of text objects.

        """
        if paper_size.lower() not in ps.SIZES.keys():
            raise ValueError(f"Paper size {paper_size} not supported")

        self.paper_size = [float(_) for _ in ps.parse_papersize(paper_size.value, "in")]
        self._paper_width, self._paper_height = [
            int(_) for _ in ps.parse_papersize(paper_size, "mm")
        ]

        if orientation == "landscape":
            # rotate the paper so that it is in landscape mode
            self.paper_size = self.paper_size[::-1]
            self._paper_width, self._paper_height = (
                self._paper_height,
                self._paper_width,
            )

        self.fig = plt.figure(figsize=self.paper_size)
        self.margins = margins

        self.paper_space: plt.Axes = self.fig.add_axes([0, 0, 1, 1])
        self.paper_space.set_xlim([0, self._paper_width])
        self.paper_space.set_ylim([0, self._paper_height])

        for key in self.margins.dict().keys():
            self.paper_space.spines[key].set_visible(False)

        for attr in ["set_xticks", "set_yticks", "set_xlabel", "set_ylabel"]:
            setattr(self.paper_space, attr, [])

        self.axes = dict()
        self.patches = dict()
        self.text = dict()
        self._header: Optional[HeaderBase] = None
        self._footer: Optional[FooterBase] = None

        # add the edge is requested
        if edge:
            self._edge = True
            self._add_edge()

    def add_axes(
        self,
        xmin: int,
        ymin: int,
        width: int,
        height: int,
        ax_name: str = None,
        space: Space = Space.PLOT,
        **kwargs,
    ):
        """Add an axes to the figure.

        Parameters
        ----------
        xmin : int
            The x-coordinate of the lower left corner of the axes in mm.
        ymin : int
            The y-coordinate of the lower left corner of the axes in mm.
        width : int
            The width of the axes in mm.
        height : int
            The height of the axes in mm.
        ax_name : str, optional
            The name of the axes, by default None. If none memory address of the axes is used.
        space : Space, optional
            Whether the axes should be inside the paper space or plot space, by default plot space

        Additional keyword arguments are passed to the `add_axes` method of the figure.

        Returns
        -------
        axes : matplotlib.axes.Axes
            The axes object.

        Raises
        ------
        ValueError
            If the axes are outside the paper.
        """
        normalized_position = self._normalize_position(
            [xmin, ymin, width, height], space=space
        )

        ax = self.fig.add_axes(
            normalized_position,
            **kwargs,
        )

        if ax_name:
            self.axes[ax_name] = ax
        else:
            self.axes[id(ax)] = ax

        return ax

    def add_patch(
        self,
        xmin: int,
        ymin: int,
        width: int,
        height: int,
        patch_name: str = None,
        space: Space = Space.PLOT,
        **kwargs,
    ):
        """
        Add a patch to the figure.

        Parameters
        ----------
        xmin : int
            The x-coordinate of the lower left corner of the patch in mm.
        ymin : int
            The y-coordinate of the lower left corner of the patch in mm.
        width : int
            The width of the patch in mm.
        height : int
            The height of the patch in mm.
        patch_name : str, optional
            The name of the patch, by default None. If none memory address of the patch is used.
        space : Space, optional
            Whether the patch should be inside the paper space or plot space, by default plot space

        Additional keyword arguments are passed to the `add_patch` method of the figure.

        Returns
        -------
        None

        """
        xy = self._patch_xy([xmin, ymin, width, height], space=space)
        patch = self.paper_space.add_patch(plt.Polygon(xy, **kwargs))

        if patch_name:
            self.patches[patch_name] = patch
        else:
            self.patches[id(patch)] = patch

    def add_text(
        self,
        x: int,
        y: int,
        text: str,
        space: Space = Space.PLOT,
        text_name: str = None,
        **kwargs,
    ):
        """
        Add text to the figure.

        Parameters
        ----------
        x : int
            The x-coordinate of the text in mm.
        y : int
            The y-coordinate of the text in mm.
        text : str
            The text to be added.
        space : Space, optional
            Whether the text should be inside the paper space or plot space, by default plot space
        text_name : str, optional
            The name of the text, by default None. If none memory address of the text is used.

        Additional keyword arguments are passed to the `text` method of the figure.

        Returns
        -------
        None

        """
        if space == Space.PAPER:
            t = self.paper_space.text(
                x, y, text, transform=self.paper_space.transData, **kwargs
            )
        elif space == Space.PLOT:
            x = x + self.margins.left
            y = y + self.margins.bottom
            t = self.paper_space.text(
                x, y, text, transform=self.paper_space.transData, **kwargs
            )
        else:
            raise ValueError(f"Space {space} not supported")

        if text_name:
            if text_name in self.text.keys():
                raise ValueError(f"Text name {text_name} already exists")
            self.text[text_name] = t
        else:
            self.text[id(t)] = t

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: HeaderBase):
        if not isinstance(header, HeaderBase):
            raise TypeError(
                f"Header must be an instance of Header, but {type(header)} was given"
            )
        self._header = header
        self._header.add_to_template(template=self)

        # find existing header and remove it
        for patch in self.paper_space.patches:
            if patch.get_label() == "header":
                patch.remove()

        self._header.add_to_template(template=self)

    @property
    def footer(self, *args, **kwargs):
        return self._footer

    @footer.setter
    def footer(self, footer: FooterBase):
        if not isinstance(footer, FooterBase):
            raise TypeError(
                f"Footer must be an instance of Footer, but {type(footer)} was given"
            )
        self._footer = footer

        # find old footer and remove it
        for patch in self.paper_space.patches:
            if patch.get_label() == "footer":
                patch.remove()

        self._footer.add_to_template(template=self)

    def export(self, filepath: Path, rasterize: bool = False, dpi: int = 300, **kwargs):
        """
        Export the figure to a file.
        The figure can optionally be rasterized. This can be useful if the figure contains a lot of data and
        thus becomes very large.

        Parameters
        ----------
        filepath : Path
            The path to the file.
        rasterize : bool, optional
            Whether to rasterize the figure, by default False
        dpi : int, optional
            The dpi of the figure when rasterized, by default 300

        Additional keyword arguments are passed to the `savefig` method of the figure.

        Returns
        -------
        None

        """
        if rasterize:
            dest = BytesIO()
            self.fig.savefig(dest, format="png", dpi=dpi)

            dest.seek(0)

            image_1 = Image.open(dest)
            im_1 = image_1.convert("RGB")
            im_1.save(filepath, resolution=dpi)
        else:
            self.fig.savefig(filepath, **kwargs)

    def _normalize_position(self, position: List[int], space: Space = Space.PLOT):
        """Normalize the position of an axes to the paper size.

        Parameters
        ----------
        position : List[int]
            The position of the axes in mm.
        inside_margins : bool, optional
            Whether the axes should be inside the margins, by default True

        Returns
        -------
        normalized_position : List[float]
            The normalized position of the axes.
        """
        if space == Space.PLOT:
            normalized_position = [
                (position[0] + self.margins.left) / self._paper_width,
                (position[1] + self.margins.bottom) / self._paper_height,
                position[2] / self._paper_width,
                position[3] / self._paper_height,
            ]
        elif space == Space.PAPER:
            normalized_position = [
                position[0] / self._paper_width,
                position[1] / self._paper_height,
                position[2] / self._paper_width,
                position[3] / self._paper_height,
            ]
        else:
            raise ValueError(f"Space {space} not supported")

        if any(
            [
                normalized_position[0] < 0,
                normalized_position[1] < 0,
                normalized_position[0] + normalized_position[2] > 1,
                normalized_position[1] + normalized_position[3] > 1,
            ]
        ):
            raise ValueError(
                f"The position of the axes is outside the paper, {normalized_position}."
            )

        return normalized_position

    def _patch_xy(self, position: List[int], space: Space = Space.PLOT):
        """Convert the position of a patch to the paper size.

        Parameters
        ----------
        position : List[int]
            The position of the patch in mm.
            position[0] is the x-coordinate of the lower left corner of the patch.
            position[1] is the y-coordinate of the lower left corner of the patch.
            position[2] is the width of the patch.
            position[3] is the height of the patch.
        inside_margins : bool, optional
            Whether the patch should be inside the margins, by default True

        Returns
        -------
        xy : List[float]
            The normalized position of the patch. List contains 4 points, each point is a tuple of x and y coordinates.
             Postion 0 is the lower left corner of the patch. See figure below or positions in xy list.

             [3]-------------------[2]
              |         Patch       |
              |                     |
             [0]-------------------[1]

        Raises
        ------
        ValueError
            If the position of the patch is outside the paper or if a invalid space is given.

        """
        x_min, x_max = position[0], position[0] + position[2]
        y_min, y_max = position[1], position[1] + position[3]

        if space == Space.PLOT:
            xy = [
                [self.margins.left + x_min, self.margins.bottom + y_min],
                [self.margins.left + x_max, self.margins.bottom + y_min],
                [self.margins.left + x_max, self.margins.bottom + y_max],
                [self.margins.left + x_min, self.margins.bottom + y_max],
            ]

            # Check if the patch is outside the plotting space
            if any(
                [
                    xy[0][0] < self.margins.left,
                    xy[0][1] < self.margins.bottom,
                    xy[1][0] > (self._paper_width - self.margins.right),
                    xy[0][1] > (self._paper_height - self.margins.top),
                ]
            ):
                raise ValueError(
                    f"""The position of the patch is outside the plotting space, {xy}.
                    {xy[0][0]} < {self.margins.left},
                    {xy[0][1]} < {self.margins.bottom},
                    {xy[1][0]} > {(self._paper_width - self.margins.right)},
                    {xy[0][1]} > {(self._paper_height - self.margins.top)}
                    """
                )
        elif space == Space.PAPER:
            xy = [
                [x_min, y_min],
                [x_max, y_min],
                [x_max, y_max],
                [x_min, y_max],
            ]
            # Check if the patch is outside the plotting space
            if any(
                [
                    xy[0][0] < 0,
                    xy[0][1] < 0,
                    xy[1][0] > self._paper_width,
                    xy[0][1] > self._paper_height,
                ]
            ):
                raise ValueError(
                    f"The position of the patch is outside the paper, {xy}."
                )
        else:
            raise ValueError(f"Invalid space {space}.")

        return xy

    def _add_edge(self):
        """Add an edge to the figure.

        Returns
        -------
        None

        """
        position = [
            self.margins.left,
            self.margins.bottom,
            self._paper_width - self.margins.left - self.margins.right,
            self._paper_height - self.margins.bottom - self.margins.top,
        ]
        self.add_patch(
            *position,
            patch_name="edge",
            space=Space.PAPER,
            edgecolor="black",
            facecolor="none",
        )
