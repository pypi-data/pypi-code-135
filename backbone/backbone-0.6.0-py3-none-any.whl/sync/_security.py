import abc
import functools
import gc
import os
import typing

from nacl import encoding, hash
from nacl.public import PrivateKey, PublicKey
from nacl.pwhash import argon2id
from nacl.signing import SigningKey, VerifyKey

from backbone.common import cord, models, protocol

from ._utils import zip_longest_reverse

SERVICE_PUBLIC_KEY = PublicKey(
    public_key=b"bckbnHWxnTY3inEPGpDrYKPeOK4V1OcNDERRxnJZH10="
    if not os.getenv("BACKBONE_DEV")
    else b"etHbHeOUNpTao_ACalJEpsBQc19QTlr68GzSzNPKWn4=",
    encoder=encoding.URLSafeBase64Encoder,
)

T = typing.TypeVar("T", bound=cord.Record)
M = typing.TypeVar("M", bound=cord.Record)


class Enclave(abc.ABC):
    def __init__(self, key: bytes):
        self._mask: bytes = os.urandom(len(key))
        self._masked_key: bytes = bytes(a ^ b for a, b in zip(key, self._mask))

    @property
    def _unmasked_key(self):
        return bytes(a ^ b for a, b in zip(self._masked_key, self._mask))


class SecretKeyEnclave(Enclave):
    def encrypt_envelope(
        self, record_cls: typing.Type[models.SecretEnvelope], encrypted: T, plain: M
    ) -> models.SecretEnvelope:
        return record_cls.encrypt(key=self._unmasked_key, encrypted=encrypted, plain=plain)

    def decrypt_envelope(self, value: models.SecretEnvelope) -> T:
        return value.decrypt(self._unmasked_key)


class PrivateKeyEnclave(Enclave):
    def __init__(self, key: PrivateKey):
        super().__init__(bytes(key))
        self._public_key = self._unmasked_key.public_key

    @property
    def _unmasked_key(self):
        return PrivateKey(super()._unmasked_key)

    def encrypt_request(self, encrypted: protocol.ServiceRequest) -> protocol.ServiceRequestEnvelope:
        return protocol.ServiceRequestEnvelope.encrypt(
            provider=self._unmasked_key, recipient=SERVICE_PUBLIC_KEY, encrypted=encrypted
        )

    def decrypt_response(self, value: protocol.ServiceResponseEnvelope) -> protocol.ServiceResponse:
        return value.decrypt(recipient=self._unmasked_key, provider=SERVICE_PUBLIC_KEY)

    def encrypt_envelope(
        self,
        record_cls: typing.Type[models.SharedEnvelope],
        recipient: PublicKey,
        encrypted: T,
        plain: M,
    ) -> models.SharedEnvelope:
        return record_cls.encrypt(provider=self._unmasked_key, recipient=recipient, encrypted=encrypted, plain=plain)

    def decrypt_envelope(self, value: models.SharedEnvelope, expected_provider: PublicKey) -> T:
        return value.decrypt(recipient=self._unmasked_key, expected_provider=expected_provider)


class SigningKeyEnclave(Enclave):
    def __init__(self, key: SigningKey):
        super().__init__(bytes(key))
        self._verify_key = self._unmasked_key.verify_key

    @property
    def _unmasked_key(self):
        return SigningKey(super()._unmasked_key)

    def sign_envelope(self, record_cls: typing.Type[models.SignedEnvelope], content: T):
        return record_cls.sign(notary=self._unmasked_key, content=content)

    def verify_envelope(self, value: models.SignedEnvelope) -> T:
        return value.verify(expected_notary=self._verify_key)


