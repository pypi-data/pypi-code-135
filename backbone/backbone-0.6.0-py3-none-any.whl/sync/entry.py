import typing
from datetime import datetime, timedelta, timezone

from nacl.public import PrivateKey
from nacl.signing import SigningKey

from backbone.common import enums, keyspace, models, protocol, service

from ._decorators import endpoint
from ._origin import Origin
from ._security import Trust

if typing.TYPE_CHECKING:
    from .workspace import WorkspaceClient


class EntryClient:
    def __init__(self, trust: Trust, origin: Origin, workspace_client: "WorkspaceClient"):
        self._trust = trust
        self._origin = origin
        self._workspace_client = workspace_client

    @endpoint(action="set_entry", ingress=protocol.SetWorkspaceEntryIngress)
    def set_bytes(self, path: str, value: bytes, duration_ms: typing.Optional[int] = None) -> None:
        assert isinstance(value, bytes), "Value must be a byte array"
        assert isinstance(duration_ms, (type(None), int)), "Duration must be an integer if defined"
        path = keyspace.Path.from_path(path)

        try:
            _, _, _, existing_entry_credentials = self._fetch_raw(path.resolve())
        except service.Error:
            existing_entry_credentials: typing.Optional[models.EntryGrantCredentials] = None

        parent, _, parent_credentials = self._workspace_client.namespace._fetch_raw(path.parent.resolve())

        entry_private_key: typing.Optional[PrivateKey] = (
            existing_entry_credentials.private_key if existing_entry_credentials else PrivateKey.generate()
        )
        entry_signing_key: typing.Optional[SigningKey] = (
            existing_entry_credentials.signing_key if existing_entry_credentials else SigningKey.generate()
        )

        signed_public_entry_grant = models.SignedSharedEntryGrant.sign(
            notary=parent_credentials.signing_key,
            content=models.SharedEntryGrant.encrypt(
                provider=parent_credentials.private_key,
                recipient=parent_credentials.private_key.public_key,
                encrypted=models.EntryGrantCredentials(private_key=entry_private_key, signing_key=entry_signing_key),
                plain=models.EntryGrant(
                    permissions=set(enums.KeyspacePermission),
                    recipient=models.NamespaceGrantRecipient(("namespace", parent.identify())),
                ),
            ),
        )

        signed_entry = models.EntryEnvelope(
            metadata=models.SignedEntry.sign(
                notary=parent_credentials.signing_key,
                content=models.Entry(
                    path=path.resolve(),
                    public_key=entry_private_key.public_key,
                    verify_key=entry_signing_key.verify_key,
                    expiration=duration_ms and datetime.now(tz=timezone.utc) + timedelta(milliseconds=duration_ms),
                ),
            ),
            content=models.SignedSharedEntryContent.sign(
                notary=entry_signing_key,
                content=models.SharedEntryContent.encrypt(
                    provider=entry_private_key,
                    recipient=entry_private_key.public_key,
                    encrypted=models.EntryContent(value=value),
                    plain=None,
                ),
            ),
        )

        self._origin.react(
            action="set_entry",
            data=protocol.SetWorkspaceEntryIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.SetEntryIngress(entry=signed_entry, entry_grant=signed_public_entry_grant),
            ),
        )

    def set(self, path: str, value: str, duration_ms: typing.Optional[int] = None) -> None:
        assert isinstance(value, str), "Value must be a string"
        return self.set_bytes(path, value.encode("utf-8"), duration_ms=duration_ms)

    @endpoint(
        action="fetch_entry",
        ingress=protocol.FetchWorkspaceEntryChainIngress,
        egress=protocol.FetchEntryChainEgress,
    )
    def _fetch_raw(
        self, path: str
    ) -> (models.Entry, models.SharedEntryContent, models.EntryGrant, models.EntryGrantCredentials):
        path = keyspace.Path.from_path(path)

        response: protocol.FetchEntryChainEgress = self._origin.react(
            action="fetch_entry",
            data=protocol.FetchWorkspaceEntryChainIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.FetchEntryChainIngress(path=path.resolve()),
            ),
        )

        return self._trust.decrypt_entry_chain(response.entry_chain)

    def get_bytes(self, path: str) -> bytes:
        entry: models.Entry
        encrypted_content: models.SharedEntryContent
        entry_credentials: models.EntryGrantCredentials
        entry, encrypted_content, _, entry_credentials = self._fetch_raw(path)
        entry_content: models.EntryContent = encrypted_content.decrypt(
            entry_credentials.private_key, expected_provider=entry.public_key
        )
        return entry_content.value

    def get(self, path: str) -> str:
        entry_bytes = self.get_bytes(path)
        return entry_bytes.decode("utf-8")

    @endpoint(action="delete_entry", ingress=protocol.DeleteWorkspaceEntryIngress)
    def delete(self, path: str) -> None:
        path = keyspace.Path.from_path(path)

        self._origin.react(
            action="delete_entry",
            data=protocol.DeleteWorkspaceEntryIngress(
                workspace_name=self._workspace_client.name, data=protocol.DeleteEntryIngress(path=path.resolve())
            ),
        )

    @endpoint(action="create_entry_grant", ingress=protocol.CreateWorkspaceEntryGrantIngress)
    def grant(
        self,
        path: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
        access: typing.Set[enums.KeyspacePermission] = None,
    ) -> None:
        access = access or set()
        path = keyspace.Path.from_path(path)
        _, _, parent_namespace_credentials = self._workspace_client.namespace._fetch_raw(path.parent.resolve())
        _, _, _, entry_credentials = self._fetch_raw(path.resolve())

        recipient_variant = self._grant_recipient(recipient)
        granted_credentials = models.EntryGrantCredentials(private_key=None, signing_key=None)

        if enums.KeyspacePermission.READ in access:
            assert entry_credentials.private_key is not None
            granted_credentials.private_key = entry_credentials.private_key
        if enums.KeyspacePermission.CREATE in access or enums.KeyspacePermission.UPDATE in access:
            assert entry_credentials.signing_key is not None
            granted_credentials.signing_key = entry_credentials.signing_key

        signed_public_entry_grant = models.SignedSharedEntryGrant.sign(
            notary=parent_namespace_credentials.signing_key,
            content=models.SharedEntryGrant.encrypt(
                provider=parent_namespace_credentials.private_key,
                recipient=recipient.public_key,
                encrypted=granted_credentials,
                plain=models.EntryGrant(permissions=access, recipient=recipient_variant),
            ),
        )

        self._origin.react(
            action="create_entry_grant",
            data=protocol.CreateWorkspaceEntryGrantIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.CreateEntryGrantIngress(path=path.resolve(), entry_grant=signed_public_entry_grant),
            ),
        )

    @endpoint(
        action="list_entry_grants",
        ingress=protocol.ListWorkspaceEntryGrantsIngress,
        egress=protocol.ListEntryGrantsEgress,
    )
    def list_grants(self, path: str) -> typing.List[models.EntryGrant]:
        path = keyspace.Path.from_path(path)

        response: protocol.ListEntryGrantsEgress = self._origin.react(
            action="list_entry_grants",
            data=protocol.ListWorkspaceEntryGrantsIngress(
                workspace_name=self._workspace_client.name, data=protocol.ListEntryGrantsIngress(path=path.resolve())
            ),
        )

        parent_namespace, _, _ = self._trust.decrypt_namespace_chain(response.parent_chain)
        verified_shared_entry_grants = self._trust.authenticate_entry_grants(parent_namespace, response.entry_grants)
        return [entry_grant.plain for entry_grant in verified_shared_entry_grants]

    @endpoint(action="delete_entry_grant", ingress=protocol.DeleteWorkspaceEntryGrantIngress)
    def revoke(
        self,
        path: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
    ) -> None:
        path = keyspace.Path.from_path(path)
        recipient_variant = self._grant_recipient(recipient)

        self._origin.react(
            action="delete_entry_grant",
            data=protocol.DeleteWorkspaceEntryGrantIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.DeleteEntryGrantIngress(path=path.resolve(), recipient=recipient_variant),
            ),
        )

    @staticmethod
    def _grant_recipient(
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity]
    ) -> models.EntryGrantRecipient:
        if isinstance(recipient, models.Identifiable):
            # Handles case where a subclass of an identity type is passed; e.g. Workspace | Namespace | User
            recipient = recipient.identify()

        if isinstance(recipient, models.NamespaceIdentity):
            return models.EntryGrantRecipient(("namespace", recipient))
        elif isinstance(recipient, models.WorkspaceIdentity):
            return models.EntryGrantRecipient(("workspace", recipient))
        elif isinstance(recipient, models.UserIdentity):
            return models.EntryGrantRecipient(("user", recipient))
        else:
            raise ValueError("Invalid recipient")
