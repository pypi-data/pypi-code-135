from functools import reduce
from typing import List, Optional

import markdown
from pymdownx.arithmatex import arithmatex_fenced_format, arithmatex_inline_format
from pymdownx.highlight import HighlightExtension
from pymdownx.superfences import SuperFencesCodeExtension
from pymdownx.inlinehilite import InlineHiliteExtension
from markdown.extensions.def_list import DefListExtension
from markdown.extensions.footnotes import FootnoteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.meta import MetaExtension
from notes_compiler.tree_node import MarkdownTreeNode
from notes_compiler.utils import snake_case_to_title_case


class HtmlPage:
    def __init__(
        self,
        parent: MarkdownTreeNode,
        body: str = "",
        css: Optional[List[str]] = None,
        scripts: Optional[List[str]] = None,
        name: str = "",
    ):
        self.parent = parent
        self.body: str = body
        self.css: List[str] = css.copy() if css else []
        self.scripts: List[str] = scripts.copy() if scripts else []
        self.name: str = name
        self.prefix: List[str] = []
        self.page_before: Optional[HtmlPage] = None
        self.page_after: Optional[HtmlPage] = None

    @staticmethod
    def from_markdown(md: str, **kwargs):
        html = HtmlPage._compile_markdown(md)
        return HtmlPage(body=html, **kwargs)

    @staticmethod
    def _compile_markdown(md: str) -> str:
        return markdown.markdown(
            md,
            tab_length=2,
            extensions=[
                DefListExtension(),
                FootnoteExtension(),
                TableExtension(),
                TocExtension(),
                MetaExtension(),
                HighlightExtension(),
                SuperFencesCodeExtension(
                    custom_fences=[
                        {
                            "name": "math",
                            "class": "arithmatex",
                            "format": arithmatex_fenced_format(which="generic"),
                        }
                    ]
                ),
                InlineHiliteExtension(
                    custom_inline=[
                        {
                            "name": "math",
                            "class": "arithmatex",
                            "format": arithmatex_inline_format(which="generic"),
                        }
                    ]
                ),
                "python3_markdown_extension_graphviz",
            ],
        )

    def build_page(self) -> str:
        return f"""
<html>
    <head>
        {reduce(lambda a,b: f'{a} {b}', (self.get_css_link(css) for css in self.css), '')}
    </head>

    <body>
        {reduce(lambda a,b: f'{a} {b}', (self.get_script_link(script) for script in self.scripts), '')}
        <header>
        {self._get_header()}
        </header>
        {self.body}
        <footer>
        {self._get_header()}
        </footer>
    </body>
</html>
"""

    def _get_link_to_page(self, page: "HtmlPage") -> str:
        return f"{self.parent.path_to_root()}/{page.parent.path_from_root()}/{page.name}.html"

    def _get_header(self):
        node = self.parent
        linked_index = None
        if self.name == "index":
            node = node.parent
        while node is not None and linked_index is None:
            linked_index = node.content["index"]
            node = node.parent
        return f"""
            {f'<a class="link-before" href={self._get_link_to_page(self.page_before)}><small>&#9664; {snake_case_to_title_case(self.page_before.name)}</small></a>' if self.page_before else '<div class="link-before"></div>'}
            {f'<a class="link-index" href={self._get_link_to_page(linked_index["page"])}><small>To Index</small></a>' if linked_index else '<div class="link-index"></div>'}
            {f'<a class="link-after" href={self._get_link_to_page(self.page_after)}><small>{snake_case_to_title_case(self.page_after.name)} &#9654;</small></a>' if self.page_after else '<div class="link-after"></div>'}
"""

    def get_css_link(self, css: str) -> str:
        return f'<link rel="stylesheet" type="text/css" href="{self.parent.path_to_root()}/{css}"/>'

    def get_script_link(self, script: str) -> str:
        return f'<script src="{script}"></script>'
