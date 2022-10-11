"""Helper functions for the typed-format-version unit tests."""

import pathlib
import sys

from typing import Any

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib


def toml_load(filename: str) -> Any:
    """Load a TOML file into a generic Python data structure."""
    return tomllib.load(
        (pathlib.Path(__file__).parent.parent.parent / "test_data" / filename).open(mode="rb")
    )
