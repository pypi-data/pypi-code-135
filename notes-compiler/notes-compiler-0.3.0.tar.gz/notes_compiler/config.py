import json
import os.path
from typing import Dict, Self


class Config:
    def __init__(self, config: Dict):
        self.config = config

    @classmethod
    def from_json(cls, json_text: str) -> Self:
        return cls.default().merge_with(cls(json.loads(json_text)))

    @classmethod
    def from_json_file(cls, filename: str) -> Self:
        with open(filename, "r") as file:
            return cls.default().merge_with(cls(json.loads(file.read())))

    @classmethod
    def default(cls) -> Self:
        raise NotImplementedError()

    def merge_with(self, other: Self) -> Self:
        def merge_configs(source, destination):
            for key, value in source.items():
                if isinstance(value, dict):
                    node = destination.setdefault(key, {})
                    merge_configs(value, node)
                elif (
                    isinstance(value, list)
                    and key in destination
                    and isinstance(destination[key], list)
                ):
                    destination[key].extend(value)
                else:
                    destination[key] = value

            return destination

        self.config = merge_configs(other.config, self.config)
        return self

    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        else:
            raise AttributeError(name)


class ProjectConfig(Config):
    @classmethod
    def default(cls) -> Self:
        return cls(
            {
                "css": ["header.css", "pygments.css"],
                "scripts": [
                    "https://polyfill.io/v3/polyfill.min.js?features=es6",
                    "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js",
                ],
                "root": ".",
                "src_root": "src",
                "public_root": "public",
            }
        )

    @classmethod
    def from_json_file(cls, filename: str) -> Self:
        root = os.path.dirname(os.path.abspath(filename))
        return super().from_json_file(filename).merge_with(cls({"root": root}))


class FolderConfig(Config):
    @classmethod
    def default(cls) -> Self:
        return cls({"build_index": False})
