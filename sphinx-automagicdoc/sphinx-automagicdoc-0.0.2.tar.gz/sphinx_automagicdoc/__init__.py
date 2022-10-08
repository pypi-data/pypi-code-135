"""A plugin to automagically create autodoc-based API documentation files on the fly"""
__version__ = '0.0.2'

from .entrypoint import setup

__all__ = [
    "setup",
]
