from __future__ import annotations
from typing import Union, Any


class HasContext:
    _context: Union[None, list] = None

    # Add contextual information.
    # param: label
    # type: str|int
    # param: data
    # type: Any
    # return: HasContext
    def add_context(self, label: Union[str, int], data: Any) -> HasContext:
        self._context[label] = data
        return self

    # Set contextual information.
    # param: context
    # type: list
    # return: HasContext
    def set_context(self, context: list) -> HasContext:
        self._context = context
        return self

    # Get contextual information.
    # param: label
    # type: None|str|int
    # return: Any
    def get_context(self, label: Union[None, str, int] = None) -> Any:
        if label:
            if label in self._context:
                return self._context[label]
            else:
                return None
        return self._context
