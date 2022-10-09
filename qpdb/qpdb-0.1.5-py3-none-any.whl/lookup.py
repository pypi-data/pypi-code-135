from __future__ import annotations

import re
from sys import stderr, stdout

import defopt
import httpx

from .intersphinx import fetch_inv
from .web_parsing import slurp

__all__ = ["announce", "lookup_docs", "fetch_entities", "cli"]


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
    package: str = "pandas",
    *,
    version: str = "",
    domain: str = "py",
    role: str = "",
    names: str = "",
    debug: bool = False,
    crawl: bool = False,
    quiet: bool = False,
) -> None:
    announce(f"qp ⠶ {package=} & {version=}", quiet=quiet, where=stderr)
    url_base, inv = fetch_inv(package=package, version=version)
    check_domain = domain != ""
    check_role = role != ""
    check_name = names != ""
    names_pat = re.compile(pattern=names)
    py_objects = [
        o
        for o in inv.objects
        if not check_domain or (check_domain and o.domain == domain)
        if not check_role or (check_role and o.role == role)
        if not check_name or (check_name and names_pat.search(o.name))
    ]
    announce(
        what=f"Fetched {len(py_objects)} :py: domain objects from {url_base}",
        quiet=quiet,
        where=stderr,
    )
    if crawl:
        lookup_docs(url_base=url_base, inv_objects=py_objects, debug=debug)
    else:
        for obj in py_objects:
            if debug:
                breakpoint()
            else:
                announce(what=f"{obj.name} {url_base}{obj.uri_expanded}", quiet=False)


def cli():
    defopt.run(fetch_entities)
