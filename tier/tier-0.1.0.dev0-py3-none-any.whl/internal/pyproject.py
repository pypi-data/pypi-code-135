# std
from __future__ import annotations
import os
from typing import List, Optional as Opt

# external
import toml

# internal
from tier.internal.build_systems import build_system
from tier.internal.git.commit import Commit
from tier.internal.logging import log


class PyProject:

    FILENAME = 'pyproject.toml'

    def __init__(self, dirpath: Opt[str] = None):
        self.dirpath = dirpath or os.getcwd()

    def __repr__(self) -> str:
        return self.filepath

    @property
    def filepath(self) -> str:
        return os.path.join(self.dirpath, self.FILENAME)

    def exists(self) -> bool:
        return os.path.isfile(self.filepath)

    def read(self) -> dict:
        with open(self.filepath, 'r') as fh:
            return toml.load(fh)

    def write(self, obj: dict):
        with open(self.filepath, 'w') as fh:
            toml.dump(obj, fh)

    def build_system(self) -> 'AbstractBuildSystem':
        build_backend = self.read().get('build-system', {}).get('build-backend', '')
        return build_system.get(build_backend, self.dirpath)

    @classmethod
    def find_recursively(cls, dirpath: Opt[str] = None) -> List[PyProject]:
        dirpath = dirpath or os.getcwd()
        result = []
        for dirpath, dirnames, filenames in os.walk(dirpath):
            if cls.FILENAME in filenames:
                result.append(PyProject(dirpath))
        return result
