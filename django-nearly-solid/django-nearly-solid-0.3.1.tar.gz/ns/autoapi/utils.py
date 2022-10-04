import base64
import json
from typing import Callable

from django.contrib.auth.models import User
from django.http import HttpRequest

from ns.auth import authorized_user
from ns.application_layer.dataclasses import MethodData


def get_service_method(service_name: str, method_name: str) -> (Callable, MethodData):
    """
    Возвращает метод и данные о нем
    """
    if service_name not in SERVICES:
        raise RPCError(ErrorCodes.UNKNOWN_SERVICE)
    service = SERVICES[service_name]
    method = getattr(service, method_name)
    parsed_method = None
    for parsed_method in parsed_services[service_name].methods:
        if parsed_method.name == method_name:
            break
    if not parsed_method or parsed_method.name != method_name:
        raise RPCError(ErrorCodes.UNKNOWN_SERVICE_METHOD)
    return method, parsed_method


def authenticate_user(request: HttpRequest) -> User:
    """
    Аутентифицирует юзера в АПИ
    """
    user = None
    auth_token = request.headers.get('Authorization')
    if auth_token:
        user = SERVICES['users']._authenticate(auth_token)
    authorized_user.set(user)
    return user


def parse_method_arguments(request: HttpRequest, method_data: Method) -> list[any]:
    """
    Парсит данные реквеста в аргументы метода
    """
    if method_data.upload_image:
        return parse_upload_data(request, method_data)
    return parse_json_args(request, method_data)


def parse_json_args(request: HttpRequest, method_data: Method) -> list[any]:
    """
    Парсит JSON данные реквеста в аргументы метода
    """
    args = json.loads(request.body)
    if not isinstance(args, list):
        raise ValueError('arguments must be a list')

    if len(args) != len(method_data.args):
        raise ValueError(f'got bad arguments. Excepted: {method_data.args.__repr__()}')

    deserialized_args = []
    for argument in args:
        argument_index = args.index(argument)
        parsed_arg = method_data.args[argument_index]

        if isinstance(parsed_arg.type_instance.type_instance, ModelMetaclass):
            argument = parsed_arg.type_instance.type_instance(**argument)
        deserialized_args.append(argument)
    return deserialized_args


def parse_upload_data(request: HttpRequest, method_data: Method) -> list[any]:
    """
    Парсит Multipart/Form-Data данные реквеста в аргументы метода
    """
    args = json.loads(request.body)
    if not isinstance(args, list):
        raise ValueError('arguments must be a list')

    if len(args) != len(method_data.args):
        raise ValueError(f'got bad arguments. Excepted: {method_data.args.__repr__()}')

    deserialized_args = []
    for argument in args:
        argument_index = args.index(argument)
        parsed_arg = method_data.args[argument_index]
        if isinstance(parsed_arg.type_instance.type_instance, ModelMetaclass):
            argument = parsed_arg.type_instance.type_instance(**argument)
        elif parsed_arg.type_instance.type_instance is bytes:
            if not isinstance(argument, str):
                raise ...
            argument = argument.replace('data:image/png;base64,', '').encode('ascii')
            argument = base64.b64decode(argument)
        deserialized_args.append(argument)
    return deserialized_args

