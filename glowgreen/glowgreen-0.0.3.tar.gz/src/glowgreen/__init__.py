import importlib.metadata

try:
    __version__ = importlib.metadata.version("glowgreen")
except importlib.metadata.PackageNotFoundError:
    __version__ = None

from .clearance import Clearance_1m

from .close_contact import (
    ContactPatternRepeating,
    ContactPatternOnceoff,
    cs_restrictions,
    cs_patterns,
    restrictions_for,
)
