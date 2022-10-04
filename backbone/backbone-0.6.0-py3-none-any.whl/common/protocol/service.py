from nacl.public import Box, PrivateKey, PublicKey

from backbone.common import cord
from backbone.common.exceptions import CryptographyError


class ServiceError(cord.Record):
    code = cord.StringField()
    message = cord.StringField()


class ServiceRequest(cord.Record):
    id = cord.BytesField()
    action = cord.StringField()
    version = cord.StringField()
    datetime = cord.DateTimeField()
    data = cord.OptionalField(cord.BytesField())


class ServiceResponseContent(cord.Variant):
    data = cord.OptionalField(cord.BytesField())
    error = cord.RecordField(ServiceError)


class ServiceResponse(cord.Record):
    id = cord.BytesField()
    content = cord.VariantField(ServiceResponseContent)


class ServiceRequestEnvelope(cord.Record):
    _encrypted: bytes = cord.EncryptedField(ServiceRequest)
    provider: PublicKey = cord.PublicKeyField()

    @classmethod
    def encrypt(cls, provider: PrivateKey, recipient: PublicKey, encrypted: ServiceRequest) -> "ServiceRequestEnvelope":
        encoded = encrypted.encode()
        encrypted = Box(provider, recipient).encrypt(encoded)
        return cls(provider=provider.public_key, _encrypted=encrypted)

    def decrypt(self, recipient: PrivateKey, provider: PublicKey) -> ServiceRequest:
        try:
            decrypted = Box(recipient, provider).decrypt(self._encrypted)
        except:
            raise CryptographyError("Decryption failed")

        return ServiceRequest.decode(decrypted)


class ServiceResponseEnvelope(cord.Record):
    _encrypted: bytes = cord.EncryptedField(ServiceResponse)
    recipient: PublicKey = cord.PublicKeyField()

    @classmethod
    def encrypt(
        cls, provider: PrivateKey, recipient: PublicKey, encrypted: ServiceResponse
    ) -> "ServiceResponseEnvelope":
        encoded = encrypted.encode()
        encrypted = Box(provider, recipient).encrypt(encoded)
        return cls(recipient=recipient, _encrypted=encrypted)

    def decrypt(self, recipient: PrivateKey, provider: PublicKey) -> ServiceResponse:
        try:
            decrypted = Box(recipient, provider).decrypt(self._encrypted)
        except:
            raise CryptographyError("Decryption failed")

        return ServiceResponse.decode(decrypted)
