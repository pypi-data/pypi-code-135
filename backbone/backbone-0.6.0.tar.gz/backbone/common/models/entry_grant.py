from backbone.common import enums

from ._containers import *
from .namespace import NamespaceIdentity
from .user import UserIdentity
from .workspace import WorkspaceIdentity


class EntryGrantRecipient(cord.Variant):
    user = cord.RecordField(UserIdentity)
    workspace = cord.RecordField(WorkspaceIdentity)
    namespace = cord.RecordField(NamespaceIdentity)


class EntryGrant(cord.Record):
    permissions: typing.Set[enums.KeyspacePermission] = cord.SetField(cord.EnumField(enums.KeyspacePermission))
    recipient: EntryGrantRecipient = cord.VariantField(EntryGrantRecipient)


class EntryGrantCredentials(cord.Record):
    private_key: typing.Optional[PrivateKey] = cord.OptionalField(cord.PrivateKeyField())
    signing_key: typing.Optional[SigningKey] = cord.OptionalField(cord.SigningKeyField())


class SharedEntryGrant(SharedEnvelope):
    plain: EntryGrant = cord.RecordField(EntryGrant)
    _encrypted: bytes = cord.EncryptedField(EntryGrantCredentials)


class SignedSharedEntryGrant(SignedEnvelope):
    _content: SharedEntryGrant = cord.RecordField(SharedEntryGrant)
