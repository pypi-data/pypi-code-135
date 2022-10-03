"""Scratch module."""

from collections.abc import Sequence
import logging
from typing import TypedDict

from pytyu.json import is_json_schema


class TD(TypedDict):
    """A TypedDict."""

    a: str
    b: int
    c: Sequence[str]
    d: Sequence[int, str]


logging.basicConfig(level=0)

logging.debug("Simple types")
is_json_schema({"x": 1}, TD)
is_json_schema({"a": 1}, TD)

logging.debug("List types")
is_json_schema({"x": [1]}, TD)
is_json_schema({"b": [1]}, TD)
is_json_schema({"d": [1]}, TD)
is_json_schema({"c": [1, "2"]}, TD)

logging.debug("Dict types")
is_json_schema({"x": {"a": 1}}, TD)
