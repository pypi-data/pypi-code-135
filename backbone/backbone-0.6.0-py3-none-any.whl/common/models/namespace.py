from ._containers import *


class NamespaceIdentity(cord.Record):
    path: str = cord.StringField()
    public_key: PublicKey = cord.PublicKeyField()
    verify_key: VerifyKey = cord.VerifyKeyField()


class Namespace(Identifiable, NamespaceIdentity):
    def identify(self) -> NamespaceIdentity:
        return NamespaceIdentity(path=self.path, public_key=self.public_key, verify_key=self.verify_key)


class SignedNamespace(SignedEnvelope):
    _content: Namespace = cord.RecordField(Namespace)