class Trust:
    def __init__(self, user_name: str, secret_key: bytes, private_key: PrivateKey, signing_key: SigningKey):
        self._secret_key_enclave = SecretKeyEnclave(secret_key)
        self._private_key_enclave = PrivateKeyEnclave(private_key)
        self._signing_key_enclave = SigningKeyEnclave(signing_key)

        self._user: models.User = models.User(
            name=user_name, public_key=private_key.public_key, verify_key=signing_key.verify_key, trusted_workspaces=[]
        )

        self._is_bootstrapped = False

        gc.collect()

    @property
    def secret_key_enclave(self) -> SecretKeyEnclave:
        return self._secret_key_enclave

    @property
    def private_key_enclave(self) -> PrivateKeyEnclave:
        return self._private_key_enclave

    @property
    def signing_key_enclave(self) -> SigningKeyEnclave:
        return self._signing_key_enclave

    @property
    def is_bootstrapped(self) -> bool:
        return self._is_bootstrapped

    @property
    def user(self) -> models.User:
        return self._user

    @classmethod
    def derive_secrets(cls, user_name: str, master_secret: typing.Union[str, bytes]) -> (bytes, PrivateKey, SigningKey):
        encoded_user_name = user_name.encode()

        if isinstance(master_secret, str):
            master_secret = master_secret.encode()

        salt = hash.sha256(b"backbone:user:" + encoded_user_name, encoder=encoding.RawEncoder)
        salt = hash.sha256(salt, encoder=encoding.RawEncoder)

        expanded_secret = argon2id.kdf(
            size=256,
            password=master_secret,
            salt=salt[:16],
            memlimit=argon2id.MEMLIMIT_INTERACTIVE,
            opslimit=argon2id.OPSLIMIT_INTERACTIVE,
        )

        secret_key = expanded_secret[0:32]
        private_key = PrivateKey(expanded_secret[32:64])
        signing_key = SigningKey(expanded_secret[64:96])

        return secret_key, private_key, signing_key

    @classmethod
    def from_master_secret(cls, user_name: str, master_secret: typing.Union[str, bytes]) -> "Trust":
        secret_key, private_key, signing_key = cls.derive_secrets(user_name, master_secret)
        return cls(user_name=user_name, secret_key=secret_key, private_key=private_key, signing_key=signing_key)

    def bootstrap(self, signed_user: models.SignedUser) -> None:
        self._user: models.User = self.signing_key_enclave.verify_envelope(signed_user)
        self._is_bootstrapped = True

    @functools.lru_cache(1)
    def authenticate_workspace(self, signed_workspace: models.SignedWorkspace) -> models.Workspace:
        assert self.is_bootstrapped

        workspace: models.Workspace = signed_workspace.verify(signed_workspace._content.verify_key)
        assert workspace.identify() in self.user.trusted_workspaces

        return workspace

    def authenticate_workspace_grant(
        self, verified_workspace: models.Workspace, signed_public_grant: models.SignedSharedWorkspaceGrant
    ) -> models.SharedWorkspaceGrant:
        assert self.is_bootstrapped

        public_grant: models.SharedWorkspaceGrant = signed_public_grant.verify(verified_workspace.verify_key)
        assert public_grant.provider == verified_workspace.public_key

        return public_grant

    def decrypt_namespace_chain(
        self, chain: models.NamespaceChain
    ) -> (models.Namespace, models.NamespaceGrant, models.NamespaceGrantCredentials):
        assert self.is_bootstrapped

        # Always verify the root of trust
        verified_workspace: models.Workspace = self.authenticate_workspace(chain.workspace)

        expected_notary: typing.Optional[VerifyKey] = verified_workspace.keyspace_verify_key
        expected_provider: typing.Optional[PublicKey] = verified_workspace.keyspace_public_key
        current_key: typing.Optional[PrivateKey] = self.private_key_enclave._unmasked_key

        if chain.workspace_grant:
            public_workspace_grant: models.SharedWorkspaceGrant = chain.workspace_grant.verify(
                verified_workspace.verify_key
            )
            workspace_credentials: models.WorkspaceGrantCredentials = self.private_key_enclave.decrypt_envelope(
                public_workspace_grant, verified_workspace.public_key
            )
            current_key = workspace_credentials.keyspace_private_key

        verified_namespace = None
        namespace_grant_plain = None
        namespace_grant_credentials = None
        for signed_namespace, signed_namespace_grant in zip_longest_reverse(chain.namespaces, chain.namespace_grants):
            verified_namespace = signed_namespace.verify(expected_notary)

            if isinstance(signed_namespace_grant, models.SignedSharedNamespaceGrant):
                public_namespace_grant: models.SharedNamespaceGrant = signed_namespace_grant.verify(expected_notary)
                namespace_grant_plain = public_namespace_grant.plain
                namespace_grant_credentials = public_namespace_grant.decrypt(current_key, expected_provider)
                current_key = namespace_grant_credentials.private_key

            expected_notary = verified_namespace.verify_key
            expected_provider = verified_namespace.public_key

        return verified_namespace, namespace_grant_plain, namespace_grant_credentials

    def decrypt_entry_chain(
        self, chain: models.EntryChain
    ) -> (models.Entry, models.SharedEntryContent, models.EntryGrant, models.EntryGrantCredentials):
        _, _, parent_namespace_credentials = self.decrypt_namespace_chain(chain.namespace_chain)

        parent_namespace: models.Namespace = chain.namespace_chain.namespaces[-1]._content

        entry_metadata: models.Entry = self.authenticate_entry(parent_namespace, chain.entry.metadata)
        entry_content: models.SharedEntryContent = self.authenticate_entry_content(entry_metadata, chain.entry.content)

        public_entry_grant: models.SharedEntryGrant = chain.entry_grant.verify(parent_namespace.verify_key)

        if parent_namespace_credentials:
            entry_grant_credentials: models.EntryGrantCredentials = public_entry_grant.decrypt(
                parent_namespace_credentials.private_key, parent_namespace.public_key
            )
        else:
            entry_grant_credentials: models.EntryGrantCredentials = self._private_key_enclave.decrypt_envelope(
                public_entry_grant, parent_namespace.public_key
            )

        return entry_metadata, entry_content, public_entry_grant.plain, entry_grant_credentials

    @staticmethod
    def authenticate_namespace(parent: models.Namespace, namespace: models.SignedNamespace) -> models.Namespace:
        return namespace.verify(parent.verify_key)

    @staticmethod
    def authenticate_entry(parent: models.Namespace, entry: models.SignedEntry) -> models.Entry:
        return entry.verify(parent.verify_key)

    @staticmethod
    def authenticate_entry_content(
        entry_metadata: models.Entry, entry_content: models.SignedSharedEntryContent
    ) -> models.SharedEntryContent:
        return entry_content.verify(entry_metadata.verify_key)

    @staticmethod
    def authenticate_namespace_grants(
        parent: models.Namespace, namespace_grants: typing.List[models.SignedSharedNamespaceGrant]
    ) -> typing.Iterator[models.SharedNamespaceGrant]:
        for namespace_grant in namespace_grants:
            verified_grant: models.SharedNamespaceGrant = namespace_grant.verify(expected_notary=parent.verify_key)
            if verified_grant.provider != parent.public_key:
                raise ValueError("Invalid namespace grant provider")

            yield verified_grant

    @staticmethod
    def authenticate_entry_grants(
        parent: models.Namespace, entry_grants: typing.List[models.SignedSharedEntryGrant]
    ) -> typing.Iterator[models.SharedEntryGrant]:
        for entry_grant in entry_grants:
            verified_grant: models.SharedEntryGrant = entry_grant.verify(expected_notary=parent.verify_key)
            if verified_grant.provider != parent.public_key:
                raise ValueError("Invalid entry grant provider")

            yield verified_grant
