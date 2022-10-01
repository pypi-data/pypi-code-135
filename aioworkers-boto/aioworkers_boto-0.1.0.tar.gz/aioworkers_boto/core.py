from typing import Optional

from aiobotocore.client import AioBaseClient
from aiobotocore.session import AioSession, ClientCreatorContext
from aioworkers.core.base import AbstractConnector


class Connector(AbstractConnector):
    _client: Optional[AioBaseClient] = None
    _client_context: Optional[ClientCreatorContext] = None
    _connection_fields = (
        "region_name",
        "api_version",
        "use_ssl",
        "verify",
        "endpoint_url",
        "aws_access_key_id",
        "aws_secret_access_key",
        "aws_session_token",
    )

    def __init__(self, *args, **kwargs):
        connection = kwargs.setdefault("connection", {})
        for field in self._connection_fields:
            if field in kwargs:
                connection.setdefault(field, kwargs.pop(field))
        super().__init__(*args, **kwargs)

    @property
    def client(self) -> AioBaseClient:
        assert self._client is not None
        return self._client

    async def connect(self):
        session = AioSession()
        service_name = self.config.get("service_name")
        cfg = self.config.get("connection") or {}
        self._client_context = session.create_client(service_name, **cfg)
        self._client = await self._client_context.__aenter__()

    async def disconnect(self):
        client_ctx = self._client_context
        if client_ctx is not None:
            await client_ctx.__aexit__(None, None, None)
            self._client = None
            self._client_context = None

    async def __aenter__(self):
        await self.connect()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
