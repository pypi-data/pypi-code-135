# Pure zero-dependency JSON-RPC 2.0 implementation.
# Copyright © 2022 Andrew Malchuk. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
from collections import UserDict as Dict
from collections.abc import Iterator, MutableSequence
from functools import partial, singledispatch
from http import HTTPStatus
from io import DEFAULT_BUFFER_SIZE, BytesIO
from sys import exc_info
from threading import Thread
from traceback import print_exception
from typing import Any, ClassVar, Final, Protocol, TypeAlias, cast, overload

from ._dispatcher import Dispatcher
from ._errors import BaseError, Error
from ._request import BaseBatchRequest, BaseRequest, BatchRequest, Request
from ._response import BaseBatchResponse, BaseResponse, BatchResponse, Response
from ._serializer import JSONSerializer
from ._typing import Headers, InputStream, OptExcInfo, StartResponse, WSGIEnvironment

__all__: Final[tuple[str, ...]] = ("WSGIHandler",)

_AnyRequest: TypeAlias = BaseRequest | BaseError | BaseBatchRequest
_AnyResponse: TypeAlias = BaseResponse | BaseBatchResponse | None


class request_handler(Protocol):
    @overload
    def __call__(self, request: BaseRequest) -> BaseResponse | None: ...
    @overload
    def __call__(self, request: BaseError) -> BaseResponse: ...
    @overload
    def __call__(self, request: BaseBatchRequest[Any]) -> BaseBatchResponse[Any]: ...


class BaseWSGIHandler(Dict[str, Any], metaclass=ABCMeta):
    __slots__: tuple[str, ...] = ()

    #: The default content type of the responses.
    default_content_type: ClassVar[str] = "application/json"

    #: The list of HTTP request methods which are allowed to use.
    allowed_http_methods: ClassVar[tuple[str, ...]] = ("POST", "PUT")

    def __repr__(self) -> str:
        return f"<{self.__class__.__qualname__}({self.data!r})>"

    def __call__(self, environ: WSGIEnvironment, start_response: StartResponse) -> Iterator[bytes]:
        # Prevents the "start_response" argument duplicate invocation:
        wsgi_response: partial[Iterator[bytes]] = partial(self._get_response, start_response)

        if environ["REQUEST_METHOD"] not in self.allowed_http_methods:
            # Specified request method is invalid:
            return wsgi_response(status=HTTPStatus.METHOD_NOT_ALLOWED)

        try:
            if not (request_body := self._read_request_body(environ)):
                # Trying to check the request body is empty.
                # If that's true then it returns HTTP 400 "Bad Request".
                return wsgi_response(status=HTTPStatus.BAD_REQUEST)

            if not (response_body := self.process_request(request_body)):
                # Trying to check the response is empty.
                # If that's true then it returns empty response body.
                return wsgi_response(status=HTTPStatus.NO_CONTENT)

            # We're on a roll, baby. Send the response as is.
            return wsgi_response(response_body=response_body)

        except Exception as exc:
            # Houston, we have a problem O_o
            # In unexpected situations it raises the exception to WSGI server.
            print_exception(exc, file=environ["wsgi.errors"])
            return wsgi_response(status=HTTPStatus.INTERNAL_SERVER_ERROR, exc_info=exc_info())

    def _read_request_body(self, environ: WSGIEnvironment) -> bytes:
        try:
            content_length: int = int(environ["CONTENT_LENGTH"])
        except (KeyError, ValueError):
            return b""

        stream: Final[InputStream] = environ["wsgi.input"]

        with BytesIO() as raw_buffer:
            # Ensure to disallow reading the stream more bytes
            # than specified by "Content-Length" header:
            while content_length > 0:
                if not (chunk := stream.read(min(content_length, DEFAULT_BUFFER_SIZE))):
                    raise EOFError(f"Client disconnected, {content_length:d} more bytes were expected")

                # Appends the chunk of request body to the buffer
                # and decreases the request size:
                content_length -= raw_buffer.write(chunk)

            return raw_buffer.getvalue()

    def _get_response(self,
        start_response: StartResponse,
        *,
        status: HTTPStatus = HTTPStatus.OK,
        response_body: bytes | None = None,
        exc_info: OptExcInfo | None = None
    ) -> Iterator[bytes]:
        content_length: Final[int] = len(response_body := b"" if response_body is None else response_body)
        headers: Final[Headers] = [
            ("Content-Length", f"{content_length:d}"),
            ("Content-Type", self.default_content_type)
        ]

        if status == HTTPStatus.METHOD_NOT_ALLOWED:
            # Fill the allowed request methods if the specified method is invalid:
            headers.append(("Allow", "\u002c\u0020".join(self.allowed_http_methods)))

        start_response(f"{status.value:d}\u0020{status.phrase!s}", headers, exc_info)
        yield response_body

    @property
    @abstractmethod
    def handle_request(self) -> request_handler:
        raise NotImplementedError

    @abstractmethod
    def process_request(self, request_body: bytes) -> bytes:
        raise NotImplementedError


