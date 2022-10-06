
from Crypto.Cipher import AES as _AES
from Crypto.Random import get_random_bytes
import getpass

class AES:
    
    def __init__(self):
        self.key_size = 16
        self.nonce_size = 16
        
    def generate_random_key_tuple(self):
        self.key = get_random_bytes(self.key_size)
        cipher = _AES.new(self.key, _AES.MODE_EAX)
        self.nonce = cipher.nonce
        return self.key, self.nonce
        
    def write_key_tuple(self, file, key, nonce):
        with open(file, "wb") as f:
            for x in (key, nonce):
                f.write(x)
    
    def read_key_tuple(self, file):
        with open(file, "rb") as f:
            self.key, self.nonce = [f.read(x) for x in (self.key_size, self.nonce_size)]
        return self.key, self.nonce
    
    def encrypt(self, message, key=None, nonce=None):
        if key is None and nonce is None:
            key = self.key
            nonce = self.nonce
        if type(message) is str: # it should be byte
            message = message.encode('utf-16')
        cipher = _AES.new(key, _AES.MODE_EAX, nonce)
        self.ciphertext, self.tag = cipher.encrypt_and_digest(message)
        return self.ciphertext, self.tag

    def decrypt(self, ciphertext, tag, key, nonce, to_text=False):
        cipher = _AES.new(key, _AES.MODE_EAX, nonce)
        res = cipher.decrypt_and_verify(ciphertext, tag)
        return res.decode('utf-16') if to_text else res
    
    def write_ciphertext(self, file, ciphertext, tag, nonce):
        with open(file, 'wb') as f:
            for x in (nonce, tag, ciphertext):
                f.write(x)
        print(f"message saved in {file}.")
    
    def read_ciphertext(self, file):
        return self.read_encrypted(file)
            
    def write_encrypted(self, file, message, key=None, nonce=None):
        if key is None and nonce is None:
            key = self.key
            nonce = self.nonce
        self.ciphertext, self.tag = self.encrypt(message)
        self.write_ciphertext(file, self.ciphertext, self.tag, nonce)
    
    def read_encrypted(self, file):
        with open(file, "rb") as f:
            nonce, tag, ciphertext = [f.read(x) for x in (self.nonce_size, 16, -1)]
        return ciphertext, tag, nonce
    
    def read_and_decrypt(self, file, key=None, nonce=None):
        if key is None and nonce is None:
            key = self.key
            nonce = self.nonce
        ciphertext, tag, nonce = self.read_encrypted(file)
        return self.decrypt(ciphertext, tag, key, nonce)
    
    def read_and_decrypt_files(self, file, key_file):
        key = self.read_key(key_file)
        return self.read_and_decrypt(file, key)
    
    def generate_key_user_pass(self, key_file, user_file, pass_file):
        key, nonce = self.generate_random_key_tuple()
        self.write_key_tuple(key_file, key, nonce)
        username = getpass.getpass("Username: ").encode('utf-16')
        password = getpass.getpass("Password: ").encode('utf-16')
        self.write_encrypted(user_file, username, key=key, nonce=nonce)
        self.write_encrypted(pass_file, password, key=key, nonce=nonce)
    
    def read_key_user_pass(self, key_file, user_file, pass_file):
        ca = AES()
        ca._key, ca._nonce = self.read_key_tuple(key_file)
        ca._user_ciphertext, ca._user_tag, ca._user_nonce  = ca.read_encrypted(user_file)
        ca._pass_ciphertext, ca._pass_tag, ca._pass_nonce = ca.read_encrypted(pass_file)
        return ca
    
    @property
    def username(self):
        return self.decrypt(self._user_ciphertext, self._user_tag, self._key, self._user_nonce).decode('utf-16')
    
    @property
    def password(self):
        return self.decrypt(self._pass_ciphertext, self._pass_tag, self._key, self._pass_nonce).decode('utf-16')
        

