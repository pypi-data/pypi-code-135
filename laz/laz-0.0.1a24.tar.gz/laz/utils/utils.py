# std
import sys
from typing import List, Optional as Opt, Tuple


def split_args(args: Opt[List[str]] = None) -> Tuple[List[str], List[str]]:
    """Split args into cli args and laz args to be forwarded"""
    args = args or sys.argv
    for i, s in enumerate(args):
        if i > 0 and not s.startswith("-"):
            return args[1:i], args[i:]
    return args[1:], []
