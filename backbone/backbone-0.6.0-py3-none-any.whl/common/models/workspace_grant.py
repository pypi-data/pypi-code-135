from backbone.common import enums

from ._containers import *
from .user import UserIdentity


class WorkspaceGrantRecipient(cord.Variant):
    user = cord.RecordField(UserIdentity)


class WorkspaceGrant(cord.Record):
    permissions: typing.Set[enums.WorkspacePermission] = cord.SetField(cord.EnumField(enums.WorkspacePermission))
    recipient: WorkspaceGrantRecipient = cord.VariantField(WorkspaceGrantRecipient)


class WorkspaceGrantCredentials(cord.Record):
    private_key: typing.Optional[PrivateKey] = cord.OptionalField(cord.PrivateKeyField())
    signing_key: typing.Optional[SigningKey] = cord.OptionalField(cord.SigningKeyField())

    keyspace_private_key: typing.Optional[PrivateKey] = cord.OptionalField(cord.PrivateKeyField())
    keyspace_signing_key: typing.Optional[SigningKey] = cord.OptionalField(cord.SigningKeyField())


class SharedWorkspaceGrant(SharedEnvelope):
    plain: WorkspaceGrant = cord.RecordField(WorkspaceGrant)
    _encrypted: bytes = cord.EncryptedField(WorkspaceGrantCredentials)


class SignedSharedWorkspaceGrant(SignedEnvelope):
    _content: SharedWorkspaceGrant = cord.RecordField(SharedWorkspaceGrant)
