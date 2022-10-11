# std
from __future__ import annotations
from typing import Dict

# internal
from tier.internal.build_systems.abstract_build_system import (
    AbstractBuildSystem,
    DependenciesDef, DependencyDef,
)


class Poetry(AbstractBuildSystem):

    def tool(self) -> dict:
        return self._pyproject.read().get('tool', {}).get('poetry', {})

    def get_package_name(self) -> str:
        return self.tool().get('name', '')

    def get_version(self) -> str:
        return self.tool().get('version', '')

    def set_version(self, version: str):
        obj = self._pyproject.read()
        if 'tool' not in obj:
            obj['tool'] = {}
        if 'poetry' not in obj['tool']:
            obj['tool']['poetry'] = {}
        obj['tool']['poetry']['version'] = version
        self._pyproject.write(obj)

    def get_dependencies(self) -> DependenciesDef:
        return self.tool()['dependencies']

    def set_dependency(self, dependency_name: str, dependency: DependencyDef):
        obj = self._pyproject.read()
        if 'tool' not in obj:
            obj['tool'] = {}
        if 'poetry' not in obj['tool']:
            obj['tool']['poetry'] = {}
        if 'dependencies' not in obj['tool']['poetry']:
            obj['tool']['poetry']['dependencies'] = {}
        obj['tool']['poetry']['dependencies'][dependency_name] = dependency
        self._pyproject.write(obj)

    @classmethod
    def system_name(cls) -> str:
        return 'poetry'

    @classmethod
    def build_backend(cls) -> str:
        return 'poetry.core.masonry.api'
