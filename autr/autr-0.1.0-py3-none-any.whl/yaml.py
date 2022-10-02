import typing

import os

import yaml

from .base import Reader, read


class CustomLoader(yaml.SafeLoader):
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(CustomLoader, self).__init__(stream)


class YamlReader(Reader, extensions=(".yaml", ".yml")):
    def _read(
        self, filename: str, loader: yaml.SafeLoader = CustomLoader, *args, **kwargs
    ) -> typing.Any:
        with open(filename, "r") as f:
            return yaml.load(f, loader) if loader else yaml.load(f)

    def _write(self, filename: str, *args, **kwargs):
        with open(filename, "w") as file:
            yaml.dump(self.data, file, *args, **kwargs)


def include_constructor(loader, node):
    params = {}
    try:
        filename = os.path.join(loader._root, loader.construct_scalar(node))
    except yaml.constructor.ConstructorError:
        params = loader.construct_mapping(node, deep=True)
        filename = os.path.join(loader._root, params.pop("filename"))

    args = params.pop("args", [])
    kwargs = params.pop("kwargs", {})

    return read(filename, *args, **kwargs, **params)


CustomLoader.add_constructor("!include", include_constructor)
