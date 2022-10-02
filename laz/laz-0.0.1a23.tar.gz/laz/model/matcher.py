# std
from fnmatch import fnmatch
from typing import List

# external
from braceexpand import braceexpand


class Matcher:
    def __init__(self, pattern: str):
        self._patterns: List[str] = list(braceexpand(pattern))

    def match(self, string: str) -> bool:
        return any(fnmatch(string, p) for p in self._patterns)
