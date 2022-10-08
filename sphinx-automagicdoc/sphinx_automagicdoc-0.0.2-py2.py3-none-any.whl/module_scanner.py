import os
from fnmatch import fnmatch
from functools import partial
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Iterable, List, Optional, Union

from .model import Module

INIT_PY = '__init__.py'
MAIN_PY = '__main__.py'


def _path_to_str(path: Path, base_path: Path) -> str:
    path_str = str(path).replace(str(base_path.parent), '').replace(os.path.sep, '.')
    if path_str.startswith('.'):
        path_str = path_str[1:]
    if path_str.endswith('.py'):
        path_str = path_str[:-3]
    return path_str


def _is_ignored(check_path: Path, ignore: List[str], base_path: Path) -> bool:
    path_str = _path_to_str(check_path, base_path=base_path)
    for ignored_item in ignore:
        if fnmatch(path_str, ignored_item):
            return True
    return False


def _get_submodules(base_path: Path, ignore: List[str]) -> Iterable[Module]:
    is_ignored = partial(_is_ignored, ignore=ignore, base_path=base_path)
    path_to_str = partial(_path_to_str, base_path=base_path)
    sub_modules = [
        p for p in sorted(base_path.rglob(INIT_PY)) if not is_ignored(p.parent)
    ]

    for sub_module in sub_modules:
        sub_module = sub_module.parent
        sub_sub_modules = [
            sub_sub_module
            for sub_sub_module in sub_module.glob('*.py')
            if sub_sub_module.name not in (INIT_PY, MAIN_PY)
            and not is_ignored(sub_sub_module)
        ]

        submodule_str = path_to_str(sub_module)

        yield Module(
            module_str=submodule_str,
            is_package=True,
            has_submodules=bool(len(sub_sub_modules)),
            parent_str='.'.join(submodule_str.split('.')[:-1]),
        )

        for sub_sub_module in sub_sub_modules:
            yield Module(
                module_str=path_to_str(sub_sub_module),
                is_package=False,
                has_submodules=False,
                parent_str=submodule_str,
            )


def get_module_hierarchy(
    name: Union[str, ModuleType], ignore: Optional[List[str]] = None
) -> Iterable[Module]:
    if ignore is None:
        ignore = []

    if isinstance(name, str):
        module = import_module(name)
    else:
        module = name

    assert isinstance(module, ModuleType) and module.__file__ is not None

    path = Path(module.__file__).parent

    yield from _get_submodules(path, ignore)
