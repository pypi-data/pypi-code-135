import os

import requests


class URLRequest:
    def __init__(self, url):
        self.url = url

    def get(self, **kwargs):
        return requests.get(self.url, **kwargs)

    def post(self, **kwargs):
        return requests.post(self.url, **kwargs)

    def delete(self, **kwargs):
        return requests.delete(self.url, **kwargs)

    def put(self, **kwargs):
        return requests.put(self.url, **kwargs)

    def patch(self, **kwargs):
        return requests.patch(self.url, **kwargs)

    def __getattr__(self, k):
        return URLRequest(os.path.join(self.url, k))

    def __getitem__(self, k):
        return URLRequest(os.path.join(self.url, k))