from __future__ import annotations

import defopt

__all__ = ["main", "cli"]


def list_entities(package_name: str = "pandas", version: int | None = None):
    print(f"qp ⠶ {package_name=} & {version=}")


def cli():
    defopt.run(list_entities)
