from enum import EnumMeta

from ns.application_layer.entities.entities import EntityData
from ns.application_layer.serialization.types import serialize_type


def serialize_enum_entity(model: EnumMeta) -> EntityData:
    props = []
    return EntityData(
        name=model.__name__,
        props=props,
        type=serialize_type(model),
    )
