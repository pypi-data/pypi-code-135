from typing import Callable
from collections import deque as _deque

__tie = "".join

__next_or_none = lambda __i: next(__i, None)


def tie(*args) -> str:
    return __tie(args)


def next_or_none(__i):
    return __next_or_none(__i)


def __iter_limit(__iterator, limit: int):
    count = 0
    for value in iter(__iterator):
        count += 1
        if count > limit:
            break
        yield value


def __iter_bigrams(__iterator, wrapper: Callable):
    __iterator = iter(__iterator)
    try:
        lhs = next(__iterator)
    except StopIteration:
        return
    for rhs in __iterator:
        yield wrapper((lhs, rhs))
        lhs = rhs
    yield wrapper((lhs, None))


def __iter_ngrams(__iterator, width: int, wrapper: Callable):
    deque = _deque()
    append = deque.append
    popleft = deque.popleft
    __iterator = iter(__iterator)
    for _ in range(width):
        try:
            value = next(__iterator)
            append(value)
        except StopIteration:
            continue
    for rhs in __iterator:
        yield wrapper(deque)
        append(rhs)
        popleft()
    yield wrapper(deque)


def iter_limit(__iterator, limit: int):
    return __iter_limit(__iterator, limit=limit)


def iter_bigrams(__iterator, wrapper: Callable = None, limit: int = None):
    _wrapper = lambda value: value if wrapper is None else wrapper
    iterator = __iter_bigrams(__iterator, wrapper=_wrapper)
    return iterator if limit is None else __iter_limit(iterator, limit=limit)


def iter_ngrams(__iterator, width: int, wrapper: Callable = tuple, limit: int = None):
    iterator = (
        __iter_ngrams(__iterator, width=width, wrapper=wrapper)
        if width > 2
        else iter_bigrams(__iterator)
        if width == 2
        else iter(__iterator)
    )
    return iterator if limit is None else __iter_limit(iterator,limit=limit)
