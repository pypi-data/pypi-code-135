from __future__ import annotations

from sys import stderr, stdout

import bs4
import defopt
import httpx

from .intersphinx import fetch_inv
from .web_parsing import slurp

__all__ = ["lookup_docs", "list_entities", "cli"]


def announce(what, quiet, where=stdout):
    if not quiet:
        print(what, file=where)


def lookup_docs(url_base, inv_objects, debug: bool = False, quiet: bool = False):
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
                announce(what=obj, quiet=quiet)
            r = client.get(url_head)
            print(f"\nFetched {url_head}")
            docs = slurp(content=r.content, doc_id=doc_id)
    return docs


def fetch_entities(
    package_name: str = "pandas",
    *,
    version: str = "",
    debug: bool = False,
    fetch: bool = True,
    quiet: bool = False,
) -> None:
    announce(f"qp ⠶ {package_name=} & {version=}", quiet=quiet, where=stderr)
    url_base, inv = fetch_inv(package=package_name, version=version)
    py_objects = [o for o in inv.objects if o.domain == "py"]
    announce(
        what=f"Fetched {len(py_objects)} :py: domain objects from {url_base}",
        quiet=quiet,
        where=stderr,
    )
    if fetch:
        lookup_docs(url_base=url_base, inv_objects=py_objects, debug=debug)
    else:
        for obj in py_objects:
            if debug:
                breakpoint()
            else:
                announce(what=f"{obj.name} {url_base}{obj.uri_expanded}", quiet=False)


def cli():
    defopt.run(fetch_entities)
