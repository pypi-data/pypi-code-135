from typing import Callable


def auth_required(fn: Callable) -> Callable:
    ...
