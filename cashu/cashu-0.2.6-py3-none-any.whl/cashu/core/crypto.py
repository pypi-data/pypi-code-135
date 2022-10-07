import hashlib
from typing import Dict


def derive_keyset_id(keys: Dict[str, str]):
    """Deterministic derivation keyset_id from set of public keys."""
    return hashlib.sha256((str(keys)).encode("utf-8")).hexdigest().encode("utf-8")[:16]
