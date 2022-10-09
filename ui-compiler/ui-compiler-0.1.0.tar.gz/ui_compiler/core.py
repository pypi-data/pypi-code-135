import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Sequence, Set

from dominate import document
from dominate import tags as d
from dynamic_imports import class_impl_from_module
from ready_logger import logger

from .. import components
from .css import get_css
from .js import get_js


@dataclass
class WebPage:
    html: document
    js_files: Set[Path] = field(default_factory=set)
    js_urls: Set[str] = field(default_factory=set)
    global_js_vars: Dict[str, Any] = field(default_factory=dict)
    css_files: Set[Path] = field(default_factory=set)
    css_urls: Set[str] = field(default_factory=set)
    preconnect_urls: Set[str] = field(default_factory=set)

    def __post_init__(self):
        # add URLs that are required on each page.
        self.css_urls.update(
            [
                "https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
            ]
        )
        self.preconnect_urls.update(
            [
                "https://fonts.googleapis.com",
                "https://fonts.gstatic.com",
            ]
        )


def compile_web_pages(
    pages: Sequence[WebPage],
    output_dir: Path,
    pretty: bool = True,
):
    if isinstance(pages, WebPage):
        pages = [pages]

    # map component name to component class.
    component_impls = {
        t.__name__: t
        for t in class_impl_from_module(
            base_class=components.component,
            module=components,
        )
    }
    components_re = re.compile(
        f'data-component="(' + "|".join(component_impls.keys()) + ')"'
    )
    js_file = output_dir.joinpath("main.js")
    css_file = output_dir.joinpath("main.css")

    docs_html = []
    global_js_vars = {}
    js_files, css_files = set(), set()
    for p in pages:
        global_js_vars.update(p.global_js_vars)
        js_files.update(p.js_files)
        css_files.update(p.css_files)
        docs_html.append(doc_html := p.html.render())
        present_components = {m.group(1) for m in components_re.finditer(doc_html)}
        logger.info(
            f"Found {len(present_components)} component(s) in document {p.html.title}: {present_components}"
        )
        present_components = {component_impls[c] for c in present_components}
        # page can have external URLs
        css_urls = p.css_urls.copy()
        js_urls = p.js_files.copy()
        preconnect_urls = p.preconnect_urls.copy()
        for c in present_components:
            # components within the page can have their own external URLs.
            css_urls.update(c.css_urls)
            css_urls.add(str(css_file))
            js_urls.update(c.js_urls)
            js_urls.add(str(js_file))
            preconnect_urls.update(c.preconnect_urls)
        with p.html.head:
            for url in preconnect_urls:
                d.link(rel="preconnect", href=url)
            for url in css_urls:
                d.link(
                    rel="stylesheet",
                    href=url,
                )
            for url in js_urls:
                d.script(type="text/javascript", src=url)

    html_dir = output_dir.joinpath("html")
    html_dir.mkdir(parents=True, exist_ok=True)

    for p in pages:
        title = re.sub(r"\s+", "_", p.html.title.lower())
        file = html_dir.joinpath(f"{title}.html")
        logger.info(f"Writing HTML: {file}")
        file.write_text(p.html.render())

    js = get_js(
        docs_html=docs_html,
        required_js=js_files,
        # check for components JS that should be added.
        check_js=list(Path(__file__).parent.joinpath("js").glob("*.js")),
        global_js_vars=global_js_vars,
        pretty=pretty,
    )

    logger.info(f"Writing JS: {js_file}")
    js_file.write_text(js)

    css = get_css(
        docs_html=docs_html, js_files=js_files, css_files=css_files, pretty=pretty
    )
    logger.info(f"Writing CSS: {js_file}")
    css_file.write_text(css)
