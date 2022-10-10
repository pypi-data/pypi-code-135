import inspect
import itertools
import json
import logging
from enum import Enum
from functools import lru_cache
from http import HTTPStatus
from itertools import chain
from time import sleep
from typing import Any, Mapping, Optional, NamedTuple, Sequence, Iterable, MutableMapping, Callable, Union, SupportsInt, \
    SupportsFloat

import requests
from enforce_typing import enforce_types
from frozendict import frozendict  # type: ignore
from http_constants.headers import HttpHeaders
from hyperlink import URL
from requests import Response

from platform_client.authentication import get_request_auth
from platform_client.configuration import get_env_variable


class RequestMode(Enum):
    PRIVILEGED = 'PRIVILEGED'


class ErrorInfo:

    @property
    def status_code(self) -> Optional[int]:
        return None

    @property
    def exception(self) -> Optional[Exception]:
        return None

    def __str__(self) -> str:
        if self.exception:
            return f"ErrorInfo(exception={self.exception})"
        return f"ErrorInfo(status_code={self.status_code})"


RetryPolicy = Callable[[ErrorInfo, Any], Any]


@enforce_types
def retry_policy(*,
                 max_retry: Optional[SupportsInt] = None,
                 initial_retry_delay: SupportsFloat = 1,
                 max_retry_delay: SupportsFloat = 600,
                 backoff_ratio: SupportsFloat = 2,
                 is_whitelisted: Callable[[ErrorInfo], Any] = lambda _: False) -> RetryPolicy:
    i_max_retry = int(max_retry) if max_retry is not None else None
    f_initial_retry_delay = float(initial_retry_delay)
    f_max_retry_delay = float(max_retry_delay)
    f_backoff_ratio = float(backoff_ratio)
    if not f_backoff_ratio >= 1.0:
        raise ValueError("retry_policy: backoff ratio cannot be less than 1.0")
    if not f_max_retry_delay > 0.0:
        raise ValueError("retry_policy: max_retry_delay must be strictly positive number")
    if not f_initial_retry_delay > 0.0:
        raise ValueError("retry_policy: initial_retry_delay must be strictly positive")
    if not f_max_retry_delay >= f_initial_retry_delay:
        raise ValueError("retry_policy: max_retry_delay must by no less than initial retry delay")
    if i_max_retry and not i_max_retry >= 0:
        raise ValueError("retry_policy: max_retry (if any) must be non-negative integer.")

    @enforce_types
    def policy(err_info: ErrorInfo, retry: Optional[int]) -> Optional[int]:
        retry = retry or 0
        retry += 1  # now retry contains which (in order) retry is this one
        if i_max_retry is not None and retry > i_max_retry or is_whitelisted(err_info):
            return None  # max retry limit reached (no retry then) or it's not considered an error (no retry then)
        sleep_time = min(f_initial_retry_delay * (f_backoff_ratio ** (retry - 1)), f_max_retry_delay)
        sleep(sleep_time)
        return retry

    return policy


@enforce_types
def _status_error_info(status: int) -> ErrorInfo:
    class StatusErrorInfo(ErrorInfo):
        @property
        def status_code(self) -> Optional[int]:
            return status

    return StatusErrorInfo()


@enforce_types
def _exception_error_info(exc: Exception) -> ErrorInfo:
    class ExceptionErrorInfo(ErrorInfo):
        @property
        def exception(self) -> Optional[Exception]:
            return exc

    return ExceptionErrorInfo()


# noinspection PyUnusedLocal
no_retry_policy = retry_policy(max_retry=0)


def _curr_func_name(level: int = 1) -> str:
    return inspect.stack()[level][3]


def _debug_log(msg: Any) -> None:
    calling_function_name = _curr_func_name(2)
    message = f'{calling_function_name}: {msg}'
    logging.debug(message)


class PreconditionFailedException(Exception):
    pass


class GetInstanceResponse(NamedTuple):
    etag: str
    content: Mapping[str, Any]


class CollectionPage(NamedTuple):
    items: Sequence[Mapping[str, Any]]
    # page info will come later if needed


class PostResponse(NamedTuple):
    id: str
    # perhaps something will go in the future (so the change will be non-breaking)


class PatchResponse(NamedTuple):
    etag: str
    # perhaps something will go in the future (so the change will be non-breaking)


class EntityInstanceEvent(NamedTuple):
    next_representation: Optional[Mapping[str, Any]]
    prev_representation: Optional[Mapping[str, Any]]


def _get_cs_base_url() -> str:
    return get_env_variable('ENTITY_ENGINE_ROOT_URI')


@lru_cache
@enforce_types
def _get_cs_base_url_as_url(_ignore: None = None) -> URL:
    return URL.from_text(_get_cs_base_url()).normalize()


