from __future__ import annotations

from enum import Enum
from argparse import ArgumentParser
from types import new_class

Group = new_class('Group', (Enum,))

class Actions(dict, Enum):

    @staticmethod
    def fmt(fstr: str):
        return property(lambda _self: fstr.format(**_self.__dict__))
    
    @property
    def __dict__(self):
        return {
            'name': self.name,
            'group': type(self).__name__,
            'dest': self.name.upper()
        }
    def __init__(self, __v) -> None:
        self._value_ = __v | {'action': self.action.lower()}

    def __call__(self, **kwargs):
        return self.value | kwargs

class Parser(ArgumentParser):

    def init_group(self, arg_group, **kwargs) -> ArgumentParser:
        parser = self.add_argument_group(**kwargs)
        for arg in arg_group._member_map_.values():
            parser.add_argument(
                f"--{arg_group.__name__}-{arg.name}".lower(),
                dest = f"{arg_group.__name__}_{arg.name}".upper(),
                **arg.value)
        parser.title = arg_group.__name__.upper()
        return parser

    def __init__(self, *subparsers, **root_options) -> None:
        super().__init__(conflict_handler='resolve')
        for arg in Group('Root', root_options.items())._member_map_.values():
            self.add_argument(
                f"--{arg.name}".lower(),
                dest = arg.name,
                **arg.value)
        for asub in subparsers:
            self.init_group(asub)