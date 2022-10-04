from django.contrib.auth.middleware import AuthenticationMiddleware as DjangoAuthenticationMiddleware
from django.http import HttpRequest

from ns.auth.contextvars import authorized_user


class AuthenticationMiddleware(DjangoAuthenticationMiddleware):
    def process_request(self, request: HttpRequest):
        super().process_request(request)
        authorized_user.set(request.user)
