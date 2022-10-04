import inspect
import re
from inspect import signature, Parameter
from typing import Callable

from ns.application_layer.entities.methods import MethodData
from ns.application_layer.entities.props import PropData
from ns.application_layer.serialization.types import serialize_type


def getdoc(obj):
    """Get the doc string or comments for an object."""
    result = inspect.getdoc(obj) or inspect.getcomments(obj)
    if not result:
        return None
    doc_lines = result.split('\n')
    print(doc_lines)
    return result


def serialize_method(func: Callable) -> MethodData:
    method_signature = signature(func)
    arguments = []
    for param_name, param in method_signature.parameters.items():
        if param_name == 'self':
            continue
        prop_data = PropData(
            name=param_name,
            type=serialize_type(param.annotation),
            required=param.default is Parameter.empty,
            default_value=param.default,
        )
        arguments.append(prop_data)
    description = getdoc(func)
    return MethodData(
        name=func.__name__,
        args=arguments,
        return_type=serialize_type(method_signature.return_annotation),
        set_auth_token=func.__dict__.get('__set_auth_token__', False),
        auth_required=func.__dict__.get('__auth_required__', False),
        upload_image=func.__dict__.get('__upload_image__', False),
        returns_png=func.__dict__.get('__returns_png__', False),
        is_query=func.__dict__.get('__query__', False),
        description=description,
    )
