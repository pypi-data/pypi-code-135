# -*- coding: utf-8 -*-
# Copyright (c) 2022, KarjaKAK
# All rights reserved.

from ast import literal_eval as lite
import tkinter as tk
from tkinter import messagebox
from string import digits
from dataclasses import dataclass
from types import MappingProxyType as mpt


__all__ = ["EvalExp"]


@dataclass(frozen=True, slots=True)
class EvalExp:
    """Class eval that controled what can be express"""

    expression: str
    _all: dict | None

    def __post_init__(self):

        super(EvalExp, self).__setattr__("expression", self.expression)
        if self._all: 
            super(EvalExp, self).__setattr__("_all", mpt(self._all))

    def evlex(self):
        """Expression that controled by what allowed"""

        comp = compile(self.expression, "<string>", "eval",)
        try:
            for name in comp.co_names:
                if name not in self._all:
                    raise NameError(f"{name!r} is not allowed for expression!")
            else:
                return eval(self.expression, {"__builtins__": None}, self._all)
        except:
            raise
