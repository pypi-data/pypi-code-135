from datetime import datetime

from ._containers import *


class Entry(cord.Record):
    path: str = cord.StringField()
    public_key: PublicKey = cord.PublicKeyField()
    verify_key: VerifyKey = cord.VerifyKeyField()
    expiration: typing.Optional[datetime] = cord.OptionalField(cord.DateTimeField())


class SignedEntry(SignedEnvelope):
    _content: Entry = cord.RecordField(Entry)


class EntryContent(cord.Record):
    value: bytes = cord.BytesField()


class SharedEntryContent(SharedEnvelope):
    plain: None = cord.NullField()
    _encrypted: bytes = cord.EncryptedField(EntryContent)


class SignedSharedEntryContent(SignedEnvelope):
    _content: SharedEntryContent = cord.RecordField(SharedEntryContent)


class EntryEnvelope(cord.Record):
    metadata: SignedEntry = cord.RecordField(SignedEntry)
    content: SignedSharedEntryContent = cord.RecordField(SignedSharedEntryContent)
