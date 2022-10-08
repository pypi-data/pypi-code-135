import sys
from functools import wraps


def mock(original_function, module=None):
    def _mock(new_function):
        @wraps(new_function)
        def _inner(*args, **kwargs):
            return new_function(*args, **kwargs)

        _inner.original = original_function

        inner_module = module

        if inner_module is None:
            inner_module = sys.modules[original_function.__module__]
        setattr(inner_module, original_function.__name__, _inner)
        return _inner

    return _mock
