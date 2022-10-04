from ns.auth.interface import IAuthProvider


class DjangoAuthProvider(IAuthProvider):

    def authorize(self, username: str, password: str) -> str:
        pass

    def authenticate(self, auth_token: str) -> int:
        pass
