#!/usr/bin/env python
from setuptools import setup
from setuptools import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

srcs = [
    "nist256p1",
    "base58",
    "bignum",
    "bip32",
    "ecdsa",
    "curves",
    "hmac",
    "rand",
    "ripemd160",
    "secp256k1",
    "sha2",
    "sha3",
    "address",
    "rfc6979",
    "hmac_drbg",
    "memzero",
    "hasher",
    "blake256",
    "blake2b",
    "groestl",
    "ed25519-donna/curve25519-donna-32bit",
    "ed25519-donna/curve25519-donna-helpers",
    "ed25519-donna/curve25519-donna-scalarmult-base",
    "ed25519-donna/modm-donna-32bit",
    "ed25519-donna/ed25519",
    "ed25519-donna/ed25519-keccak",
    "ed25519-donna/ed25519-donna-32bit-tables",
    "ed25519-donna/ed25519-donna-basepoint-table",
    "ed25519-donna/ed25519-donna-impl-base",
    "ed25519-donna/ed25519-sha3",
]

extensions = [
    Extension(
        "TrezorCrypto",
        sources=["TrezorCrypto.pyx", "c.pxd"] + [x + ".c" for x in srcs],
        extra_compile_args=[],
    )
]

setup(
    url="https://github.com/trezor/trezor-crypto",
    cmdclass={"build_ext": build_ext},
    ext_modules=cythonize(extensions),
    include_package_data=True,
)
