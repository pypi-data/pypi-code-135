from enum import EnumMeta

from pydantic.main import ModelMetaclass as PydanticModelMetaclass
from django.db.models.base import ModelBase as DjangoModelMetaclass

from ns.application_layer.entities.entities import EntityData
from ns.application_layer.serialization.dataclass_entities import serialize_dataclass_entity
from ns.application_layer.serialization.django_models import serialize_django_model
from ns.application_layer.serialization.enum_entities import serialize_enum_entity
from ns.application_layer.serialization.pydantic_entities import serialize_pydantic_entity
from ns.application_layer.typings import EntityMeta


def serialize_entities(*models: EntityMeta) -> dict[str, EntityData]:
    result = {}
    for model in models:
        model_data = serialize_entity(model)
        if model_data.name in result:
            raise ValueError(f'Names conflict with {result[model_data.name]} and {model_data}')
        result[model_data.name] = model_data
    return result


def serialize_entity(model: EntityMeta) -> EntityData:
    if isinstance(model, PydanticModelMetaclass):
        return serialize_pydantic_entity(model)
    elif isinstance(model, DjangoModelMetaclass):
        return serialize_django_model(model)
    elif hasattr(model, '__dataclass_fields__'):
        return serialize_dataclass_entity(model)
    elif isinstance(model, EnumMeta):
        return serialize_enum_entity(model)
    raise ValueError(f'model type {model.__name__} is not a valid')
