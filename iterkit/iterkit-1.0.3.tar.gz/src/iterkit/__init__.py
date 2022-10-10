
from collections import deque as _deque
from typing import Callable

__tie = "".join

__next_or_none = lambda __i:next(__i,None)

def tie(*args) -> str:
    return __tie(args)

def next_or_none(__i):
    return __next_or_none(__i)

def __iter_bigrams(__iterator):
    __iterator = iter(__iterator)
    try:
        lhs = next(__iterator)
    except StopIteration:
        return
    for rhs in __iterator:
        yield (lhs, rhs)
        lhs = rhs
    
    yield (lhs, None)



def __iter_ngrams(__iterator,width:int,wrapper:Callable):
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
    

def iter_bigrams(__iterator):
    return __iter_bigrams(__iterator)


def iter_ngrams(__iterator,width:int,wrapper:Callable=tuple):
    return __iter_ngrams(__iterator,width=width,wrapper=wrapper) if width > 2 else iter_bigrams(__iterator) if width == 2 else iter(__iterator)

