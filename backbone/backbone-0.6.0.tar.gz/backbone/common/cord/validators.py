import abc
import re

from ._exceptions import *


class Validator(abc.ABC):
    def __call__(self, obj):
        raise NotImplementedError


class RegexValidator(Validator):
    def __init__(self, expr):
        self.expr = re.compile(expr)

    def __call__(self, obj):
        if not self.expr.fullmatch(obj):
            raise CordValueError(f"Failed regex validation: '{obj}' does not match '{self.expr}'")


class LengthValidator(Validator):
    def __init__(self, min_length=None, max_length=None):
        self._min_length = min_length
        self._max_length = max_length

    def __call__(self, obj):
        if self._min_length is not None and len(obj) < self._min_length:
            raise CordValueError(f"Failed length validation: '{obj}' is shorter than {self._min_length}")

        if self._max_length is not None and len(obj) > self._max_length:
            raise CordValueError(f"Failed length validation: '{obj}' is longer than {self._max_length}")
