import os
import typing
from datetime import datetime, timezone

import httpx

from backbone.common import cord, protocol, service

from ._security import Trust


class Reactor:
    def __init__(
        self,
        origin: "Origin",
        trust: Trust,
        action: str,
        ingress: typing.Optional[typing.Type[cord.Record]] = None,
        egress: typing.Optional[typing.Type[cord.Record]] = None,
    ):
        self._origin = origin
        self._trust = trust
        self._action = action
        self._ingress = ingress
        self._egress = egress

    async def react(self, data: typing.Optional[cord.Record] = None):
        headers = {"Content-Type": "application/octet-stream"}

        request_content = protocol.ServiceRequest(
            id=os.urandom(16),
            action=self._action,
            version=self._origin._version,
            datetime=datetime.now(timezone.utc),
            data=data and data.encode(),
        )

        request_envelope = self._trust.private_key_enclave.encrypt_request(request_content)
        request_body = request_envelope.encode()

        response = await self._origin._driver.post("/", content=request_body, headers=headers)

        response_body = response.read()
        response_envelope = protocol.ServiceResponseEnvelope.decode(response_body)
        response_content = self._trust.private_key_enclave.decrypt_response(response_envelope)

        if response_content.id != request_content.id:
            raise service.Error(code="invalid", message="The response ID encountered is unexpected")

        content_type, content = response_content.content

        if content_type == "error":
            raise service.Error.load(content)

        return self._egress and self._egress.decode(content)


class Origin:
    def __init__(
        self,
        trust: Trust,
        endpoint: str = None,
        version: typing.Optional[str] = "latest",
        **kwargs: typing.Any,
    ):
        self._count = 0
        self._driver: typing.Optional[httpx.AsyncClient] = None

        if not endpoint:
            endpoint = "https://api.backbone.dev" if not os.getenv("BACKBONE_DEV") else "http://localhost:8000"

        self._endpoint = endpoint
        self._kwargs = kwargs
        self._version = version
        self._trust = trust
        self._reactors = {}
        self._initialize_driver()

    def _initialize_driver(self):
        self._count += 1

        if self._driver is not None and not self._driver.is_closed:
            return self

        self._driver = httpx.AsyncClient(base_url=self._endpoint, **self._kwargs, timeout=None)

        return self

    async def __aenter__(self):
        return self._initialize_driver()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._count = max(0, self._count - 1)

        if self._count > 0 or self._driver is None:
            return

        await self._driver.aclose()

    def __contains__(self, value: str) -> bool:
        return value in self._reactors

    def add_reactor(
        self,
        action: str,
        ingress: typing.Optional[typing.Type[cord.Record]] = None,
        egress: typing.Optional[typing.Type[cord.Record]] = None,
    ):
        self._reactors[action] = Reactor(self, self._trust, action, ingress, egress)

    def react(self, *, action: str, data: typing.Any = None):
        return self._reactors[action].react(data)
