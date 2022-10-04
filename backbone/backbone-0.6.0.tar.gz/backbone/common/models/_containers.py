import abc
import typing

from nacl.public import Box, PrivateKey, PublicKey
from nacl.secret import SecretBox
from nacl.signing import SigningKey, VerifyKey

from backbone.common import cord
from backbone.common.exceptions import CryptographyError

T = typing.TypeVar("T", bound=cord.Record)


class SignedEnvelope(cord.Record, abc.ABC):
    _content: T
    notary: VerifyKey = cord.VerifyKeyField()
    _signature: bytes = cord.BytesField()

    @classmethod
    def sign(cls, notary: SigningKey, content: cord.Record) -> "SignedEnvelope":
        encoded = content.encode()
        signed = notary.sign(encoded)
        return cls(notary=notary.verify_key, _signature=signed.signature, _content=content)

    def verify(self, expected_notary: VerifyKey) -> T:
        if self.notary != expected_notary:
            raise CryptographyError("Invalid notary")

        encoded = self._content.encode()

        try:
            self.notary.verify(encoded, self._signature)
        except Exception as e:
            raise CryptographyError("Invalid signature") from e

        return self._content


class SharedEnvelope(cord.Record, abc.ABC):
    plain: T
    _encrypted: bytes
    provider: PublicKey = cord.PublicKeyField()
    recipient: PublicKey = cord.PublicKeyField()

    @classmethod
    def encrypt(
        cls, provider: PrivateKey, recipient: PublicKey, encrypted: cord.Record, plain: typing.Any
    ) -> "SharedEnvelope":
        encoded = encrypted.encode()
        encrypted = Box(provider, recipient).encrypt(encoded)
        return cls(provider=provider.public_key, recipient=recipient, plain=plain, _encrypted=encrypted)

    def decrypt(self, recipient: PrivateKey, expected_provider: PublicKey) -> T:
        if self.provider != expected_provider:
            raise CryptographyError("Invalid provider")

        if self.recipient != recipient.public_key:
            raise CryptographyError("Invalid recipient")

        try:
            decrypted = Box(recipient, self.provider).decrypt(self._encrypted)
            field: cord.EncryptedField = self.fields["_encrypted"]  # noqa
            return field.record_cls.decode(decrypted)
        except:
            raise CryptographyError("Decryption failed")


class SecretEnvelope(cord.Record, abc.ABC):
    plain: T
    _encrypted: bytes

    @classmethod
    def encrypt(cls, key: bytes, encrypted: cord.Record, plain: typing.Any) -> "SecretEnvelope":
        encoded = encrypted.encode()
        encrypted = SecretBox(key).encrypt(encoded)
        return cls(plain=plain, _encrypted=encrypted)

    def decrypt(self, key: bytes) -> T:
        try:
            decrypted = SecretBox(key).decrypt(self._encrypted)
            field: cord.EncryptedField = self.fields["_encrypted"]  # noqa
            return field.record_cls.decode(decrypted)
        except:
            raise CryptographyError("Decryption failed")


class Identifiable(abc.ABC):
    def identify(self):
        raise NotImplementedError
