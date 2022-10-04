from dataclasses import dataclass

from ns.application_layer.decorators import model
from ns.application_layer.entities.methods import MethodData


@model
@dataclass
class ServiceData:
    __tech__ = True

    name: str
    methods: list[MethodData]
