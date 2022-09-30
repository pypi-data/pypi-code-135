#!/usr/bin/env python3
from urllib.parse import urljoin
import requests


class RequestsAPI(object):
    """Wrapper for requests()"""

    def __init__(self, API_URL: str, API_KEY: str):
        """Init Constructor requires API-URL and API-KEY
        Args:
            API_URL (str): API url.
            API_KEY (str): API key.
        """
        self.API_URL = API_URL.strip('/') + '/'
        self.API_KEY = API_KEY
        self.HEADERS = {'Authorization': f'Bot {self.API_KEY}'}
        self.session = requests.Session()

    def get(self, path: str, **kwargs):
        """
        HTTP GET

        Args:
            path: The endpoint for API
        """
        if not kwargs.get("headers"):
            kwargs.update({"headers": self.HEADERS})
        kwargs.update({"url": urljoin(self.API_URL, path.strip('/'))})

        self.r = self.session.get(**kwargs)
        if self.r.headers.get('Content-Type'):
            if 'json' in self.r.headers.get('Content-Type'):
                return self.r.json()
        return self.r.text

    def put(self, path: str, **kwargs):
        """
        HTTP PUT

        Args:
            path: The endpoint for API
        """
        if not kwargs.get("headers"):
            kwargs.update({"headers": self.HEADERS})
        kwargs.update({"url": urljoin(self.API_URL, path.strip('/'))})

        self.r = self.session.put(**kwargs)
        if self.r.headers.get('Content-Type'):
            if 'json' in self.r.headers.get('Content-Type'):
                return self.r.json()
        return self.r.text

    def patch(self, path: str, **kwargs):
        """
        HTTP PUT

        Args:
            path: The endpoint for API
        """
        if not kwargs.get("headers"):
            kwargs.update({"headers": self.HEADERS})
        kwargs.update({"url": urljoin(self.API_URL, path.strip('/'))})

        self.r = self.session.patch(**kwargs)
        if self.r.headers.get('Content-Type'):
            if 'json' in self.r.headers.get('Content-Type'):
                return self.r.json()
        return self.r.text

    def post(self, path: str, **kwargs):
        """
        HTTP POST

        Args:
            path: The endpoint for API
        """
        if not kwargs.get("headers"):
            kwargs.update({"headers": self.HEADERS})
        kwargs.update({"url": urljoin(self.API_URL, path.strip('/'))})

        self.r = self.session.post(**kwargs)
        if self.r.headers.get('Content-Type'):
            if 'json' in self.r.headers.get('Content-Type'):
                return self.r.json()
        return self.r.text

    def delete(self, path: str, **kwargs):
        """
        HTTP DELETE

        Args:
            path: The endpoint for API
        """
        if not kwargs.get("headers"):
            kwargs.update({"headers": self.HEADERS})
        kwargs.update({"url": urljoin(self.API_URL, path.strip('/'))})

        self.r = self.session.delete(**kwargs)
        if self.r.headers.get('Content-Type'):
            if 'json' in self.r.headers.get('Content-Type'):
                return self.r.json()
        return self.r.text
