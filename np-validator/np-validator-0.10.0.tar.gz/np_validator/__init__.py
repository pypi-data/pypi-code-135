"""Awesome `np-validator` is a Python cli/package created with https://github.com/TezRomacH/python-package-template"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata

from .core import (
    autogenerate_validation_steps,
    run_validation,
    update_project_validation_steps,
)
from .exceptions import NpValidatorError
from .models import (
    Processor,
    ValidationStep,
    Validator,
    dump_ValidationResults,
    load_ValidationStep,
)


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

# needed or else mypy will complain as of 0.971
__all__ = [
    "run_validation",
    "ValidationStep",
    "Validator",
    "Processor",
    "load_ValidationStep",
    "dump_ValidationResults",
    "autogenerate_validation_steps",
    "update_project_validation_steps",
    "version",
    "NpValidatorError",
]
