import base64
import typing

from backbone.common import models, protocol

from ._decorators import endpoint
from ._origin import Origin
from ._security import Trust
from ._utils import decode_token, encode_token


class UserClient:
    def __init__(self, trust: Trust, origin: Origin):
        self._trust = trust
        self._origin = origin

    @endpoint(action="create_user", ingress=protocol.CreateUserIngress)
    def create(self) -> None:
        """Create a user"""
        signed_secret_user = self._trust.signing_key_enclave.sign_envelope(
            record_cls=models.SignedUser, content=self._trust.user
        )

        self._origin.react(action="create_user", data=protocol.CreateUserIngress(user=signed_secret_user))

    @endpoint(action="fetch_self", egress=protocol.FetchSelfEgress)
    def fetch_self(self) -> models.User:
        """Fetch and verify the current user's details"""
        result: protocol.FetchSelfEgress = self._origin.react(action="fetch_self")
        self._trust.bootstrap(result.user)
        return self._trust.user

    def share_identity(self) -> str:
        result: protocol.FetchSelfEgress = self._origin.react(action="fetch_self")
        identity_token = result.user.encode()
        return encode_token(identity_token, prefix="bbu_")

    @staticmethod
    def load_identity(identity_token: str) -> models.User:
        recipient: bytes = decode_token(identity_token, "bbu_")
        recipient: models.SignedUser = models.SignedUser.decode(recipient)
        return recipient.verify(expected_notary=recipient.notary)

    @endpoint(action="update_user", ingress=protocol.UpdateUserIngress)
    def update(self, trusted_workspaces: typing.List[models.WorkspaceIdentity]):
        new_user = models.User(**self._trust.user)
        new_user.trusted_workspaces = trusted_workspaces
        new_signed_user: models.SignedUser = self._trust.signing_key_enclave.sign_envelope(
            record_cls=models.SignedUser, content=new_user
        )

        self._origin.react(
            action="update_user",
            data=protocol.UpdateUserIngress(user=new_signed_user),
        )

        self._trust.bootstrap(new_signed_user)

    def trust(self, workspace: models.Workspace):
        workspace_identity = workspace.identify()
        new_trusted_workspaces = self._trust.user.trusted_workspaces[:]
        new_trusted_workspaces.append(workspace_identity)

        self.update(new_trusted_workspaces)

    def untrust(self, workspace: models.Workspace):
        new_trusted_workspaces = [
            candidate_workspace
            for candidate_workspace in self._trust.user.trusted_workspaces
            if candidate_workspace != workspace
        ]

        self.update(new_trusted_workspaces)

    @endpoint(action="delete_self")
    def delete(self) -> None:
        """Delete the current user from backbone"""
        self._origin.react(action="delete_self")
