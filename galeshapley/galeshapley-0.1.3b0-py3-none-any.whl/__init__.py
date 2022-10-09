""" Top-level imports for the library. """

import sys

from .base import BaseGame, BaseMatching, BasePlayer
from .matchings import MultipleMatching, SingleMatching
from .players import Player
from .version import __version__

if not sys.warnoptions:
    import warnings

    warnings.simplefilter("always")

__all__ = [
    "BaseGame",
    "BaseMatching",
    "BasePlayer",
    "SingleMatching",
    "MultipleMatching",
    "Player",
    "__version__",
]
