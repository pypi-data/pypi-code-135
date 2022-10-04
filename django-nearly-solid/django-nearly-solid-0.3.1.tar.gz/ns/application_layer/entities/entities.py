from dataclasses import dataclass

from ns.application_layer.decorators import model
from ns.application_layer.entities.props import PropData
from ns.application_layer.entities.types import TypeData


@model
@dataclass
class EntityData:
    __tech__ = True

    name: str
    type: TypeData
    props: list[PropData]

