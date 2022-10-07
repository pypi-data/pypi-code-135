from io import BufferedReader
from pathlib import Path
from typing import Iterable, Type

from devtools import debug
import ijson
from pydantic import ValidationError

from dar_etl.schemas.base_model import DarBaseModel
from dar_etl.schemas.root_keys import Root


class DarParser:
    def __init__(self, root: Root, parsing_type: Type[DarBaseModel]) -> None:
        self.root_key: str = root.value
        self.parsing_type = parsing_type

    def parse(self, filepath: Path) -> Iterable[DarBaseModel]:
        with open(file=filepath, mode="rb") as file_pointer:
            try:
                yield from self.iterate_json(file_pointer=file_pointer)
            except ijson.IncompleteJSONError:
                debug(self.root_key)

    def iterate_json(self, file_pointer: BufferedReader) -> Iterable[DarBaseModel]:
        for record in ijson.items(file_pointer, f"{self.root_key}.item"):
            try:
                yield self.parsing_type(**record)
            except ValidationError as validation_error:
                debug(record)
                raise validation_error
