import importlib
import pkgutil
import pyclbr
from pathlib import Path
from types import ModuleType
from typing import List, Union

from .importers import import_module


def get_modules(
    package: Union[ModuleType, str],
    search_subpackages: bool = True,
    names_only: bool = False,
) -> Union[List[str], List[ModuleType]]:
    """Find all modules in a package or nested packages.

    Args:
        package (Union[ModuleType, str]): Top-level package where search should begin.
        search_subpackages (bool, optional): Search sub-packages within `package`. Defaults to True.
        names_only (bool, optional): Return module names.

    Returns:
        Union[List[str], List[ModuleType]]: The discovered modules or module names.
    """
    if isinstance(package, str):
        # import the package.
        package = importlib.import_module(package)
    # search for module names.
    searcher = pkgutil.walk_packages if search_subpackages else pkgutil.iter_modules
    module_names = [
        name
        for _, name, ispkg in searcher(package.__path__, f"{package.__name__}.")
        if not ispkg
    ]
    if names_only:
        return module_names
    # import the discovered modules.
    return [import_module(name) for name in module_names]


def module_class_impl(
    base_class: Union[ModuleType, str],
    module: Union[ModuleType, str],
    names_only: bool = False,
) -> Union[List[str], List[ModuleType]]:
    """Find all implementations of a base class within a module.

    Args:
        base_class (Union[ModuleType, str]): The base class who's implementations should be searched for.
        module (Union[ModuleType, str]): The module to search in.
        names_only (bool, optional): Return class names. Defaults to False.

    Returns:
        Union[List[str], List[ModuleType]]: The discovered classes or class names.
    """
    if isinstance(module, str):
        if names_only:
            # check if module_name is a path to a Python file.
            if (module_path := Path(module)).is_file():
                # read python file path
                module_classes = pyclbr.readmodule(
                    module_path.stem, path=module_path.parent
                )
            else:
                # read installed module path.
                module_classes = pyclbr.readmodule(module)
            base_class = (
                base_class if isinstance(base_class, str) else base_class.__name__
            )
            return [
                cls_name
                for cls_name, cls_obj in module_classes.items()
                if any(getattr(s, 'name', s) == base_class for s in cls_obj.super)
            ]
        module = import_module(module)
    # parse the imported module.
    if isinstance(base_class, str):
        class_defs = [
            o
            for o in module.__dict__.values()
            if base_class in [c.__name__ for c in getattr(o, "__bases__", [])]
        ]
    else:
        class_defs = [
            o
            for o in module.__dict__.values()
            if base_class in getattr(o, "__bases__", [])
        ]
    if names_only:
        return [c.__name__ for c in class_defs]
    return class_defs


def pkg_class_impl(
    base_class: Union[ModuleType, str],
    package: Union[ModuleType, str],
    search_subpackages: bool = True,
    names_only: bool = False,
) -> Union[List[str], List[ModuleType]]:
    """Find all implementations of a base class within a package.

    Args:
        base_class (Union[ModuleType, str]): The base class who's implementations should be searched for.
        package (Union[ModuleType, str]): The package to search in.
        search_subpackages (bool, optional): Search sub-packages within `package`. Defaults to True.
        names_only (bool, optional): Return class names. Defaults to False.

    Returns:
        Union[List[str], List[ModuleType]]: The discovered classes or class names.
    """
    class_impl = []
    for module in get_modules(package, search_subpackages, names_only):
        class_impl += module_class_impl(base_class, module, names_only)
    return class_impl



def module_class_inst(
    module: Union[ModuleType, str, Path], class_type: ModuleType
) -> List[ModuleType]:
    """Find all instances of a class within a module.

    Args:
        module (Union[ModuleType, str, Path]): The module to search in.
        class_type (ModuleType): The class who's instances should be searched for.

    Returns:
        List[ModuleType]: The discovered class instances.
    """
    if isinstance(module, (Path,str)):
        module = import_module(module)
    return [o for o in module.__dict__.values() if isinstance(o, class_type)]


def pkg_class_inst(
    class_type: ModuleType,
    package: Union[ModuleType, str],
    search_subpackages: bool = True,
) -> List[ModuleType]:
    """Find all instances of a class within a package.

    Args:
        class_type (ModuleType): The class who's instances should be searched for.
        package (Union[ModuleType, str]): The package to search in.
        search_subpackages (bool, optional): Search sub-packages within `package`. Defaults to True.

    Returns:
        List[ModuleType]: The discovered class instances.
    """
    return [
        o
        for module in get_modules(package, search_subpackages)
        for o in module.__dict__.values()
        if isinstance(o, class_type)
    ]
    
    
