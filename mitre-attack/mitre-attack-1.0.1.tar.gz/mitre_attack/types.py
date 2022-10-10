import datetime
from typing import Iterable, Any, Optional, Union

STRS = Iterable[str]
TIME = datetime.datetime
DATE = datetime.date


def get_len(seq: Iterable[Any]) -> int:
    return sum(1 for _ in seq)


def to_set(values: Optional[Iterable[Any]]) -> set:
    return set(values) if values else set()


def to_lowercase_strings(values: Union[str, STRS]) -> STRS:
    values = [values] if isinstance(values, str) else list(map(str, values))
    values = list(map(str.lower, values))
    return values
