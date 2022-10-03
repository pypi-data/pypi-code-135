"""Awesome `data_manifestor` is a Python cli/package created with https://github.com/TezRomacH/python-package-template"""

import sys
from importlib import metadata as importlib_metadata

from .core import (
    compare_manifest_to_local,
    get_project_data_manifestor_template,
    path_to_manifest_template,
    update_project_data_manifestor_template,
)
from .exceptions import DataManifestorError, ManifestError
from .models import Template


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

__all__ = [
    "version",
    "compare_manifest_to_local",
    "get_project_data_manifestor_template",
    "update_project_data_manifestor_template",
    "path_to_manifest_template",
    "Template",
    "DataManifestorError",
    "ManifestError",
]
