from dataclasses import dataclass
from typing import Union

from ns.application_layer.decorators import model


@model
@dataclass
class TypeData:
    __tech__ = True

    type_instance: type
    name: str
    is_generic: bool
    generic_args: list['TypeData']
    is_entity: bool
    is_dataclass: bool
    is_pydantic_model: bool
    is_django_model: bool
    is_enum: bool
    enum_values: list[Union[str, int]]
    is_technical: bool
