from pathlib import Path

from pydantic.error_wrappers import ValidationError
from ..models import BaseModel


class BaseDriver:
    def _source_not_found(self, sourcelocation: str):
        return

    def _validate(self, raw_config: dict, cls: BaseModel, sourcelocation: str):
        return

    def load(self, annotations: dict) -> dict:
        pass

    def save(self, annotations: dict, globals: dict) -> None:
        pass
