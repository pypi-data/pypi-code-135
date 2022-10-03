from __future__ import annotations

import ast
from typing import Any, Generator, Tuple, Type

TAN001 = "TAN001: Use `|` instead of `Union` or `Optional`."
TAN002 = (
    "TAN002: Use built-in generics instead of typing implementations "
    + "(e.g. list instead of `List`)."
)

VisitorError = Tuple[int, int, str]
PluginErrorInfo = Tuple[int, int, str, Type[Any]]


class UnionTypingVisitor(ast.NodeVisitor):
    """AST-based visitor that checks for usage of Union and Optional."""

    _union_names = ("Union", "Optional")

    def __init__(self) -> None:
        """Initializes visitor with an empty errors list."""
        self.errors: list[VisitorError] = []

    def visit_Subscript(self, node: ast.Subscript) -> None:
        """Checks subscript annotations."""
        union_used = (
            isinstance(node.value, ast.Name)
            and node.value.id in self._union_names
        )
        if union_used:
            self.errors += [(node.lineno, node.col_offset, TAN001)]
        self.generic_visit(node)


class GenericTypesVisitor(ast.NodeVisitor):
    """AST-based visitor that checks for usage of non-generic instances."""

    _non_generic_names = (
        "Dict",
        "List",
        "Tuple",
        "Type",
        "Set",
    )

    def __init__(self) -> None:
        """Initializes visitor with an empty errors list."""
        self.errors: list[VisitorError] = []

    def visit_Subscript(self, node: ast.Subscript) -> None:
        """Checks subscript annotations."""
        invalid_keyword_used = (
            isinstance(node.value, ast.Name)
            and node.value.id in self._non_generic_names
        )
        if invalid_keyword_used:
            self.errors += [(node.lineno, node.col_offset, TAN002)]
        self.generic_visit(node)


class TypeAnnotationsPlugin:
    """
    Plugin for flake8 checking for common type annotation mistakes.

    TAN001 - disallows `Union` and `Optional` usages and encourages usage of
             a new `|` operator syntax. The usage of the new syntax can be
             enabled in earlier versions (Python 3.7+) via the
             `from __future__ import annotations` import.

    TAN002 - disallows usage of types where built-in alternative can be used,
             e.g. `List[]` instead of `list[]`, etc. The support for usage of
             generics in typing syntax has been added in Python 3.9, and is now
             the preferred way of annotating types. The usage of the new syntax
             can be enabled in earlier versions (Python 3.7+) via the
             `from __future__ import annotations` import.
    """

    name = __name__
    version = "1.0.0"

    def __init__(self, tree: ast.AST) -> None:
        """Initializes the plugin with the AST tree."""
        self._tree = tree

    def run(self) -> Generator[PluginErrorInfo, None, None]:
        """Runs the plugin checks."""
        for visitor_cls in (UnionTypingVisitor, GenericTypesVisitor):
            visitor = visitor_cls()
            visitor.visit(self._tree)

            for line, col, msg in visitor.errors:
                yield line, col, msg, type(self)
