from ._containers import *
from .workspace import WorkspaceIdentity


class UserIdentity(cord.Record):
    name: str = cord.StringField()
    public_key: PublicKey = cord.PublicKeyField()
    verify_key: VerifyKey = cord.VerifyKeyField()


class User(Identifiable, UserIdentity):
    trusted_workspaces: typing.List[WorkspaceIdentity] = cord.ListField(cord.RecordField(WorkspaceIdentity))

    def identify(self) -> UserIdentity:
        return UserIdentity(name=self.name, public_key=self.public_key, verify_key=self.verify_key)


class SignedUser(SignedEnvelope):
    _content: User = cord.RecordField(User)
