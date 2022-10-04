from .base_exc import BaseException

class LoginProviderFailedException(BaseException):
    def __init__(self, email: str):
        self.message = '[{}] login gagal'.format(email)