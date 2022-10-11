# std
from __future__ import annotations
from abc import ABC, abstractmethod
import os
from typing import Dict, Optional as Opt, Union

# internal
from tier.internal.pyproject import PyProject

# types
DependencyDef = Union[str, Dict[str, str]]
DependenciesDef = Dict[str, DependencyDef]


class AbstractBuildSystem(ABC):

    def __init__(self, dirpath: Opt[str] = None):
        self._dirpath = dirpath or os.getcwd()
        self._pyproject = PyProject(self._dirpath)

    @abstractmethod
    def get_package_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_version(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def set_version(self, version: str):
        raise NotImplementedError

    @abstractmethod
    def get_dependencies(self) -> DependenciesDef:
        raise NotImplementedError

    @abstractmethod
    def set_dependency(self, dependency_name: str, dependency: DependencyDef):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def system_name(cls) -> str:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def build_backend(cls) -> str:
        raise NotImplementedError

    @classmethod
    def is_build_system(cls, dirpath: Opt[str] = None) -> bool:
        return PyProject(dirpath).build_backend() == cls.build_backend()
