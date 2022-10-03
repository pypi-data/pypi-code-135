from __future__ import annotations

import defopt

from .intersphinx import get_intersphinx_inv

__all__ = ["main", "cli"]


def list_entities(package_name: str = "pandas", version: str = "1.5") -> None:
    print(f"qp ⠶ {package_name=} & {version=}")
    inv = get_intersphinx_inv(package=package_name, version=version)


def cli():
    defopt.run(list_entities)
