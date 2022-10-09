import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

from .common import logger


@dataclass
class JSFunc:
    file: Path
    file_content: str
    func_pattern: re.Pattern


@lru_cache(maxsize=100)
def load_js_file(file: Path) -> List[JSFunc]:
    logger.info(f"Loading JS file: {file}")
    file_content = file.read_text().strip()
    func_names = [
        m.group(1) for m in re.finditer(r"(?:^|\s|\n)function (\w+)", file_content)
    ]
    func_matchers = [re.compile(r"""(^|[='"\s\n(])""" + n + r"\(") for n in func_names]
    return [JSFunc(file.name, file_content, m) for m in func_matchers]


def load_js_files(files: Sequence[Path]) -> List[JSFunc]:
    """Map function name to JS file."""
    js_func_meta = []
    for f in files:
        js_func_meta += load_js_file(f)
    return js_func_meta


def make_pretty_js(
    meta: Sequence[JSFunc], global_js_vars: Optional[Dict[str, Any]] = None
):
    js = "\n\n".join([f.file_content for f in meta])
    if global_js_vars:
        global_js_vars = {
            k: f"'{v}'" if isinstance(v, str) else v for k, v in global_js_vars.items()
        }
        global_vars = "\n".join([f"var {k}={v};" for k, v in global_js_vars.items()])
        js = f"{global_vars}\n{js}"
    return js


def make_min_js(
    meta: Sequence[JSFunc], global_js_vars: Optional[Dict[str, Any]] = None
):
    pass


def get_js(
    docs_html: Sequence[str],
    required_js: Optional[Sequence[Path]] = None,
    check_js: Optional[Sequence[Path]] = None,
    global_js_vars: Optional[Dict[str, Any]] = None,
    pretty: bool = True,
) -> str:
    files = {}
    if required_js:
        files.update({f.file: f for f in load_js_files(required_js)})
    elif not check_js:
        logger.error("Either `required_js` or `check_js` must be provided.")
        return ""
    if not isinstance(docs_html, (list, tuple, set)):
        docs_html = [docs_html]
    if not isinstance(check_js, (list, tuple, set)):
        check_js = [check_js]

    check_js = load_js_files(check_js)
    # find files with JS functions that were used.
    files.update(
        {
            f.file: f
            for f in check_js
            if any(f.func_pattern.search(html) for html in docs_html)
            or any(f.func_pattern.search(s.file_content) for s in files.values())
        }
    )
    while True:
        # find file interdependencies.
        deps = {}
        for f in check_js:
            if f.file not in files and any(
                s.func_pattern.search(f.file_content) for s in files.values()
            ):
                deps[f.file] = f
        if deps:
            files.update(deps)
        else:
            break
    logger.info(f"Found {len(files)} required JS files: {list(files.keys())}")
    if pretty:
        return make_pretty_js(files.values(), global_js_vars)
    return make_min_js(files.value(), global_js_vars)
