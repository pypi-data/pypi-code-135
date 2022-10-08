from functools import wraps
import inspect
from typing import Any, Callable, Optional, TypeVar, cast, OrderedDict


FuncType = TypeVar('FuncType', bound=Callable[..., Any])

T = TypeVar('T', bound=Callable[..., Any])


def replaceFunc(replaceFunc: FuncType, *, isEnabled=True,
                _filter: Optional[Callable[[OrderedDict[str, Any]], bool]] = None):
    def decorator(func: T) -> T:
        if not isEnabled:
            return func
        signature = inspect.signature(func)

        @wraps(func)
        def decorated(*args, **kwargs):
            if not _filter:
                return replaceFunc(*args, **kwargs)
            if _filter:
                kw = signature.bind(*args, **kwargs)
                if _filter(kw.arguments):
                    return replaceFunc(*args, **kwargs)
            return func(*args, **kwargs)
        return cast(T, decorated)
    return decorator
