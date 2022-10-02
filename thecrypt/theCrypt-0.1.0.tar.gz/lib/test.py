from re import X


import base64, os, cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def main():
    password_provided = 'password'
    print(password_provided)
    password = password_provided.encode()

    salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000)

    key = base64.urlsafe_b64encode(kdf.derive(password))
    print(key)

    phrase = "hello carter"
    fernet = Fernet(key)
    encrypted = fernet.encrypt(phrase.encode())
    print(encrypted)
    decrypted = fernet.decrypt(encrypted).decode()
    print(decrypted)

if __name__ == '__main__':
   main()