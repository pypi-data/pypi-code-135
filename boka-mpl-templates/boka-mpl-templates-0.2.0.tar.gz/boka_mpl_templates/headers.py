from abc import ABC, abstractmethod
from typing import Optional

from boka_mpl_templates.schemas.template import Space


class HeaderBase(ABC):
    def __init__(
        self,
        height=35,
        title_height=10,
        spacing_header_title=1,
    ):
        """
        Parameters
        ----------
        height : float
            Height of the header in mm
        title_height : float
            Height of the title in mm
        spacing_header_title : float
            Spacing between the header and the title in mm

        """
        self.height = height
        self.title_height = title_height
        self.spacing_header_title = spacing_header_title

    @abstractmethod
    def add_to_template(self, template: "Template"):
        """
        Add the header to the template

        Parameters
        ----------
        template : Template
            The template to add the header to
        """
        return NotImplemented


class Header(HeaderBase):
    def __init__(
        self,
        title: str,
        subtitle: str,
        height=35,
        title_height=10,
        title_width=50,
        title_fontsize=10,
        spacing_header_title=1,
        header_shading="lightgray",
    ):
        super().__init__(
            height=height,
            title_height=title_height,
            spacing_header_title=spacing_header_title,
        )
        self.title = title
        self.subtitle = subtitle
        self.template: Optional["Template"] = None
        self.title_width = title_width
        self.title_fontsize = title_fontsize
        self.header_shading = header_shading

    def add_to_template(self, template: "Template"):
        """
        Add the header to the template

        Parameters
        ----------
        template : Template
            The template to add the header to
        """
        self.template = template
        xy = self.determine_xy()
        self.template.add_patch(
            *xy,
            patch_name="header",
            space=Space.PAPER,
            facecolor=self.header_shading,
            edgecolor="black",
            zorder=-1,
        )

        # Add title patch
        xy_title = [
            self.template._paper_width - self.template.margins.right - self.title_width,
            self.template._paper_height - self.template.margins.top - self.title_height,
            self.title_width,
            self.title_height,
        ]

        self.template.add_patch(
            *xy_title,
            patch_name="header_title",
            space=Space.PAPER,
            facecolor="none",
            edgecolor="black",
        )

        xy_text = [
            self.template._paper_width
            - self.template.margins.right
            - self.spacing_header_title,
            self.template._paper_height
            - self.template.margins.top
            - self.title_height
            + self.spacing_header_title,
        ]

        # plot title
        self.template.add_text(
            *xy_text,
            self.title,
            fontsize=self.title_fontsize,
            space=Space.PAPER,
            ha="right",
            va="bottom",
        )

        xy_pointid_label = [
            self.template._paper_width
            - self.template.margins.right
            - self.title_width
            + 1,
            self.template._paper_height - self.template.margins.top - 1,
        ]

        # plot pointid label
        self.template.add_text(
            *xy_pointid_label,
            "pointid",
            fontsize=8,
            space=Space.PAPER,
            ha="left",
            va="top",
        )

    def determine_xy(self):
        if self.template is None:
            raise ValueError("Template not set")

        xmin = self.template.margins.left
        xmax = self.template._paper_width - self.template.margins.right
        ymin = self.template._paper_height - self.height - self.template.margins.top
        ymax = self.template._paper_height - self.template.margins.top

        return [xmin, ymin, xmax - xmin, ymax - ymin]


class CptA4Header(HeaderBase):
    def __init__(
        self,
        title: str,
        subtitle: str,
        height=35,
        title_height=10,
        spacing_header_title=1,
    ):
        super().__init__(
            height=height,
            title_height=title_height,
            spacing_header_title=spacing_header_title,
        )
        self.title = title
        self.subtitle = subtitle

    def add_to_template(self, template: "Template"):
        template
