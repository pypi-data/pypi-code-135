import requests
import json

class RequestHandler:
    def __init__(self, url: str = None, headers: dict = None, host: dict = None) -> None:
        self.url = url
        self.headers = headers
        self.host = host

    def __call__(self, msg: str = None, type: str = None, timestamp: str = None) -> None:
        data = {
            "type": type,
            "message": msg,
            "host": self.host,
            "timestamp": timestamp
        }
        self.request(data=data)

    def request(self, data: dict = None) -> dict:
        __r = requests.post(url=self.url, json=data, headers=self.headers)
        if __r.status_code == 200:
            return __r.json()