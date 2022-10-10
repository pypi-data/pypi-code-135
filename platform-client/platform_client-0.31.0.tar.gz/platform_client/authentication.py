import inspect
import logging
from datetime import datetime, timedelta
from threading import Lock
from typing import Any, Optional, NamedTuple, Final

import requests
from http_constants.headers import HttpHeaders
from requests import PreparedRequest
from requests.auth import AuthBase

from platform_client.configuration import get_env_variable


def _curr_func_name(level: int = 1) -> str:
    return inspect.stack()[level][3]


def _debug_log(msg: Any) -> None:
    calling_function_name = _curr_func_name(2)
    message = f'{calling_function_name}: {msg}'
    logging.debug(message)


_EXPIRATION_MARGIN = timedelta(seconds=30)


class _TokenInfo(NamedTuple):
    access_token: str
    token_expiration: datetime


_token_info: Optional[_TokenInfo] = None

_token_info_lock: Final[Lock] = Lock()


def _do_we_need_a_new_token() -> bool:
    token_info = _token_info
    return not token_info or datetime.now() >= token_info.token_expiration


def get_access_token() -> str:
    global _token_info, _token_info_lock
    if _do_we_need_a_new_token():
        token_endpoint = get_env_variable('TOKEN_ENDPOINT')
        client_id = get_env_variable('CLIENT_ID')
        client_secret = get_env_variable('CLIENT_SECRET')
        with _token_info_lock:
            if _do_we_need_a_new_token():
                logging.debug(f"get_access_token: requesting access token from {token_endpoint} ...")
                expiration_start = datetime.now()
                response = requests.post(token_endpoint,
                                         data={"grant_type": "client_credentials"},
                                         auth=(client_id, client_secret))
                if not response:
                    raise RuntimeError(f"Access token request failed: {response}")
                response_json = response.json()
                access_token = response_json['access_token']
                token_expiration = (expiration_start
                                    + timedelta(seconds=response_json['expires_in'])
                                    - _EXPIRATION_MARGIN)
                _token_info = _TokenInfo(access_token, token_expiration)
    else:
        logging.debug("get_access_token: using cached access token.")
    assert _token_info
    return _token_info.access_token


def get_request_auth() -> AuthBase:
    return __REQUEST_AUTH


class __RequestAuth(AuthBase):
    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        request.headers[HttpHeaders.AUTHORIZATION] = f"Bearer {get_access_token()}"
        return request


__REQUEST_AUTH = __RequestAuth()
