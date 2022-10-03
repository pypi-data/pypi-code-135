# __init__.py

# Version of the iterkit package
__version__ = "1.0.0"


__tie = "".join

__next_or_none = lambda __i:next(__i,None)

def tie(*args) -> str:
    return __tie(tuple(args))

def next_or_none(__i):
    return __next_or_none(__i,None)