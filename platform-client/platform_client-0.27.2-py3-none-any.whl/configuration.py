import inspect
import json
import logging
import os
from threading import Lock
from typing import Mapping, Union, Optional, Any

import boto3
from enforce_typing import enforce_types
from sentinels import Sentinel, NOTHING


@enforce_types
def _retrieve_secret_config() -> Mapping[str, str]:
    secret_env_id = os.getenv("SECRET_ENV_ID")
    if not secret_env_id:
        return dict()
    secret_manager = boto3.client(service_name='secretsmanager')
    response = secret_manager.get_secret_value(SecretId=secret_env_id)
    return json.loads(response['SecretString'])


_SECRET_CONFIG_LOCK = Lock()

_SECRET_CONFIG: Optional[Mapping[str, str]] = None


@enforce_types
def _get_secret_config() -> Mapping[str, str]:
    global _SECRET_CONFIG, _SECRET_CONFIG_LOCK
    if _SECRET_CONFIG is None:
        with _SECRET_CONFIG_LOCK:
            _SECRET_CONFIG = _retrieve_secret_config() if _SECRET_CONFIG is None else _SECRET_CONFIG
    return _SECRET_CONFIG


@enforce_types
def get_env_variable(variable_name: str, default: Union[Sentinel, None, str] = NOTHING) -> Optional[str]:
    secret_config = _get_secret_config()
    use_secret = variable_name not in os.environ and variable_name in secret_config
    if use_secret:
        _debug_log(f"Env variable {variable_name}: using secret manager value ...")
        return secret_config[variable_name]
    return os.environ[variable_name] if isinstance(default, Sentinel) \
        else os.environ.get(variable_name) if default is None \
        else os.environ.get(variable_name, default)


def _curr_func_name(level: int = 1) -> str:
    return inspect.stack()[level][3]


def _debug_log(msg: Any) -> None:
    calling_function_name = _curr_func_name(2)
    message = f'{calling_function_name}: {msg}'
    logging.debug(message)
    # print(message)
