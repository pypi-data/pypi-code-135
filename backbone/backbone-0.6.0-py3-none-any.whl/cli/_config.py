import typing

from nacl.public import PrivateKey
from nacl.signing import SigningKey

from backbone.common import cord, models
from backbone.sync import Trust


class LocalConfiguration(cord.Record):
    user_name: str = cord.StringField()
    secret_key: bytes = cord.BytesField()
    private_key: PrivateKey = cord.PrivateKeyField()
    signing_key: SigningKey = cord.SigningKeyField()
    workspace_name: typing.Optional[str] = cord.OptionalField(cord.StringField())

    @classmethod
    def from_master_secret(cls, user_name: str, master_secret: typing.Union[str, bytes]) -> "LocalConfiguration":
        secret_key, private_key, signing_key = Trust.derive_secrets(user_name=user_name, master_secret=master_secret)

        return cls(
            user_name=user_name,
            secret_key=secret_key,
            private_key=private_key,
            signing_key=signing_key,
            workspace_name=None,
        )


class EncryptedLocalConfiguration(models.SecretEnvelope):
    plain: None = cord.NullField()
    _encrypted: bytes = cord.EncryptedField(LocalConfiguration)
