from backbone.common import enums

from ._containers import *
from .namespace import NamespaceIdentity
from .user import UserIdentity
from .workspace import WorkspaceIdentity


class NamespaceGrantRecipient(cord.Variant):
    user = cord.RecordField(UserIdentity)
    workspace = cord.RecordField(WorkspaceIdentity)
    namespace = cord.RecordField(NamespaceIdentity)


class NamespaceGrant(cord.Record):
    permissions: typing.Set[enums.KeyspacePermission] = cord.SetField(cord.EnumField(enums.KeyspacePermission))
    recipient: NamespaceGrantRecipient = cord.VariantField(NamespaceGrantRecipient)


class NamespaceGrantCredentials(cord.Record):
    private_key: typing.Optional[PrivateKey] = cord.OptionalField(cord.PrivateKeyField())
    signing_key: typing.Optional[SigningKey] = cord.OptionalField(cord.SigningKeyField())


class SharedNamespaceGrant(SharedEnvelope):
    plain: NamespaceGrant = cord.RecordField(NamespaceGrant)
    _encrypted: bytes = cord.EncryptedField(NamespaceGrantCredentials)


class SignedSharedNamespaceGrant(SignedEnvelope):
    _content: SharedNamespaceGrant = cord.RecordField(SharedNamespaceGrant)
