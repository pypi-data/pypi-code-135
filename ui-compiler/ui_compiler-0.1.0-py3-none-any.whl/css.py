import re
from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Sequence, Set

from lxml.html import fromstring

from .common import logger


@lru_cache(maxsize=100)
def read_css_file(file: Path):
    """read file and remove comments."""
    logger.info(f"Loading CSS file: {file}")
    return re.sub(r"/\*(.|\n)*\*/", "", file.read_text())


@dataclass
class SelectorProps:
    """CSS selectors for CSS properties."""

    # the selector(s) that `properties` should be applied to.
    selectors: Set[str] = field(default_factory=set)
    # the properties to apply.
    properties: Dict[str, str] = field(default_factory=dict)

    def add_property(self, name: str, value: str):
        if name in self.properties and self.properties[name] != value:
            raise RuntimeError(
                f"Property `{name}` already exists with value `{self.properties[name]}`. Can not set value to `{value}`"
            )
        self.properties[name] = value

    def add_properties(self, props: Dict[str, str]):
        for n, v in props.items():
            self.add_property(n, v)


def load_css_files(files: Sequence[Path]) -> List[SelectorProps]:
    """Read a CSS file from disk and extract the selectors and properties."""
    if isinstance(files, Path):
        files = [files]
    selector_properties = defaultdict(SelectorProps)
    for file in files:
        text = read_css_file(file)
        # find each selector + corresponding css text block.
        for match in re.finditer(
            r"([-#*>~|$,.\s\w:=[\]()]+?){((?:\s*[a-z-]+:[-.,\s\w%#()]+;\s*)+)}", text
        ):
            selectors, css = match.group(1).strip(), match.group(2).strip()
            selectors = [s.strip() for s in selectors.split(",")]
            # find all properties and values for this selector(s)
            for match in re.finditer(r"(\s*[a-z-]+):([-.,\s\w%#()]+;)", css):
                name, value = match.group(1).strip(), match.group(2).strip()
                for selector in selectors:
                    selector_properties[selector].add_property(name, value)
    # check if multiple selectors have the same properties/values.
    selector_merger = defaultdict(SelectorProps)
    for selector, properties in selector_properties.items():
        # make sure fields are ordered consistently.
        style_id = tuple(sorted(properties.items(), key=lambda x: x[0]))
        selector_merger[style_id].selectors.add(selector)
        selector_merger[style_id].add_properties(properties)
    return list(selector_merger.values())


def filter_selector_properties(
    docs_html: Sequence[str],
    docs_js: Sequence[str],
    selector_properties: Sequence[SelectorProps],
) -> List[SelectorProps]:
    """Remove any unused CSS."""
    doc_trees = [fromstring(html) for html in docs_html]
    # parse document and determine what styles need to be added.
    base_selectors_used = {}
    selector_props_used = []
    for selector_props in selector_properties:
        matched_selectors = set()
        for selector in selector_props.selectors:
            # clean selectors to base form. no pseudo-elements etc..
            base_selector = re.sub(
                r"(?<=[a-zA-Z])((\.|:|::).*?(?=(\s|$)))", "", selector
            )
            if (is_used := base_selectors_used.get(base_selector)) is None:
                js_reg = "".join(
                    [
                        r"classList\.(add|toggle)\('",
                        re.escape(base_selector.lstrip(".")),
                        r"'\)",
                    ]
                )
                base_selectors_used[base_selector] = is_used = (
                    # check for elements at selector paths.
                    any(tree.cssselect(base_selector) for tree in doc_trees)
                    # check for classes used in JavaScript.
                    or any(re.search(js_reg, html) for html in docs_html)
                    or any(re.search(js_reg, js) for js in docs_js)
                )
            if is_used:
                matched_selectors.add(selector)
        if matched_selectors:
            selector_props.selectors = matched_selectors
            selector_props_used.append(selector_props)

    logger.info(f"Found {len(selector_props_used)} used CSS selector properties.")
    return selector_props_used


def make_pretty_css(selector_properties: Sequence[SelectorProps]) -> str:
    pretty_css = []
    for sp in selector_properties:
        selectors = ",\n".join(sp.selectors)
        properties = "\n\t".join([f"{p}: {v}" for p, v in sp.properties.items()])
        pretty_css.append(f"{selectors} {{\n\t{properties}\n}}")
    return "\n\n".join(pretty_css)


def make_min_css(selector_properties: Sequence[SelectorProps]) -> str:
    min_css = ""
    for sp in selector_properties:
        selectors = ",".join(sp.selectors)
        properties = "".join([f"{p}:{v}" for p, v in sp.properties.items()])
        min_css += f"{selectors} {{{properties}}}"
    return min_css


def get_css(
    docs_html: Sequence[str],
    js_files: Sequence[str],
    css_files: Sequence[Path],
    pretty: bool = True,
) -> str:
    """Generate a single CSS file for a website.

    Args:
        docs_html (Sequence[str]): The HTML pages of the site.
        js_files (Sequence[str]): JS files needed for the site.
        css_files (Sequence[Path]): CSS files needed for the site.
        pretty (bool, optional): Write the CSS in an easily-readable format. Defaults to True.

    Returns:
        str: The CSS file content.
    """
    selector_properties = load_css_files(css_files)
    docs_js = [Path(f).read_text() for f in js_files]
    selector_properties = filter_selector_properties(
        docs_html,
        docs_js,
        selector_properties,
    )
    if pretty:
        return make_pretty_css(selector_properties)
    return make_min_css(selector_properties)
