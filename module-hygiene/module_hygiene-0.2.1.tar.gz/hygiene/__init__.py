"""
Namespace hygiene in Python!

This package add's something like an 'export' workflow to Python package development. Define
a collection of strings which represents the names you wish to export (not delete at the end
of the module declaration) and call the 'cleanup' function with no arguments, and all 
non-exported names will be deleted at the end of your module!

But wait, why wouldn't you use the '__all__' variable?

The '__export__' variable is a bit different. The '__all__' variable defines what names are 
exported when users type 'from module import *'. The same could be said about the 
'__export__' variable, with critical amendment: all names which are not exported are 
deleted!
"""

__export__ = {"cleanup",}

from typing import Optional, Iterable
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("module-hygiene")
except PackageNotFoundError:
    __version__ = "unknown"

def cleanup(export: Optional[Iterable] = None):
    """
    Delete every non-exported name in the caller's namespace!
    """
    import inspect

    current = inspect.currentframe()
    if current:
        parent = current.f_back
        if parent:
            locals = parent.f_locals

            __export__ = export if export else locals["__export__"]

            for _ in (*locals,):
                if locals[_] != __export__ and not _.startswith("__") and _ not in __export__:
                    del locals[_]
    
if __name__ == "__main__":
    ...
else:
    cleanup()
