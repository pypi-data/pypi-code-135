import re
from enum import EnumMeta
from importlib import import_module
from importlib.util import find_spec
from inspect import getmembers, isclass

from django.db.models.base import ModelBase
from pydantic.main import ModelMetaclass


def to_snake_case(camel):
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', camel).lower()


def is_pydantic_model(cls: type) -> bool:
    return isinstance(cls, ModelMetaclass)


def is_django_model(cls: type) -> bool:
    return isinstance(cls, ModelBase)


def is_dataclass(cls: type) -> bool:
    return hasattr(cls, '__dataclass_fields__')


def is_enum(cls: type) -> bool:
    return isinstance(cls, EnumMeta)


def import_classes_from_module(module_name: str) -> list[type]:
    result = []
    found = find_spec(module_name) is not None
    if not found:
        return result
    module = import_module(module_name)
    for name, obj in getmembers(module, lambda member: isclass(member) and member.__module__ == module_name):
        result.append(obj)
    return result
