"""An easy way to enforce assumptions on parameters."""
from dataclasses import dataclass
from functools import wraps

__version__ = "0.0.2"


@dataclass
class AssumptionException(Exception):
    msg: str = "Assumption evaluated false"

    def __init__(self, msg: str = None):
        if msg != None:
            self.msg = msg


def assume(assumption, ret=None, msg=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if assumption(*args, **kwargs):
                return func(*args, **kwargs)
            elif ret is not None:
                return ret
            elif msg is not None:
                raise AssumptionException(msg)
            else:
                raise AssumptionException()

        return wrapper

    return decorator
