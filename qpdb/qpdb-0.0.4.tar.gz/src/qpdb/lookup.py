from __future__ import annotations

import defopt

from .intersphinx import fetch_inv

__all__ = ["main", "cli"]


def list_entities(package_name: str = "pandas", version: str = "1.5") -> None:
    print(f"qp ⠶ {package_name=} & {version=}")
    [(url, inv)] = fetch_inv(package=package_name, version=version).items()
    py_objects = [o for o in inv.objects if o.domain == "py"]
    print(f"Fetched {len(py_objects)} :py: domain objects from {url}")
    for o in py_objects[:3]:
        print(o)
    print("...")
    for o in py_objects[-3:]:
        print(o)


def cli():
    defopt.run(list_entities)
