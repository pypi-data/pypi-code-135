from functools import wraps
from typing import Callable

from ns.application_layer import registry
from ns.utils import to_snake_case


def service(cls: type):
    if hasattr(cls, '__service_name__'):
        cls_name = cls.__service_name__
    else:
        cls_name = to_snake_case(cls.__name__).replace('_service', '')
        cls.__service_name__ = cls_name
    if cls_name in registry.SERVICES:
        raise ValueError(f'Duplicate service with name {cls_name}')
    registry.SERVICES[cls_name] = cls
    return cls


def model(cls: type):
    registry.ENTITIES.append(cls)
    return cls


def container(fn: Callable):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    registry.CONTAINERS.append(fn)
    return wrapper
