from src.inspector.models import Arrayable
from typing import Union
from src.inspector.models.partials import URL


class HTTP(Arrayable):
    request: Union[str, None] = None
    url: URL = None

    def set_request(self, request: str) -> None:
        self.request = request

    def set_url(self, url: URL) -> None:
        self.url = url

    def get_request(self) -> str:
        return self.request

    def get_url(self) -> URL:
        return self.url
