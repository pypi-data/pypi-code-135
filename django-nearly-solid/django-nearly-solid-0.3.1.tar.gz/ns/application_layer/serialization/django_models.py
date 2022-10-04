import ipaddress
from datetime import timedelta, date, datetime, time
from typing import TypeVar, IO

from PIL.Image import Image
from django.db.models import Field, AutoField, BigAutoField, BigIntegerField, BinaryField, BooleanField, CharField, \
    DateField, DateTimeField, DecimalField, DurationField, EmailField, FileField, FilePathField, FloatField, \
    GenericIPAddressField, ImageField, IntegerField, JSONField, PositiveBigIntegerField, PositiveIntegerField, \
    PositiveSmallIntegerField, SlugField, SmallAutoField, SmallIntegerField, TextField, TimeField, URLField, UUIDField, \
    ForeignKey, ManyToManyField, OneToOneField
from django.db.models.base import ModelBase

from ns.application_layer.entities.entities import EntityData
from ns.application_layer.entities.props import PropData
from ns.application_layer.serialization.types import serialize_type

Char = TypeVar('Char', bound=str)
Relation = TypeVar('Relation')


django_fields_types = {
    AutoField: int,
    BigAutoField: int,
    BigIntegerField: int,
    BinaryField: bytes,
    BooleanField: bool,
    CharField: Char,
    DateField: date,
    DateTimeField: datetime,
    DecimalField: float,
    DurationField: timedelta,
    EmailField: str,
    FileField: IO,
    FilePathField: str,
    FloatField: float,
    GenericIPAddressField: ipaddress,
    ImageField: Image,
    IntegerField: int,
    JSONField: dict,
    PositiveBigIntegerField: int,
    PositiveIntegerField: int,
    PositiveSmallIntegerField: int,
    SlugField: str,
    SmallAutoField: int,
    SmallIntegerField: int,
    TextField: str,
    TimeField: time,
    URLField: str,
    UUIDField: str,
}


def is_relation(field: Field) -> bool:
    return isinstance(field, ForeignKey) or isinstance(field, ManyToManyField) or isinstance(field, OneToOneField)


def serialize_django_model(model: ModelBase) -> EntityData:
    props = []
    for field in model._meta.fields:
        field: Field
        if is_relation(field):
            field_type = field.related_model
        else:
            field_type = django_fields_types[field.__class__]
        prop_data = PropData(
            name=field.name,
            type=serialize_type(field_type),
            required=not field.blank,
            default_value=field.default,
        )
        props.append(prop_data)
    return EntityData(
        name=model.__name__,
        props=props,
        type=serialize_type(model),
    )
