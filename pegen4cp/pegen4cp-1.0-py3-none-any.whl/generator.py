"""
based pegen/generator.py
"""


import ast
import re
import token
import inspect
import linecache
from typing import IO, Any, Dict, Optional, Sequence, Set, Text, Tuple

from pegen import grammar
from pegen.grammar import (
    Alt,
    Cut,
    Forced,
    Gather,
    GrammarVisitor,
    Group,
    Lookahead,
    NamedItem,
    NameLeaf,
    NegativeLookahead,
    Opt,
    PositiveLookahead,
    Repeat0,
    Repeat1,
    Rhs,
    Rule,
    StringLeaf,
)
from pegen.python_generator import InvalidNodeVisitor, PythonCallMakerVisitor, PythonParserGenerator

# todo: I don't think it is appropriate to use import to get the code as a string,
#  so think of another way

import pegen4cp.module_prefix as module_prefix
import pegen4cp.module_suffix as module_suffix


def get_source(m):
    return "".join(linecache.getlines(inspect.getfile(m)))


MODULE_PREFIX = get_source(module_prefix)
MODULE_SUFFIX = get_source(module_suffix)


class ForCPPythonParserGenerator(PythonParserGenerator):
    def __init__(
            self,
            gram_code: str,
            grammar: grammar.Grammar,
            file: Optional[IO[Text]],
            tokens: Set[str] = set(token.tok_name.values()),
            location_formatting: Optional[str] = None,
            unreachable_formatting: Optional[str] = None,
    ):
        self.gram_code = gram_code.rstrip("\n")
        super().__init__(grammar, file, tokens, location_formatting, unreachable_formatting)

    def generate(self, filename: str) -> None:
        header = self.grammar.metas.get("header", MODULE_PREFIX)
        if header is not None:
            self.print(header.rstrip("\n").format(filename=filename, gram=self.gram_code))
        subheader = self.grammar.metas.get("subheader", "")
        if subheader:
            self.print(subheader)
        cls_name = self.grammar.metas.get("class", "GeneratedParser")
        self.print("# Keywords and soft keywords are listed at the end of the parser definition.")
        self.print(f"class {cls_name}(Parser):")
        while self.todo:
            for rulename, rule in list(self.todo.items()):
                del self.todo[rulename]
                self.print()
                with self.indent():
                    self.visit(rule)

        self.print()
        with self.indent():
            self.print(f"KEYWORDS = {tuple(self.callmakervisitor.keywords)}")
            self.print(f"SOFT_KEYWORDS = {tuple(self.callmakervisitor.soft_keywords)}")

        trailer = self.grammar.metas.get("trailer", MODULE_SUFFIX.format(class_name=cls_name))
        if trailer is not None:
            self.print(trailer.rstrip("\n"))

    def visit_NamedItem(self, node: NamedItem) -> None:
        name, call = self.callmakervisitor.visit(node.item)
        if node.name:
            name = node.name
        if not name:
            self.print(call)
        else:
            if name != "cut":
                name = self.dedupe(name)
            # To work with Python 3.7 (the current version of PyPy in AtCoder), we will use a method that does not use :=.
            # This method is not equivalent to :=, but it seems sufficient, at least here.
            self.print(f"((globals().__setitem__(\"{name}\", {call}), globals()[\"{name}\"] is not None)[1])")
