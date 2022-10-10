import fnmatch
import glob
from typing import Union

from mitre_attack.types import STRS
import mitre_attack.types


def matches(values: Union[str, STRS], patterns: Union[str, STRS] = None) -> bool:
    values = mitre_attack.types.to_lowercase_strings(values)
    patterns = mitre_attack.types.to_lowercase_strings(patterns)

    for value in values:
        for pattern in patterns:
            if value == pattern or (glob.has_magic(pattern) and fnmatch.fnmatch(value, pattern)):
                return True
    return False

