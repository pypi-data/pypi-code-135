from dataclasses import dataclass
from inspect import Parameter

from ns.application_layer.decorators import model
from ns.application_layer.entities.types import TypeData


@model
@dataclass
class PropData:
    __tech__ = True

    name: str
    type: TypeData
    required: bool
    default_value: any = Parameter.empty
