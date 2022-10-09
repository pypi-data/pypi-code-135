from __future__ import annotations

from sys import stderr

import bs4
import defopt
import httpx

from .intersphinx import fetch_inv

__all__ = ["lookup_docs", "list_entities", "cli"]

bs = bs4.BeautifulSoup()


def lookup_docs(url_base, inv_objects, debug: bool = False):
    docs = []
    with httpx.Client() as client:
        for obj in inv_objects:
            url = url_base + obj.uri_expanded
            url_head, _, doc_id = url.rpartition("#")
            r = client.get(url)
            # TODO: parse soup
            if debug:
                breakpoint()
            else:
                print(obj)
    return docs


def fetch_entities(
    package_name: str = "pandas",
    *,
    version: str = "",
    debug: bool = False,
    fetch: bool = True,
) -> None:
    print(f"qp ⠶ {package_name=} & {version=}", file=stderr)
    url_base, inv = fetch_inv(package=package_name, version=version)
    py_objects = [o for o in inv.objects if o.domain == "py"]
    print(f"Fetched {len(py_objects)} :py: domain objects from {url_base}", file=stderr)
    if fetch:
        lookup_docs(url_base=url_base, inv_objects=py_objects, debug=debug)
    else:
        if debug:
            breakpoint()
        else:
            for obj in py_objects:
                print(f"{obj.name} {url_base}{obj.uri_expanded}")


def cli():
    defopt.run(fetch_entities)
