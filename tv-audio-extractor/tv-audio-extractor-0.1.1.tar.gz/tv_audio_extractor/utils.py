
from typing import Iterable, Sequence, TypeVar


_T1 = TypeVar('_T1')

def flatten(lists: Iterable[Iterable[_T1]]) -> Iterable[_T1]:
    for l in lists:
        for item in l:
            yield item 