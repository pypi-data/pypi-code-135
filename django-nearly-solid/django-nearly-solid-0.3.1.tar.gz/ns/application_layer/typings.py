from dataclasses import Field
from typing import Union

from pydantic.main import ModelMetaclass as PydanticModelMetaclass, BaseModel as PydanticModel
from django.db.models.base import ModelBase as DjangoModelMetaclass
from django.db.models import Model as DjangoModel


class DataclassMeta(type):
    __dataclass_fields__: dict[str, Field]


EntityMeta = Union[PydanticModelMetaclass, DjangoModelMetaclass, DataclassMeta]
Entity = Union[PydanticModel, DjangoModel, object, dict, list, type]
