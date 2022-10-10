from typing import Callable, TypeVar, Iterable
from collections import deque as _deque
from collections import defaultdict as _defaultdict

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


def __limited_iterator(func):
    def inner(*args, **kwargs):
        limit = kwargs.get("limit", None)
        result = func(*args, **kwargs)
        if limit is not None:
            result = __iter_limit(result, limit)
        return result

    return inner


@__limited_iterator
def __iter_bigrams(__iterator, wrapper: Callable, limit: int = None):
    _wrapper = lambda value: value if wrapper is None else wrapper
    iterator = iter(__iterator)
    try:
        lhs = next(iterator)
    except StopIteration:
        return
    for rhs in iterator:
        yield _wrapper((lhs, rhs))
        lhs = rhs
    yield _wrapper((lhs, None))


@__limited_iterator
def __iter_ngrams(__iterator, width: int, wrapper: Callable, limit: int = None):
    deque = _deque()
    append = deque.append
    popleft = deque.popleft
    iterator = iter(__iterator)
    for _ in range(width):
        try:
            value = next(iterator)
            append(value)
        except StopIteration:
            continue
    for rhs in iterator:
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
            _where_item = lambda kv: where_item(kv)
        else:
            wi = lambda kv: where_item(kv) and _where_item(kv)
            _where_item = wi
    return _where_item


@__limited_iterator
def __iter_dict(
    __dict: dict[K, V],
    where_key: Callable[[K], bool] = None,
    where_value: Callable[[V], bool] = None,
    where_item: Callable[[tuple[K, V]], bool] = None,
    wrapper: Callable = None,
    limit: int = None,
):
    _where_item = __where_item(
        where_key=where_key, where_value=where_value, where_item=where_item
    )
    _wrapper = tuple if wrapper is None else wrapper
    iterator = iter(__dict.items())
    result = (kv for kv in iterator)
    if _where_item is not None:
        result = (kv for kv in result if _where_item(kv))
    return (_wrapper(kv) for kv in result)


@__limited_iterator
def __iter_derived_values_with_cache(
    __iterator: Iterable[V], getter: Callable[[V], K] = None, limit: int = None
):
    iterator = iter(__iterator)
    key = None

    def getvalue():
        return getter(key)

    cache = _defaultdict(getvalue)
    for value in iterator:
        key = value
        result = cache[key]
        if result:
            yield result


@__limited_iterator
def _iter(__iterator, limit: int = None):
    return iter(__iterator)


def iter_limit(__iterator, limit: int):
    return __iter_limit(__iterator, limit=limit)


def iter_bigrams(__iterator, wrapper: Callable = None, limit: int = None):
    return __iter_bigrams(__iterator, wrapper=wrapper, limit=limit)


def iter_ngrams(__iterator, width: int, wrapper: Callable = tuple, limit: int = None):
    return (
        __iter_ngrams(__iterator, width=width, wrapper=wrapper, limit=limit)
        if width > 2
        else __iter_bigrams(__iterator, limit=limit)
        if width == 2
        else _iter(__iterator, limit=limit)
    )


def iter_dict(
    __dict: dict[K, V],
    where_key: Callable[[K], bool] = None,
    where_value: Callable[[V], bool] = None,
    where_item: Callable[[tuple[K, V]], bool] = None,
    wrapper: Callable = None,
    limit: int = None,
):
    return __iter_dict(
        __dict,
        where_key=where_key,
        where_value=where_value,
        where_item=where_item,
        wrapper=wrapper,
    )


def iter_derived_values(
    __iterator: Iterable[V],
    getter: Callable[[V], K] = None,
    with_cache: bool = True,
    limit: int = None,
):
    iterator = (
        __iter_derived_values_with_cache(__iterator, getter=getter, limit=limit)
        if with_cache
        else (getter(value) for value in _iter(iterator, limit=limit))
    )
