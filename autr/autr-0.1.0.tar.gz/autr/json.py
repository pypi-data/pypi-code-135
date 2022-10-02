import json

from .base import Reader


class JSONReader(Reader, extensions=(".json",)):
    def _read(self, filename: str, *args, **kwargs) -> str:
        with open(filename, "r") as f:
            content = f.read()
            return json.loads(content, *args, **kwargs)

    def _write(self, filename: str, *args, **kwargs):
        with open(filename, "w", *args, **kwargs) as f:
            json_object = json.dumps(self.data, *args, **kwargs)
            f.write(json_object)
