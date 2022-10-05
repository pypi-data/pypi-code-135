"""Middleware for InvenTree."""

from django.http import HttpResponse
from django.urls import resolve


class AuthRequiredMiddleware(object):
    """Check for user to be authenticated."""

    def __init__(self, get_response):
        """Save response object."""
        self.get_response = get_response

    def __call__(self, request):
        """Check if user needs to be authenticated and is.

        Redirects to login if not authenticated.
        """
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        assert hasattr(request, "user")

        # Is the function exempt from auth requirements?
        path_func = resolve(request.path).func
        if getattr(path_func, "auth_exempt", False) is True:
            return self.get_response(request)

        if not request.user.is_authenticated:
            # No authorization was found for the request
            # Return a 401 (Unauthorized) response code for this request
            return HttpResponse("Unauthorized", status=401)

        response = self.get_response(request)

        return response
