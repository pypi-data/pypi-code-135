"""Inject Sphinx Configuration from pyproject.toml"""
import os
import sys
from pathlib import Path

import tomli

from .dynamic import DynamicField
from .util import restore_cwd

__version__ = '0.0.2'

PYPROJECT_TOML = "pyproject.toml"
TOOL_KEY = "sphinx-autopyproject"
OUR_KEY = "autopyproject"


def walk_stack_to_importer():
    frame = sys._getframe(0)  # pylint: disable=protected-access

    own_package = Path(__file__).parent

    while True:
        frame = frame.f_back

        name = frame.f_code.co_filename
        if own_package in Path(name).parents:
            continue

        if 'importlib.' not in frame.f_code.co_filename:
            break

    return frame


def load_toml(file_name: Path):
    with file_name.open('rb') as fp:
        return tomli.load(fp)


def search_pyproject(*paths):
    for path in paths:
        path = Path(path) / PYPROJECT_TOML
        if path.is_file():
            return path
    return None


def process_autopyproject(sphinx_config, config):
    # extend path
    sys_path = config.get('sys_path', [])
    for item in reversed(sys_path):
        if not Path(item).is_absolute():
            item = str(Path(item).resolve())
        sys.path.insert(0, item)

    dynamic_updates = {}

    dynamic = config.get('dynamic', {})
    for key, dynamic_getting in dynamic.items():
        dynamic_updates[key] = DynamicField(**dynamic_getting).get()

    sphinx_config.update(dynamic_updates)


def load_from_pyproject(pyproject_path=None, target=None):
    if pyproject_path is None:
        config_file = Path(walk_stack_to_importer().f_code.co_filename)
        pyproject_path = config_file.parent.parent / PYPROJECT_TOML

    pyproject_path = Path(pyproject_path)

    project = load_toml(pyproject_path)

    with restore_cwd():
        os.chdir(pyproject_path.parent)

        tools = project.get("tool", {})

        sphinx_config = tools.get(TOOL_KEY, {})

        config = sphinx_config.pop(OUR_KEY, {})

        process_autopyproject(sphinx_config, config)

        if target:
            target.update(sphinx_config)

        return sphinx_config
