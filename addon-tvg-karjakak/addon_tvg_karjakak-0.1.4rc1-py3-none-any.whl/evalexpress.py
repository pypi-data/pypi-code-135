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


def main(root):
    root.title("Expression")
    root.eval('tk::PlaceWindow . center')
    root.attributes('-topmost',True)

    def calc(event = None):
        try:
            nums = len(entry.get())
            if nums > 101:
                raise Exception(f"{nums} charcters, is exceeding than 100 chars!")
            for i in entry.get():
                if i not in tuple(digits + "*/-+()%. "):
                    raise ValueError(f"{i!r} is not acceptable expression!")
            ms = EvalExp(entry.get(), None)
            messagebox.showinfo("Results", f"{ms.evlex()}", parent=root)
        except Exception as e:
            # raise e
            messagebox.showerror("Error Message", e, parent=root)

    entry = tk.Entry(root)
    entry.pack(padx=2, pady=2, fill=tk.BOTH)
    button = tk.Button(root, text="Calculation", command=calc)
    button.pack(fill=tk.BOTH)
    button.bind_all("<Return>", calc)
    entry.focus()
    root.mainloop()