@enforce_types
def _build_instance_or_collection_uri(instance_or_collection_id: str) -> URL:
    if instance_or_collection_id.startswith("/"):
        instance_or_collection_id = instance_or_collection_id[1:]
    base_url = _get_cs_base_url_as_url()
    new_path = chain(base_url.path, instance_or_collection_id.split("/"))
    return base_url.replace(path=new_path).normalize()


@enforce_types
def _build_event_uri(instance_id: str, event_order_no: Union[str, int]) -> URL:
    instance_uri = _build_instance_or_collection_uri(instance_id)
    event_order_no = event_order_no if isinstance(event_order_no, str) else str(event_order_no)
    new_path = chain(instance_uri.path, (".events", event_order_no))
    return instance_uri.replace(path=new_path).normalize()


# noinspection PyShadowingNames
@enforce_types
def get_instance(entity_instance_id: str, *,
                 retry_policy: RetryPolicy = no_retry_policy) -> Optional[GetInstanceResponse]:
    uri = _build_instance_or_collection_uri(entity_instance_id)
    response = _handle_response(lambda: requests.get(uri.to_text(), auth=get_request_auth()), retry_policy=retry_policy,
                                accept_not_found=True)
    return GetInstanceResponse(etag=response.headers[HttpHeaders.ETAG], content=response.json()) if response else None


def _add_mode_param(params: MutableMapping[str, Sequence[str]], request_mode: Union[None, str, RequestMode]) -> None:
    if request_mode:
        params['mode'] = [request_mode.value if isinstance(request_mode, RequestMode) else request_mode]


# noinspection PyShadowingNames
@enforce_types
def delete_instance(entity_instance_id: str, if_match: str, *, ignore_not_found: bool = False,
                    retry_policy: RetryPolicy = no_retry_policy,
                    request_mode: Union[None, str, RequestMode] = None) -> None:
    uri = _build_instance_or_collection_uri(entity_instance_id).to_text()
    auth = get_request_auth()
    headers = {HttpHeaders.IF_MATCH: if_match}
    params: MutableMapping[str, Sequence[str]] = {}
    _add_mode_param(params, request_mode)
    _handle_response(lambda: requests.delete(uri, params=params, auth=auth, headers=headers),
                     retry_policy=retry_policy,
                     accept_not_found=ignore_not_found)


# noinspection PyShadowingNames
@enforce_types
def patch_instance(entity_instance_id: str, if_match: str, patch: Mapping[str, Any],
                   *, retry_policy: RetryPolicy = no_retry_policy,
                   request_mode: Union[None, str, RequestMode] = None) -> PatchResponse:
    uri = _build_instance_or_collection_uri(entity_instance_id).to_text()
    auth = get_request_auth()
    headers = {
        HttpHeaders.IF_MATCH: if_match,
        HttpHeaders.CONTENT_TYPE: "application/merge-patch+json; charset=UTF-8"
    }
    params: MutableMapping[str, Sequence[str]] = {}
    _add_mode_param(params, request_mode)
    response = _handle_response(lambda: requests.patch(uri, auth=auth, headers=headers, json=patch, params=params),
                                retry_policy=retry_policy)
    return PatchResponse(etag=response.headers[HttpHeaders.ETAG])


# noinspection PyShadowingNames
@enforce_types
def get_domain_event(entity_instance_id: str, order_no: Union[str, int],
                     *, retry_policy: RetryPolicy = no_retry_policy) -> EntityInstanceEvent:
    uri = _build_event_uri(entity_instance_id, order_no)
    as_map = _handle_response_return_body('get_domain_event',
                                          lambda: requests.get(
                                              uri.to_text(),
                                              auth=get_request_auth(),
                                              params={'include': '/nextRepresentation,/prevRepresentation'}
                                          ),
                                          retry_policy)
    return EntityInstanceEvent(as_map.get('nextRepresentation'), as_map.get('prevRepresentation'))


# noinspection PyShadowingNames
@enforce_types
def get_full_collection(entity_collection_id: str, *,
                        a_filter: Mapping[str, Any] = frozendict(),
                        a_include: Iterable[str] = (),
                        id_property_name: str = 'id',
                        retry_policy: RetryPolicy = no_retry_policy
                        ) -> Iterable[Mapping[str, Any]]:
    last_id: Optional[str] = None
    while True:
        items = get_collection_page(
            entity_collection_id, retry_policy=retry_policy,
            a_filter=a_filter, a_include=a_include, a_min_id_exclusive=last_id).items
        last_id = None
        for item in items:
            last_id = item[id_property_name]
            yield item
        if last_id is None:
            break


class SortOrder(Enum):
    ASC = 'asc'
    DESC = 'desc'


