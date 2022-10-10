from pathlib import Path
from typing import NamedTuple

import yaml


class StatuteLabel(NamedTuple):
    category: str
    identifier: str

    def get_obj(self, statute_path: Path, yf: str) -> dict | None:
        """Supply a base statute path, e.g. corpus/statutes/<category>/<identifier>/target file name `yf` and extract the yaml file object."""
        custom_file = "".join([self.category.lower(), self.identifier.lower()])
        permitted = ["details", "data", "units", custom_file]
        if yf not in permitted:
            return None
        parts = [self.category.lower(), self.identifier.lower(), f"{yf}.yaml"]
        target = statute_path.joinpath("/".join(parts))
        if target.exists():
            text = target.read_text()
            obj = yaml.safe_load(text)
            return obj
        return None


class IndeterminateStatute(NamedTuple):
    text: str
