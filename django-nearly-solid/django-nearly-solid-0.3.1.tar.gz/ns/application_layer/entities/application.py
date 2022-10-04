from dataclasses import dataclass

from ns.application_layer.decorators import model
from ns.application_layer.entities.entities import EntityData
from ns.application_layer.entities.services import ServiceData


@model
@dataclass
class ApplicationData:
    __tech__ = True

    services: list[ServiceData]
    entities: dict[str, EntityData]
