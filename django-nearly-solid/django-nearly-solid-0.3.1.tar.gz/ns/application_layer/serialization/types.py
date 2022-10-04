from dataclasses import is_dataclass
from enum import Enum, EnumMeta
from typing import get_args

from django.db.models import Model
from django.db.models.base import ModelBase
from pydantic import BaseModel
from pydantic.main import ModelMetaclass

from ns.application_layer.entities.types import TypeData


def serialize_type(t: type) -> 'TypeData':
    if isinstance(t, str):
        return t
    is_generic = hasattr(t, '__origin__')
    generic_args = []
    if is_generic:
        generic_args = serialize_generic_args(t)
        if t.__name__ == 'Optional':
            return generic_args[0]
    is_pydantic_model = isinstance(t, ModelMetaclass)
    is_django_model = isinstance(t, ModelBase)
    is_dataclass = hasattr(t, '__dataclass_fields__')
    is_enum = isinstance(t, EnumMeta)
    is_entity = is_pydantic_model or is_django_model or is_dataclass or is_enum
    is_technical = hasattr(t, '__tech__') and t.__tech__
    return TypeData(
        type_instance=t,
        name=t.__name__,
        is_generic=is_generic,
        generic_args=generic_args,
        is_pydantic_model=is_pydantic_model,
        is_django_model=is_django_model,
        is_dataclass=is_dataclass,
        is_enum=is_enum,
        enum_values=[v.value for v in t] if isinstance(t, EnumMeta) else [],
        is_technical=is_technical,
        is_entity=is_entity,
    )


def serialize_generic_args(generic_type: type) -> list['TypeData']:
    args = get_args(generic_type)
    generic_args = []
    for arg in args:
        arg_data = serialize_type(arg)
        generic_args.append(arg_data)
    return generic_args
