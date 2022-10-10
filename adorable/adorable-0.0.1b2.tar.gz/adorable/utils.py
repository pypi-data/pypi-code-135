from collections import namedtuple
from collections.abc import Mapping
from math import sqrt
from typing import Any, Callable, Sequence, TypeVar, Union

from .ansi import Ansi

T = TypeVar("T")

RGB = namedtuple("RGB", "r g b")

T_RGB = Union[tuple[int, int, int], RGB]
HEX = Union[str, int]

def filter_ansi(style: Mapping[str, Any]) -> dict[str, Ansi]:
    """
    Filters all ansi objects inside a mapping. Useful when
    ansi objects are defined in a module so that ``locals()``
    or ``module.__dict__`` can be used.
    """
    return {k: v for k, v in style.items() if isinstance(v, Ansi)}

def get_closest_color(color: RGB, colors: Sequence[tuple[RGB, Any]]) -> int:
    """
    Turns an rgb value into the closest ansi256 color.
    """
    diffs = {}
    for value, rgb in colors:
        if color == rgb:
            return value
        
        diff = sqrt(
            abs(color.r - rgb.r) ** 2 +
            abs(color.g - rgb.g) ** 2 +
            abs(color.b - rgb.b) ** 2
        )
        
        diffs[diff] = value
    
    return diffs[min(diffs.keys())]

