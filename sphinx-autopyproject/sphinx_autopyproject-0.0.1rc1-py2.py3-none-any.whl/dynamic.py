import ast
import importlib
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, Iterable, Union

NAMESPACE_CACHE: Dict[str, Any] = {}


def get_python(value: str, namespace=None) -> Any:
    if namespace is None:
        namespace = NAMESPACE_CACHE

    def _load(name):
        namespace[name] = importlib.import_module(name)

    while True:
        # pylint: disable=no-member
        try:
            # pylint: disable=eval-used
            return eval(value, namespace)
        except NameError as e:
            _load(e.name)  # type: ignore
        except AttributeError as e:
            if not isinstance(e.obj, ModuleType):  # type: ignore
                raise
            _load(f'{e.obj.__name__}.{e.name}')  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Error evaluating '{value}': {e!r}") from e


def get_token(value: str, encoding: str = "utf-8") -> str:
    file_name, token = value.rsplit(":", 1)

    for line in Path(file_name).read_text(encoding).splitlines(keepends=True):
        if line.startswith(token):
            return ast.literal_eval(line.split("=", 1)[1])
    raise RuntimeError(f"{token} not found in {file_name}")


PACKAGE_METADATA_CACHE: Dict[str, str] = {}


def force_str(value: Union[Iterable[str], str]) -> str:
    return ''.join(list(value))


def get_package_meta(value: str) -> str:
    value = value.lower()

    if value in PACKAGE_METADATA_CACHE:
        return PACKAGE_METADATA_CACHE[value]

    # pylint: disable=import-outside-toplevel
    from .package_metadata import get_metadata_by_build

    PACKAGE_METADATA_CACHE.update(
        {
            key.lower(): force_str(value)
            for key, value in get_metadata_by_build().items()
        }
    )

    PACKAGE_METADATA_CACHE['author'] = PACKAGE_METADATA_CACHE.get(
        'author-email', ''
    ).split(' <', maxsplit=1)[0]

    return PACKAGE_METADATA_CACHE[value]


@dataclass
class DynamicField:
    type: str
    value: str

    def get(self):
        return dict(python=get_python, token=get_token, package=get_package_meta)[
            self.type
        ](self.value)
