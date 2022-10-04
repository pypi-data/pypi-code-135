from ._containers import *


class WorkspaceIdentity(cord.Record):
    name: str = cord.StringField()
    public_key: PublicKey = cord.PublicKeyField()
    verify_key: VerifyKey = cord.VerifyKeyField()

    def __eq__(self, other: "WorkspaceIdentity"):
        assert isinstance(other, WorkspaceIdentity)
        return self.name == other.name or self.public_key == other.public_key or self.verify_key == other.verify_key


class Workspace(Identifiable, WorkspaceIdentity):
    keyspace_public_key: PublicKey = cord.PublicKeyField()
    keyspace_verify_key: VerifyKey = cord.VerifyKeyField()

    def identify(self) -> WorkspaceIdentity:
        return WorkspaceIdentity(name=self.name, public_key=self.public_key, verify_key=self.verify_key)

    def __eq__(self, other: "Workspace"):
        assert isinstance(other, Workspace)
        return self.identify() == other.identify()


class SignedWorkspace(SignedEnvelope):
    _content: Workspace = cord.RecordField(Workspace)
