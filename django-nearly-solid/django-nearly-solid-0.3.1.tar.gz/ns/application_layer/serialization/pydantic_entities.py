from pydantic.fields import ModelField
from pydantic.main import ModelMetaclass

from ns.application_layer.entities.entities import EntityData
from ns.application_layer.entities.props import PropData
from ns.application_layer.serialization.types import serialize_type


def serialize_pydantic_entity(model: ModelMetaclass) -> EntityData:
    props = []
    for field_name, field in model.__fields__.items():
        field: ModelField
        prop = PropData(
            name=field_name,
            type=serialize_type(field.type_),
            required=field.required,
            default_value=field.default,
        )
        props.append(prop)
    return EntityData(
        name=model.__name__,
        props=props,
        type=serialize_type(model),
    )
