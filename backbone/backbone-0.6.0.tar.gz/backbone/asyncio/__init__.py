import typing

from nacl.public import PrivateKey
from nacl.signing import SigningKey

from backbone.common import protocol, service

from ._origin import Origin
from ._security import Trust

__all__ = ["Client", "from_derived_secrets", "from_master_secret"]

from .user import UserClient
from .workspace import WorkspaceClient


class Client:
    def __init__(self, trust: Trust, origin: Origin):
        self._trust: Trust = trust
        self._origin: Origin = origin

        self._user_client = UserClient(trust=self._trust, origin=self._origin)
        self._workspace_clients = {}

    async def __aenter__(self) -> "Client":
        await self._origin.__aenter__()

        if self._trust.is_bootstrapped:
            return self

        try:
            await self._user_client.fetch_self()
        except service.Error:
            await self._user_client.create()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._origin.__aexit__(exc_type, exc_val, exc_tb)

    @property
    def user(self):
        return self._user_client

    enter = __aenter__
    exit = __aexit__

    def with_workspace(self, workspace_name: str):
        workspace = self._workspace_clients.get(workspace_name)

        if workspace is None:
            workspace = WorkspaceClient(
                trust=self._trust,
                origin=self._origin,
                user_client=self._user_client,
                workspace_name=workspace_name,
            )

            self._workspace_clients[workspace_name] = workspace

        return workspace


def from_derived_secrets(
    user_name: str, secret_key: bytes, private_key: PrivateKey, signing_key: SigningKey
) -> "Client":
    trust = Trust(user_name=user_name, secret_key=secret_key, private_key=private_key, signing_key=signing_key)
    origin = Origin(trust)
    return Client(trust, origin)


def from_master_secret(user_name: str, master_secret: typing.Union[str, bytes]):
    trust = Trust.from_master_secret(user_name, master_secret)
    origin = Origin(trust)
    return Client(trust, origin)
