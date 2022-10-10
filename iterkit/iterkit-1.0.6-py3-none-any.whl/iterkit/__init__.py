from typing import Callable, TypeVar
from collections import deque as _deque

K = TypeVar("K")
V = TypeVar("V")

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


def __where_item(
    where_key: Callable[[K], bool] = None,
    where_value: Callable[[V], bool] = None,
    where_item: Callable[[tuple[K, V]], bool] = None,
):
    _where_item = None
    if where_key is not None:
        if where_value is not None:
            _where_item = lambda kv: where_key(kv[0]) and where_value(kv[1])
        else:
            _where_item = lambda kv: where_key(kv[0])
    elif where_value is not None:
        _where_item = lambda kv: where_value(kv[1])
    if where_item is not None:
        if _where_item is None:
            _where_item = lambda kv: where_item(kv) and _where_item(kv)
        else:
            wi = lambda kv: where_item(kv) and _where_item(kv)
            _where_item = wi
    return _where_item


def __iter_dict(
    __dict: dict[K, V],
    where_key: Callable[[K], bool] = None,
    where_value: Callable[[V], bool] = None,
    where_item: Callable[[tuple[K, V]], bool] = None,
    wrapper: Callable = None,
):
    _where_item = __where_item(
        where_key=where_key, where_value=where_value, where_item=where_item
    )
    _wrapper = tuple if wrapper is None else wrapper
    result = (kv for kv in __dict.items())
    if _where_item is not None:
        result = (kv for kv in result if _where_item(kv))
    return (_wrapper(kv) for kv in result)


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
    return iterator if limit is None else __iter_limit(iterator, limit=limit)


def iter_dict(
    __dict: dict[K, V],
    where_key: Callable[[K], bool] = None,
    where_value: Callable[[V], bool] = None,
    where_item: Callable[[tuple[K, V]], bool] = None,
    wrapper: Callable = None,
    limit: int = None,
):
    iterator = __iter_dict(
        __dict,
        where_key=where_key,
        where_value=where_value,
        where_item=where_item,
        wrapper=wrapper,
    )
    return iterator if limit is None else iter_limit(iterator, limit=limit)
