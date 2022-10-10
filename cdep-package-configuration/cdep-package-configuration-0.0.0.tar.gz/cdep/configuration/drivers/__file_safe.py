from pathlib import Path

from .__file import FileDriver
from ..models import BaseModel


class FileSafeDriver(FileDriver):
    basepath: Path

    def __init__(self, basepath: Path | str) -> None:
        pass

    def load(self, annotations: dict):
        return
