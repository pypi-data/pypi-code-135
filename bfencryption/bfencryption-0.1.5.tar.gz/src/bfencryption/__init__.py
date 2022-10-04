import hashlib
import base64


def encrypt_raw(inp, key):
    if len(inp) != len(key):
        return -1

    encrypted = [str(hashlib.sha256((str(val) + str(key[idx])).encode()).hexdigest()) for idx, val in enumerate(inp)]
    return encrypted


def decrypt_raw(inp, key):
    decrypted = []
    for idx, val in enumerate(inp):
        i = 0
        while str(hashlib.sha256((str(i) + str(key[idx])).encode()).hexdigest()) != inp[idx]:
            i += 1
        decrypted.append(i)
    return decrypted


def encrypt(inp, key):
    inp_raw = [ord(c) for c in inp]
    key_raw = [ord(c) for c in key]
    result = encrypt_raw(inp_raw, key_raw)
    b64result = base64.b64encode(".".join(result).encode()).decode()
    return b64result


def decrypt(inp, key):
    inp = base64.b64decode(inp.encode()).decode().split(".")
    key_raw = [ord(c) for c in key]
    decrypted_raw = decrypt_raw(inp, key_raw)
    output_str = ""
    for i in decrypted_raw:
        output_str += chr(i)
    return output_str


def safe_encrypt(inp, key, level):
    for i in range(level):
        inp = encrypt(inp, key)
        key = encrypt(key, key)
    return inp

def level_key_encrypt(key, level):
    for i in range(level):
        key = encrypt(key, key)
    return key

def safe_decrypt(inp, key, level):
    for i in range(level):
        level -= 1
        level_key = level_key_encrypt(key, level)
        inp = decrypt(inp, level_key)
    return inp