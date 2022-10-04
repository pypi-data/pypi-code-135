import hashlib
import base64
import random


def encrypt_raw(inp, key):
    if len(inp) != len(key):
        return -1

    encrypted = ".".join(
        [str(hashlib.md5((str(val) + str(key[idx])).encode()).hexdigest()) for idx, val in enumerate(inp)])
    return encrypted


def decrypt_raw(inp, key):
    splitted = inp.split(".")
    max_digits = splitted[0]
    decrypted = []
    for idx, val in enumerate(splitted):
        i = 0
        while str(hashlib.md5((str(i) + str(key[idx])).encode()).hexdigest()) != splitted[idx]:
            i += 1
        decrypted.append(i)
    return decrypted


def encrypt(inp, key):
    inp_raw = [ord(c) for c in inp]
    key_raw = [ord(c) for c in key]
    return base64.b64encode(encrypt_raw(inp_raw, key_raw).encode()).decode()


def decrypt(inp, key):
    inp = base64.b64decode(inp.encode()).decode()
    key_raw = [ord(c) for c in key]
    decrypted_raw = decrypt_raw(inp, key_raw)
    output_str = ""
    for i in decrypted_raw:
        output_str += chr(i)
    return output_str


def generate_key(inp):
    key = ""
    for i in inp:
        key += chr(random.choice(range(32, 176)))
    return key
