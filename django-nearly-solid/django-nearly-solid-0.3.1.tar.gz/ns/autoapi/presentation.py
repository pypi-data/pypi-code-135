from dataclasses import asdict, is_dataclass
from enum import Enum

from django.forms import model_to_dict
from pydantic import BaseModel as PydanticModel
from django.db.models import Model as DjangoModel

from ns.autoapi.errors import ErrorCodes
from ns.application_layer.typings import Entity
from ns.errors import Error


def dict_factory(kv_pairs):
    result = {}
    for k, v in kv_pairs:
        result[k] = present_data(v)
    return result


def present_data(model: Entity) -> any:
    if isinstance(model, type):
        return model.__name__
    elif isinstance(model, PydanticModel):
        return model.dict()
    elif isinstance(model, DjangoModel):
        return model_to_dict(model)
    elif is_dataclass(model):
        return asdict(model, dict_factory=dict_factory)
    elif isinstance(model, dict):
        return {key: present_data(value) for key, value in model.items()}
    elif isinstance(model, list):
        return [present_data(value) for value in model]
    elif isinstance(model, Error):
        return {
            'name': model.name,
            'code': model.code,
            'data': model.data,
        }
    elif isinstance(model, BaseException):
        return {
            'name': model.__class__.__name__,
            'code': ErrorCodes.UNKNOWN_ERROR,
            'data': model.__repr__(),
        }
    elif isinstance(model, Enum):
        return model.value
    return model
