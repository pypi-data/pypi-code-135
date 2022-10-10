from abc import ABC, abstractmethod
from typing import Optional


class FooterBase(ABC):
    def __init__(
        self,
        height=1.5,
        spacing_footer_title=0.1,
    ):
        self.height = height
        self.spacing_footer_title = spacing_footer_title

    @abstractmethod
    def add_to_template(self, template: "Template"):
        return NotImplemented()


class Footer(FooterBase):
    def __init__(
        self,
        title: str,
        height=1.5,
        spacing_footer_title=0.1,
    ):
        super().__init__(
            height=height,
            spacing_footer_title=spacing_footer_title,
        )
        self.title = title
        self.template: Optional["Template"] = None

    def add_to_template(self, template: "Template"):
        self.template = template
        xy = self.determine_xy()
        self.template.add_patch(*xy, patch_name="footer")

    def determine_xy(self):
        if self.template is None:
            raise ValueError("Template not set")

        xmin = self.template.margins.left
        xmax = self.template._paper_width - self.template.margins.right
        ymin = self.template.margins.bottom
        ymax = self.template.margins.bottom + self.height

        return [xmin, ymin, xmax - xmin, ymax - ymin]
