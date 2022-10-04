import json
import types
from dataclasses import is_dataclass, asdict, _MISSING_TYPE, MISSING
from functools import wraps
from inspect import ismethod
from typing import Callable, TypeVar, _UnionGenericAlias

from django.http import HttpResponse
from pydantic import BaseModel

from ns.autoapi.entities import Result
from ns.autoapi.presentation import present_data
from ns.application_layer.entities.types import TypeData


def handle_result(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs) -> Result:
        data = None
        error = None
        try:
            ok = True
            data = fn(*args, **kwargs)
        except BaseException as err:
            ok = False
            error = err
        return Result(ok, data, error)
    return wrapper


def json_serializer(d: any):
    if isinstance(d, TypeVar):
        return d.__name__
    elif isinstance(d, _MISSING_TYPE):
        return 'MISSING'
    elif isinstance(d, types.BuiltinFunctionType):
        return d.__name__
    elif isinstance(d, _UnionGenericAlias):
        return 'Union'
    return json.dumps(d)


def result_as_response(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs) -> HttpResponse:
        data = fn(*args, **kwargs)
        presented_data = present_data(data)
        if is_dataclass(presented_data):
            presented_data = asdict(presented_data)
        elif isinstance(presented_data, BaseModel):
            presented_data = presented_data.dict()
        json_data = json.dumps(presented_data, default=json_serializer)
        response = HttpResponse(json_data)
        response.headers['Content-Type'] = 'application/json'
        return response
    return wrapper
