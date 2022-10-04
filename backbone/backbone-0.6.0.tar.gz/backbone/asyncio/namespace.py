import typing

from nacl.public import PrivateKey
from nacl.signing import SigningKey

from backbone.common import enums, keyspace, models, protocol, service

from ._decorators import endpoint
from ._origin import Origin
from ._security import Trust

if typing.TYPE_CHECKING:
    from .workspace import WorkspaceClient


class NamespaceClient:
    def __init__(self, trust: Trust, origin: Origin, workspace_client: "WorkspaceClient"):
        self._trust = trust
        self._origin = origin
        self._workspace_client = workspace_client

    @endpoint(action="create_namespace", ingress=protocol.CreateWorkspaceNamespaceIngress)
    async def create(self, path: str, *, recursive: bool = False) -> None:
        if not recursive:
            return await self._create(path)

        path = keyspace.Path.from_path(path)
        for partial_path in path.chain():
            try:
                await self._fetch_raw(partial_path.resolve())
            except service.Error:
                await self._create(partial_path.resolve())

    async def _create(self, path: str) -> None:
        path = keyspace.Path.from_path(path)
        parent, _, parent_credentials = await self._fetch_raw(path.parent.resolve())

        namespace_private_key: PrivateKey = PrivateKey.generate()
        namespace_signing_key: SigningKey = SigningKey.generate()

        signed_public_namespace_grant = models.SignedSharedNamespaceGrant.sign(
            notary=parent_credentials.signing_key,
            content=models.SharedNamespaceGrant.encrypt(
                provider=parent_credentials.private_key,
                recipient=parent_credentials.private_key.public_key,
                encrypted=models.NamespaceGrantCredentials(
                    private_key=namespace_private_key, signing_key=namespace_signing_key
                ),
                plain=models.NamespaceGrant(
                    permissions=set(enums.KeyspacePermission),
                    recipient=models.NamespaceGrantRecipient(("namespace", parent.identify())),
                ),
            ),
        )

        signed_namespace = models.SignedNamespace.sign(
            notary=parent_credentials.signing_key,
            content=models.Namespace(
                path=path.resolve(),
                public_key=namespace_private_key.public_key,
                verify_key=namespace_signing_key.verify_key,
            ),
        )

        await self._origin.react(
            action="create_namespace",
            data=protocol.CreateWorkspaceNamespaceIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.CreateNamespaceIngress(
                    namespace=signed_namespace, namespace_grant=signed_public_namespace_grant
                ),
            ),
        )

    @endpoint(
        action="fetch_namespace",
        ingress=protocol.FetchWorkspaceNamespaceChainIngress,
        egress=protocol.FetchNamespaceChainEgress,
    )
    async def _fetch_raw(
        self, path: str
    ) -> (models.Namespace, models.NamespaceGrant, models.NamespaceGrantCredentials):
        path = keyspace.Path.from_path(path)

        response: protocol.FetchNamespaceChainEgress = await self._origin.react(
            action="fetch_namespace",
            data=protocol.FetchWorkspaceNamespaceChainIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.FetchNamespaceChainIngress(path=path.resolve()),
            ),
        )

        return self._trust.decrypt_namespace_chain(response.namespace_chain)

    @endpoint(
        action="list_namespace_children",
        ingress=protocol.ListWorkspaceNamespaceChildrenIngress,
        egress=protocol.ListNamespaceChildrenEgress,
    )
    async def list_children(self, path: str) -> typing.List[typing.Union[models.Namespace, models.Entry]]:
        path = keyspace.Path.from_path(path)
        response: protocol.ListNamespaceChildrenEgress = await self._origin.react(
            action="list_namespace_children",
            data=protocol.ListWorkspaceNamespaceChildrenIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.ListNamespaceChildrenIngress(path=path.resolve()),
            ),
        )

        parent_namespace, _, _ = self._trust.decrypt_namespace_chain(response.parent_chain)
        results = []
        results.extend(
            [self._trust.authenticate_namespace(parent_namespace, namespace) for namespace in response.namespaces]
        )
        results.extend([self._trust.authenticate_entry(parent_namespace, entry) for entry in response.entries])
        return results

    @endpoint(action="delete_namespace", ingress=protocol.DeleteWorkspaceNamespaceIngress)
    async def delete(self, path: str) -> None:
        path = keyspace.Path.from_path(path)
        await self._origin.react(
            action="delete_namespace",
            data=protocol.DeleteWorkspaceNamespaceIngress(
                workspace_name=self._workspace_client.name, data=protocol.DeleteNamespaceIngress(path=path.resolve())
            ),
        )

    @endpoint(action="create_namespace_grant", ingress=protocol.CreateWorkspaceNamespaceGrantIngress)
    async def grant(
        self,
        path: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
        access: typing.Set[enums.KeyspacePermission] = None,
    ) -> None:
        access = access or set()
        path = keyspace.Path.from_path(path)
        _, _, parent_namespace_credentials = await self._workspace_client.namespace._fetch_raw(path.parent.resolve())
        _, _, namespace_credentials = await self._workspace_client.namespace._fetch_raw(path.resolve())

        recipient_variant = self._grant_recipient(recipient)
        granted_credentials = models.NamespaceGrantCredentials(private_key=None, signing_key=None)

        if enums.KeyspacePermission.READ in access:
            assert namespace_credentials.private_key is not None
            granted_credentials.private_key = namespace_credentials.private_key
        if enums.KeyspacePermission.CREATE in access or enums.KeyspacePermission.UPDATE in access:
            assert namespace_credentials.signing_key is not None
            granted_credentials.signing_key = namespace_credentials.signing_key

        signed_public_namespace_grant = models.SignedSharedNamespaceGrant.sign(
            notary=parent_namespace_credentials.signing_key,
            content=models.SharedNamespaceGrant.encrypt(
                provider=parent_namespace_credentials.private_key,
                recipient=recipient.public_key,
                encrypted=granted_credentials,
                plain=models.NamespaceGrant(permissions=access, recipient=recipient_variant),
            ),
        )

        await self._origin.react(
            action="create_namespace_grant",
            data=protocol.CreateWorkspaceNamespaceGrantIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.CreateNamespaceGrantIngress(
                    path=path.resolve(), namespace_grant=signed_public_namespace_grant
                ),
            ),
        )

    @endpoint(
        action="list_namespace_grants",
        ingress=protocol.ListWorkspaceNamespaceGrantsIngress,
        egress=protocol.ListNamespaceGrantsEgress,
    )
    async def list_grants(self, path: str) -> typing.List[models.NamespaceGrant]:
        path = keyspace.Path.from_path(path)

        response: protocol.ListNamespaceGrantsEgress = await self._origin.react(
            action="list_namespace_grants",
            data=protocol.ListWorkspaceNamespaceGrantsIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.ListNamespaceGrantsIngress(path=path.resolve()),
            ),
        )

        parent_namespace, _, _ = self._trust.decrypt_namespace_chain(response.parent_chain)
        verified_shared_namespace_grants = self._trust.authenticate_namespace_grants(
            parent_namespace, response.namespace_grants
        )
        return [namespace_grant.plain for namespace_grant in verified_shared_namespace_grants]

    @endpoint(action="delete_namespace_grant", ingress=protocol.DeleteWorkspaceNamespaceGrantIngress)
    async def revoke(
        self,
        path: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
    ) -> None:
        path = keyspace.Path.from_path(path)
        recipient_variant = self._grant_recipient(recipient)

        await self._origin.react(
            action="delete_namespace_grant",
            data=protocol.DeleteWorkspaceNamespaceGrantIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.DeleteNamespaceGrantIngress(path=path.resolve(), recipient=recipient_variant),
            ),
        )

    @staticmethod
    def _grant_recipient(
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity]
    ) -> models.NamespaceGrantRecipient:
        if isinstance(recipient, models.Identifiable):
            # Handles case where a subclass of an identity type is passed; e.g. Workspace | Namespace | User
            recipient = recipient.identify()

        if isinstance(recipient, models.NamespaceIdentity):
            return models.NamespaceGrantRecipient(("namespace", recipient))
        elif isinstance(recipient, models.WorkspaceIdentity):
            return models.NamespaceGrantRecipient(("workspace", recipient))
        elif isinstance(recipient, models.UserIdentity):
            return models.NamespaceGrantRecipient(("user", recipient))
        else:
            raise ValueError("Invalid recipient")
