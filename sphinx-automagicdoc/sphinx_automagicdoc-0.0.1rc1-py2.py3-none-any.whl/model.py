from typing import NamedTuple


class Module(NamedTuple):
    module_str: str
    is_package: bool
    has_submodules: bool
    parent_str: str
