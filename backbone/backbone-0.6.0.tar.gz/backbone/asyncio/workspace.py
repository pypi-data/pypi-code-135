import base64
import typing

from nacl.public import PrivateKey, PublicKey
from nacl.signing import SigningKey

from backbone.common import enums, models, protocol

from ._decorators import endpoint
from ._origin import Origin
from ._security import Trust
from ._utils import decode_token, encode_token
from .entry import EntryClient
from .namespace import NamespaceClient
from .stream import StreamClient

if typing.TYPE_CHECKING:
    from . import UserClient


class WorkspaceClient:
    def __init__(self, trust: Trust, origin: Origin, user_client: "UserClient", workspace_name: str):
        self._trust = trust
        self._origin = origin
        self._user_client = user_client

        self._workspace_name = workspace_name

        # Initialize workspace-bound clients
        self._namespace = NamespaceClient(trust, origin, self)
        self._entry = EntryClient(trust, origin, self)
        self._stream = StreamClient(trust, origin, self)

    @property
    def name(self):
        return self._workspace_name

    @property
    def namespace(self):
        return self._namespace

    @property
    def entry(self):
        return self._entry

    @property
    def stream(self):
        return self._stream

    def __aenter__(self):
        return self

    @endpoint(action="create_workspace", ingress=protocol.CreateWorkspaceIngress)
    async def create(self) -> None:
        workspace_private_key: PrivateKey = PrivateKey.generate()
        workspace_signing_key: SigningKey = SigningKey.generate()

        workspace_keyspace_private_key: PrivateKey = PrivateKey.generate()
        workspace_keyspace_signing_key: SigningKey = SigningKey.generate()

        root_namespace_private_key: PrivateKey = PrivateKey.generate()
        root_namespace_signing_key: SigningKey = SigningKey.generate()

        workspace = models.Workspace(
            name=self.name,
            public_key=workspace_private_key.public_key,
            verify_key=workspace_signing_key.verify_key,
            keyspace_public_key=workspace_keyspace_private_key.public_key,
            keyspace_verify_key=workspace_keyspace_signing_key.verify_key,
        )

        signed_workspace = models.SignedWorkspace.sign(
            notary=workspace_signing_key,
            content=workspace,
        )

        signed_public_workspace_grant = models.SignedSharedWorkspaceGrant.sign(
            notary=workspace_signing_key,
            content=models.SharedWorkspaceGrant.encrypt(
                provider=workspace_private_key,
                recipient=self._trust.user.public_key,
                encrypted=models.WorkspaceGrantCredentials(
                    private_key=workspace_private_key,
                    signing_key=workspace_signing_key,
                    keyspace_private_key=workspace_keyspace_private_key,
                    keyspace_signing_key=workspace_keyspace_signing_key,
                ),
                plain=models.WorkspaceGrant(
                    permissions=set(enums.WorkspacePermission),
                    recipient=models.WorkspaceGrantRecipient(("user", self._trust.user.identify())),
                ),
            ),
        )

        signed_root_namespace = models.SignedNamespace.sign(
            notary=workspace_keyspace_signing_key,
            content=models.Namespace(
                path="/",
                public_key=root_namespace_private_key.public_key,
                verify_key=root_namespace_signing_key.verify_key,
            ),
        )

        signed_public_namespace_grant = models.SignedSharedNamespaceGrant.sign(
            notary=workspace_keyspace_signing_key,
            content=models.SharedNamespaceGrant.encrypt(
                provider=workspace_keyspace_private_key,
                recipient=workspace_keyspace_private_key.public_key,
                encrypted=models.NamespaceGrantCredentials(
                    private_key=root_namespace_private_key, signing_key=root_namespace_signing_key
                ),
                plain=models.NamespaceGrant(
                    permissions=set(enums.KeyspacePermission),
                    recipient=models.NamespaceGrantRecipient(("workspace", workspace.identify())),
                ),
            ),
        )

        data = protocol.CreateWorkspaceIngress(
            workspace=signed_workspace,
            workspace_grant=signed_public_workspace_grant,
            namespace=signed_root_namespace,
            namespace_grant=signed_public_namespace_grant,
        )

        await self._origin.react(action="create_workspace", data=data)

        try:
            await self._user_client.trust(workspace)
        except:
            await self.delete()
            raise

    @endpoint(action="fetch_workspace", ingress=protocol.WorkspaceBound, egress=protocol.FetchWorkspaceEgress)
    async def _fetch_raw(self) -> (models.SignedWorkspace, typing.List[models.SignedSharedWorkspaceGrant]):
        response: protocol.FetchWorkspaceEgress = await self._origin.react(
            action="fetch_workspace", data=protocol.WorkspaceBound(workspace_name=self.name)
        )
        return response.workspace, response.workspace_grants

    async def fetch(self) -> models.Workspace:
        signed_workspace, _ = await self._fetch_raw()
        return self._trust.authenticate_workspace(signed_workspace)

    async def share_identity(self) -> str:
        workspace, _ = await self._fetch_raw()
        identity_token = workspace.encode()
        return encode_token(identity_token, prefix="bbw_")

    @staticmethod
    def load_identity(identity_token: str) -> models.Workspace:
        recipient: bytes = decode_token(identity_token, "bbw_")
        recipient: models.SignedWorkspace = models.SignedWorkspace.decode(recipient)
        return recipient.verify(expected_notary=recipient.notary)

    async def list_grants(self) -> typing.List[models.SharedWorkspaceGrant]:
        signed_workspace, signed_workspace_grants = await self._fetch_raw()
        verified_workspace: models.Workspace = self._trust.authenticate_workspace(signed_workspace)

        return [
            self._trust.authenticate_workspace_grant(verified_workspace, signed_workspace_grant)
            for signed_workspace_grant in signed_workspace_grants
        ]

    @endpoint(action="delete_workspace", ingress=protocol.WorkspaceBound)
    async def delete(self) -> None:
        await self._origin.react(action="delete_workspace", data=protocol.WorkspaceBound(workspace_name=self.name))

    @endpoint(
        action="fetch_workspace_grant",
        ingress=protocol.FetchWorkspaceGrantIngress,
        egress=protocol.FetchWorkspaceGrantEgress,
    )
    async def fetch_grant(self, user_name: str) -> models.SharedWorkspaceGrant:
        response: protocol.FetchWorkspaceGrantEgress = await self._origin.react(
            action="fetch_workspace_grant",
            data=protocol.FetchWorkspaceGrantIngress(
                workspace_name=self.name, data=protocol.WorkspaceGrantUserReference(user_name=user_name)
            ),
        )

        verified_workspace: models.Workspace = self._trust.authenticate_workspace(response.workspace)
        verified_grant: models.SharedWorkspaceGrant = self._trust.authenticate_workspace_grant(
            verified_workspace, response.workspace_grant
        )
        _, recipient = verified_grant.plain.recipient
        assert recipient.name == user_name, "Grant does not belong to username"
        return verified_grant

    @endpoint(action="create_workspace_grant", ingress=protocol.CreateWorkspaceGrantIngress)
    async def trust(self, user: models.User, access: typing.Set[enums.WorkspacePermission] = None):
        # Not specifying an access level results in an empty grant
        access = access or set()
        credentials = None

        for grant in await self.list_grants():
            if grant.recipient != self._trust.user.public_key:
                continue

            # TODO: Provider should always be the workspace's public key; Cache and statically retrieve this?
            credentials = self._trust.private_key_enclave.decrypt_envelope(grant, expected_provider=grant.provider)
            break

        assert credentials is not None, "Missing user workspace credentials"

        granted_credentials = models.WorkspaceGrantCredentials(
            private_key=None, signing_key=None, keyspace_private_key=None, keyspace_signing_key=None
        )

        if enums.WorkspacePermission.MANAGE_WORKSPACE in access:
            assert credentials.private_key is not None
            assert credentials.signing_key is not None
            granted_credentials.private_key = credentials.private_key
            granted_credentials.signing_key = credentials.signing_key

        if enums.WorkspacePermission.MANAGE_KEYSPACE in access:
            assert credentials.keyspace_private_key is not None
            assert credentials.keyspace_signing_key is not None
            granted_credentials.keyspace_private_key = credentials.keyspace_private_key
            granted_credentials.keyspace_signing_key = credentials.keyspace_signing_key

        signed_public_workspace_grant = models.SignedSharedWorkspaceGrant.sign(
            notary=credentials.signing_key,
            content=models.SharedWorkspaceGrant.encrypt(
                provider=credentials.private_key,
                recipient=user.public_key,
                encrypted=granted_credentials,
                plain=models.WorkspaceGrant(
                    permissions=access,
                    recipient=models.WorkspaceGrantRecipient(("user", user.identify())),
                ),
            ),
        )

        await self._origin.react(
            action="create_workspace_grant",
            data=protocol.CreateWorkspaceGrantIngress(workspace_name=self.name, data=signed_public_workspace_grant),
        )

    @endpoint(action="delete_workspace_grant", ingress=protocol.DeleteWorkspaceGrantIngress)
    async def untrust(self, user_name: str):
        await self._origin.react(
            action="delete_workspace_grant",
            data=protocol.DeleteWorkspaceGrantIngress(
                workspace_name=self.name,
                data=protocol.WorkspaceGrantUserReference(user_name=user_name),
            ),
        )
