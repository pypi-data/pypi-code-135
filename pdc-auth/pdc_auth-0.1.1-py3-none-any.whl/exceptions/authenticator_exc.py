from .base_exc import BaseException

class ConfigLoadException(BaseException):
    def __init__(self, fname: str):
        self.message = 'gagal memuat {}'.format(fname)

class ConfigLoadValidationException(Exception):
    def __init__(self, fname: str):
        self.message = 'konfigurasi {} tidak lengkap'.format(fname)