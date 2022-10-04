import typing

from backbone.common import enums, keyspace, models, protocol

from ._decorators import endpoint
from ._origin import Origin
from ._security import Trust

if typing.TYPE_CHECKING:
    from .workspace import WorkspaceClient


class StreamClient:
    def __init__(self, trust: Trust, origin: Origin, workspace_client: "WorkspaceClient"):
        self._trust = trust
        self._origin = origin
        self._workspace_client = workspace_client

    def create(self, stream: str) -> None:
        self._workspace_client.namespace.create(keyspace.SERVICE_STREAM_PATH.resolve(), recursive=True)

        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        self._workspace_client.entry.set(stream_path.resolve(), "")

    @endpoint(action="publish_stream", ingress=protocol.PublishWorkspaceStreamIngress)
    def publish(self, stream: str, *payloads: bytes) -> None:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        _, _, _, existing_entry_credentials = self._workspace_client.entry._fetch_raw(stream_path.resolve())

        results: typing.List[models.SignedSharedStreamBytes] = []
        for payload in payloads:
            signed_shared_stream_bytes = models.SignedSharedStreamBytes.sign(
                notary=existing_entry_credentials.signing_key,
                content=models.SharedStreamBytes.encrypt(
                    provider=existing_entry_credentials.private_key,
                    recipient=existing_entry_credentials.private_key.public_key,
                    encrypted=models.StreamBytes(value=payload),
                    plain=None,
                ),
            )

            results.append(signed_shared_stream_bytes)

        self._origin.react(
            action="publish_stream",
            data=protocol.PublishWorkspaceStreamIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.PublishStreamIngress(
                    stream_name=stream, data=protocol.PublishStreamIngressData(data=results)
                ),
            ),
        )

    @endpoint(
        action="consume_stream", ingress=protocol.ConsumeWorkspaceStreamIngress, egress=protocol.ConsumeStreamEgress
    )
    def consume(self, stream: str, batch: int, *, shared: bool = False) -> typing.List[bytes]:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream

        entry, _, _, existing_entry_credentials = self._workspace_client.entry._fetch_raw(stream_path.resolve())

        response: protocol.ConsumeStreamEgress = self._origin.react(
            action="consume_stream",
            data=protocol.ConsumeWorkspaceStreamIngress(
                workspace_name=self._workspace_client.name,
                data=protocol.ConsumeStreamIngress(
                    stream_name=stream, data=protocol.ConsumeStreamIngressMetadata(shared=shared, batch=batch)
                ),
            ),
        )

        results: typing.List[bytes] = []
        for signed_shared_message in response.data:
            shared_message: models.SharedStreamBytes = signed_shared_message.verify(entry.verify_key)
            payload: models.StreamBytes = shared_message.decrypt(
                existing_entry_credentials.private_key, existing_entry_credentials.private_key.public_key
            )
            results.append(payload.value)

        return results

    def delete(self, stream: str) -> None:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        self._workspace_client.entry.delete(stream_path.resolve())

    def grant(
        self,
        stream: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
        access: typing.Set[enums.KeyspacePermission] = None,
    ) -> None:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        self._workspace_client.entry.grant(stream_path.resolve(), recipient, access)

    def list_grants(self, stream: str) -> typing.List[models.EntryGrant]:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        return self._workspace_client.entry.list_grants(stream_path.resolve())

    def revoke(
        self,
        stream: str,
        recipient: typing.Union[models.NamespaceIdentity, models.WorkspaceIdentity, models.UserIdentity],
    ) -> None:
        stream_path: keyspace.Path = keyspace.SERVICE_STREAM_PATH / stream
        return self._workspace_client.entry.untrust(stream_path.resolve(), recipient)
