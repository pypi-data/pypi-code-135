from typing import Any, Generic, TypeAlias, TypeVar, overload

T = TypeVar("T", covariant=True)
S = TypeVar("S", covariant=True)
E = TypeVar("E", covariant=False)  # restrict to exception?


class _Result(Generic[T]):
    _value: T
    __match_args__ = ("value",)
    __slots__ = ("_value",)

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, value: T):
        ...

    def __init__(self, value: Any = True):
        self._value = value

    @property
    def value(self) -> T:
        return self._value


class Success(_Result[S]):
    pass

class Failure(_Result[E]):
    pass

Result: TypeAlias = Success[S] | Failure[E]
