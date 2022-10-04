from ._containers import *


class StreamBytes(cord.Record):
    value: bytes = cord.BytesField()


class SharedStreamBytes(SharedEnvelope):
    plain: None = cord.NullField()
    _encrypted: bytes = cord.EncryptedField(StreamBytes)


class SignedSharedStreamBytes(SignedEnvelope):
    _content: SharedStreamBytes = cord.RecordField(SharedStreamBytes)
