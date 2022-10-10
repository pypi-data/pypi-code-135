import ruamel.yaml
import typing

from ._base import ConfigBase


class ConfigYAML(ConfigBase):
    suffix = '.yaml'

    def load(self) -> typing.Any:
        yaml = ruamel.yaml.YAML(typ='safe')
        try:
            data = yaml.load(self._path)
        except (FileNotFoundError, TypeError, KeyError):
            return {}
        return data

    def __repr__(self) -> str:
        return f'ConfigYAML(path="{self._path}")'
