import argparse
import copy
import json
import os
from jsonschema import validate

VALID_ARGUMENT_KWARGS = ["name", "abbrev", "action", "nargs", "const", "default", "type", "choices", "required", "help", "metavar", "dest", "mutually_exclusive_group"]

ARGPARSEJSON_DIR = os.path.abspath(os.path.dirname(__file__))
SCHEMA = json.load(open(os.path.join(ARGPARSEJSON_DIR, "schema.json"), "r"))

def getType(s:str):
    if s is None:
        return

    if type(s) != str:
        return type(s)

    s = s.lower()

    if s == "int" or s == "integer":
        return int
    elif s == "bool" or s == "boolean":
        return bool
    elif s == "str" or s == "string":
        return str
    elif s == "float":
        return float
    else:
        return None

class MyArgParser(argparse.ArgumentParser):
    def __init__(self, prog=None, add_help=True):
        self.add_help=add_help
        super().__init__(prog=prog, add_help=add_help)

    def exit(self, status=0, message=None):
        if status:
            if self.add_help:
                super().exit(status=status, message=message)

def _parse_kwargs(parser, kwargs:dict):
    abbrev = kwargs.pop('abbrev') if kwargs.get('abbrev') is not None else None
    name = kwargs.pop('name') if kwargs.get('name') is not None else None

    if kwargs.get('type') is not None:
        kwargs['type'] = getType(kwargs.get('type'))

    if kwargs.get("action") == "store_true":
        if kwargs.get("type") is not None:
            del kwargs["type"]
        if kwargs.get("default") is not None:
            del kwargs["default"]

    if abbrev is None:
        args = [name]
    else:
        args = [abbrev, name]

    parser.add_argument(*args, **kwargs)

def _parse_args(parser, commands:dict):
    for arg in commands.get('args', []):
        kwargs = copy.deepcopy(arg)
        for k in kwargs.keys():
            if k not in VALID_ARGUMENT_KWARGS:
                raise ValueError("'{}' is an unexpected keyword argument for argparse".format(k))

        if kwargs.get("mutually_exclusive_group") is not None:
            mutually_exclusive_parser = parser.add_mutually_exclusive_group(required=kwargs["mutually_exclusive_group"].get("required"))

            _parse_args(mutually_exclusive_parser, kwargs["mutually_exclusive_group"])
        else:
            _parse_kwargs(parser, kwargs)

def _parse_subparsers(parser, commands:dict):
    if len(commands.get("subparsers", [])) > 0:
        if commands.get("subparser_params") is not None:
            kwargs = copy.deepcopy(commands.get("subparser_params"))
            subparsers = parser.add_subparsers(**kwargs)
        else:
            subparsers = parser.add_subparsers()

        for sbp in commands["subparsers"]:
            aliases = [sbp.get('abbrev')] if sbp.get('abbrev') is not None else []
            sub_parser = subparsers.add_parser(sbp.get('name'), aliases=aliases, add_help=True)

            _parse_subparsers(sub_parser, sbp)

            _parse_args(sub_parser, sbp)

def parse_arguments(commands_file, prog=None, add_help=True):
    if isinstance(commands_file, str):
        commands = json.load(open(os.path.abspath(commands_file), "r"))
    elif isinstance(commands_file, dict):
        commands = commands_file
    else:
        raise TypeError("Expected either parameter of type '{}' or '{}' for parameter '{}', but instead received type '{}'".format(str, dict, "commands_file", type(commands_file)))

    validate(instance=commands, schema=SCHEMA)

    parser = MyArgParser(prog=prog, add_help=add_help)

    _parse_args(parser, commands)

    _parse_subparsers(parser, commands)

    return parser
