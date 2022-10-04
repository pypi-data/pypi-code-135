from abc import ABC


class IImageStorage(ABC):
    def upload_image(self, data: bytes) -> str: ...