class WSGIHandler(BaseWSGIHandler):
    """
    Base class representing the ``WSGI`` entry point.
    Its subclassing the :py:class:`collections.UserDict` object
    for providing the user-defined data storage.

    For example::

        >>> app = WSGIHandler()
        >>> app["my_private_key"] = "foobar"
        >>> app["my_private_key"]
        "foobar"
    """
    __slots__: tuple[str, ...] = ()

    #: Class variable representing the :class:`jsonrpc.Dispatcher` object
    #: used by this class for routing user-defined functions by default.
    dispatcher: ClassVar[Dispatcher] = Dispatcher()

    #: Class variable representing the :class:`jsonrpc.JSONSerializer` object
    #: used by this class for data serialization by default.
    serializer: ClassVar[JSONSerializer] = JSONSerializer()

    @property
    def handle_request(self) -> request_handler:
        """
        Returns a single-dispatch method for the handling deserialized requests.

        :param request: One of the following objects types: :class:`jsonrpc.Request`, :class:`jsonrpc.BatchRequest`
            or :class:`jsonrpc.Error`. If the :class:`jsonrpc.BatchRequest` object type was supplied,
            its will be invoked itself recursively for each one item containing in the batch request.
        :raises ValueError: Due the invocation with unsupported request type.
        :returns: Either :class:`jsonrpc.Response` or :class:`jsonrpc.BatchResponse`.
            If the :class:`jsonrpc.Request` object was received and it's a notification, then it returns :py:data:`None`.
        """
        @singledispatch
        def wrapper(request: _AnyRequest) -> _AnyResponse:
            raise ValueError(f"Unsupported type {type(request).__name__!r}")

        @wrapper.register
        def _(request: Request) -> Response | None:
            # Save the callback for future use:
            dispatch: partial[Any] = partial(self.dispatcher.dispatch, request.method)
            # Redirect the method invocation to the separate thread,
            # if the method is notification:
            if request.is_notification:
                Thread(target=dispatch, args=request.args, kwargs=request.kwargs, daemon=True).start()
                return None
            # Elsewise, execute the method as claimed and returns the error if an exception is raised:
            try:
                result: Final[Any] = dispatch(*request.args, **request.kwargs)
                return Response(body=result, response_id=request.request_id)
            except Error as error:
                return Response(error=error, response_id=request.request_id)

        @wrapper.register
        def _(request: Error) -> Response:
            # Returns the response as is with the error attribute.
            return Response(error=request, response_id=None)

        @wrapper.register
        def _(request: BatchRequest) -> BatchResponse:
            # We need to go deeper, 'cause received a batch request object.
            # Then invoke itself recursively.
            return BatchResponse(response for response in map(wrapper, request) if isinstance(response, Response))

        return cast(request_handler, wrapper)

    def process_request(self, request_body: bytes) -> bytes:
        """
        Base method for consuming a raw requests from ``WSGI`` server and producing the serialized responses.

        :param request_body: The :py:class:`bytes` object representing a request body incoming from ``WSGI`` server.
        :returns: The :py:class:`bytes` object representing a serialized response body for next sending to ``WSGI`` server.
        """
        try:
            obj: Any = self.serializer.deserialize(request_body)
        except Error as error:
            deserialization_error: Response = Response(error=error, response_id=None)
            return self.serializer.serialize(deserialization_error.json)

        is_batch_request: Final[bool] = isinstance(obj, MutableSequence) and len(obj) >= 1
        request: Final[_AnyRequest] = BatchRequest.from_json(obj) if is_batch_request else Request.from_json(obj)

        if not (response := self.handle_request(request)):
            return b""

        try:
            return self.serializer.serialize(response.json)
        except Error as error:
            serialization_error: Response = Response(error=error, response_id=None)
            return self.serializer.serialize(serialization_error.json)
