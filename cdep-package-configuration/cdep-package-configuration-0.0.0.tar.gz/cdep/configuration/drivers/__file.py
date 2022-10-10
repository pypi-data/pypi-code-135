import json
from pathlib import Path

from .__base import BaseDriver
from ..models import BaseModel


class FileDriver(BaseDriver):
    def __init__(self, basepath: Path | str) -> None:
        pass

    def load(self, annotations: dict):
        return

    def save(self, annotations: dict, globals: dict):
        pass
