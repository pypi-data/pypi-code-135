from abc import ABC
from enum import Enum
from typing import TypeVar, Generic

from ns.utils import to_snake_case

T = TypeVar('T', bound=Enum)


class ErrorMeta(type):
    def __new__(mcs, *args, **kwargs):
        cls = super(mcs).__new__(*args, **kwargs)
        cls.name = to_snake_case(cls.__name__).replace('_error', '')
        return cls


class Error(ABC, BaseException, Generic[T]):
    name: str
    code: T
    data: any

    def __init__(self, code: T, **data: any):
        self.code = code
        self.data = data

    def __str__(self):
        result = []
        for name, value in self.data.items():
            if name.startswith('_'):
                continue
            result.append(f'{name}={value}')
        result = ', '.join(result)
        return f'{self.__class__.__name__}({self.code.value})[{result}]'
