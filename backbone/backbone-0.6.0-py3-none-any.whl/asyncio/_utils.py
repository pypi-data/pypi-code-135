import base64
import secrets
import typing
import zlib


def zip_longest_reverse(first: typing.List, second: typing.List, default=None):
    length = max(len(first), len(second))
    # Prefix pad both sequences
    first = [default] * (length - len(first)) + first
    second = [default] * (length - len(second)) + second
    return zip(first, second)


def encode_token(obj: bytes, prefix: str = "backbone_") -> str:
    checksum = zlib.crc32(obj).to_bytes(4, "big")
    return prefix + base64.urlsafe_b64encode(obj + checksum).decode()


def decode_token(obj: str, prefix: str = "backbone_") -> bytes:
    if not obj.startswith(prefix):
        raise ValueError("Expected prefix not found")

    obj = obj[len(prefix) :]
    obj = base64.urlsafe_b64decode(obj)

    if len(obj) < 4:
        raise ValueError("Decoded token length must be at least the size of the checksum")

    obj, observed_checksum = obj[:-4], obj[-4:]
    expected_checksum = zlib.crc32(obj).to_bytes(4, "big")

    if not secrets.compare_digest(observed_checksum, expected_checksum):
        raise ValueError("Token checksum does not match what was expected")

    return obj