class SortKey(NamedTuple):
    sort_property_json_pointer: str
    sort_order: SortOrder

    @staticmethod
    @enforce_types
    def asc(sort_property_json_pointer: str) -> "SortKey":
        return SortKey(sort_property_json_pointer, SortOrder.ASC)

    @staticmethod
    @enforce_types
    def desc(sort_property_json_pointer: str) -> "SortKey":
        return SortKey(sort_property_json_pointer, SortOrder.DESC)


@enforce_types
def _build_sort_query_param(a_sort: Sequence[SortKey]) -> Sequence[str]:
    @enforce_types
    def map_sort_key(key: SortKey) -> Sequence[str]:
        return key.sort_property_json_pointer, key.sort_order.value

    return list(itertools.chain.from_iterable(map(map_sort_key, a_sort)))


# noinspection PyShadowingNames
@enforce_types
def get_collection_page(entity_collection_id: str, *,
                        a_sort: Sequence[SortKey] = tuple(),
                        a_page: Optional[int] = None,
                        a_size: Optional[int] = None,
                        a_filter: Mapping[str, Any] = frozendict(),
                        a_include: Iterable[str] = (),
                        a_min_id_exclusive: Optional[str] = None,
                        a_count_pages: bool = False,
                        retry_policy: RetryPolicy = no_retry_policy
                        ) -> CollectionPage:
    collection_uri = _build_instance_or_collection_uri(entity_collection_id)
    query_params: MutableMapping[str, Sequence[str]] = {"countPages": ["true" if a_count_pages else "false"]}
    if a_page is not None:
        query_params['page'] = [str(a_page)]
    if a_size is not None:
        query_params['size'] = [str(a_size)]
    if a_min_id_exclusive is not None:
        query_params['minIdExclusive'] = [a_min_id_exclusive]
    if a_filter:
        query_params['filter'] = list(map(lambda _: f"{_[0]},{json.dumps(_[1])}", a_filter.items()))
    if a_include:
        query_params['include'] = list(a_include)
    if a_sort:
        query_params['sort'] = _build_sort_query_param(a_sort)

    response = _handle_response_return_body(
        _curr_func_name(),
        lambda: requests.get(collection_uri.to_text(), auth=get_request_auth(), params=query_params),
        retry_policy
    )
    return CollectionPage(response['_embedded']['item'])


# noinspection PyShadowingNames
@enforce_types
def post_on_collection(collection_id: str, payload: Mapping[str, Any],
                       *, retry_policy: RetryPolicy = no_retry_policy,
                       request_mode: Union[None, str, RequestMode] = None) -> PostResponse:
    return _post(collection_id, payload, retry_policy=retry_policy)


# noinspection PyShadowingNames
@enforce_types
def post_on_instance(instance_id: str, payload: Mapping[str, Any],
                     *, retry_policy: RetryPolicy = no_retry_policy,
                     request_mode: Union[None, str, RequestMode] = None) -> PostResponse:
    return _post(instance_id, payload, retry_policy=retry_policy)


# noinspection PyShadowingNames
@enforce_types
def _post(collection_or_instance_id: str, payload: Mapping[str, Any], *,
          retry_policy: RetryPolicy = no_retry_policy,
          request_mode: Union[None, str, RequestMode] = None) -> PostResponse:
    params: MutableMapping[str, Sequence[str]] = {}
    _add_mode_param(params, request_mode)
    uri = _build_instance_or_collection_uri(collection_or_instance_id)
    body = _handle_response_return_body(
        'post_principal',
        lambda: requests.post(uri.to_text(), json=payload, auth=get_request_auth(), params=params),
        retry_policy
    )
    return PostResponse(body['id'])


# noinspection PyShadowingNames
@enforce_types
def _handle_response(action: Callable[[], Response],
                     retry_policy: RetryPolicy, accept_not_found: bool = False) -> Response:
    retry = None
    while True:
        try:
            response = action()
        except Exception as exc:
            retry = retry_policy(_exception_error_info(exc), retry)
            if retry:
                _debug_log(f"Retrying after exception: retry: {retry}")
                continue
            raise
        if not response and not (accept_not_found and response.status_code == HTTPStatus.NOT_FOUND):
            if response.status_code == HTTPStatus.PRECONDITION_FAILED:
                raise PreconditionFailedException
            retry = retry_policy(_status_error_info(response.status_code), retry)
            if retry:
                _debug_log(f"Retrying after HTTP status {response.status_code}: retry: {retry}")
                continue
            raise RuntimeError(
                f"HTTP request failed: method = {response.request.method}, uri = {response.request.url}, "
                f"headers={response.request.headers}, response = {response}")
        return response


# noinspection PyShadowingNames
@enforce_types
def _handle_response_return_body(function_name: str, action: Callable[[], Response],
                                 retry_policy: RetryPolicy) -> Mapping[str, Any]:
    response = _handle_response(action, retry_policy)
    response_json = response.json()
    logging.debug(f"{function_name}: {response_json}")
    return response_json
