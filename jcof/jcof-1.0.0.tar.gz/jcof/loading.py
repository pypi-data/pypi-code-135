#!/usr/bin/env python3
# coding=utf-8
# SPDX-License-Identifier: GPL-3.0-or-later
"""Functions for translating JCOF -> Python."""
import json

BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
BASE62_ALPHANUM: dict[str, int] = {char: index for index, char in enumerate(
    BASE62_ALPHABET)}


def parse(string: str):
    reader = StringReader(string)
    string_table = parse_string_table(reader)
    reader.skip(";")
    object_shape_table = parse_objectshape_table(reader, string_table)
    reader.skip(";")
    return parse_value(reader, string_table, object_shape_table)


class StringReader:
    """
    A simple peekable string buffer.
    """
    def __init__(self, string: str):
        self.string = string
        self.index = 0

    def peek(self) -> str | None:
        """
        Return the character ahead of the current index,
        or None if the end of the buffer has been reached.
        """
        if self.index < len(self.string):
            return self.string[self.index]
        return None

    def consume(self):
        """
        Increase the index, moving ahead the current character.
        """
        self.index += 1

    def skip(self, char):
        """
        Advance the reader by one and expect that it's character is `char`. If not, raise a
        :exc:`ParseError`.

        :param char: The expected character.
        """
        if (peeked := self.peek()) != char:
            raise ParseError(f"Unexpected char: Expected '{char}', got '{peeked}'", self.index)
        self.consume()

    def maybeskip(self, char):
        """
        Skip only if the next character is `char`, otherwise do nothing.

        :param char: The possible character to test for.
        """
        if self.peek() == char:
            self.consume()


def parse_string_table(reader: StringReader) -> list[str]:
    if reader.peek() == ";":
        return []

    strings = []
    while True:
        strings.append(parse_string(reader))
        if (char := reader.peek()) == ";":
            return strings
        if char == ",":
            reader.consume()


def parse_string(reader: StringReader):
    if reader.peek() == '"':
        return parse_json_string(reader)
    if reader.peek() in BASE62_ALPHABET:
        return parse_plain_string(reader)
    raise ParseError("Expected plain string or JSON string", reader.index)


def parse_plain_string(reader: StringReader):
    string = reader.peek()
    reader.consume()
    while True:
        if not (char := reader.peek()) in BASE62_ALPHABET:
            return string
        string += char
        reader.consume()


def parse_json_string(reader: StringReader):
    start = reader.index
    reader.skip('"')
    while True:
        char = reader.peek()
        reader.consume()
        if char == '"':
            break
        if char == "\\":
            reader.consume()
        elif char is None:
            raise ParseError("Unexpected EOF", reader.index)
    return json.loads(reader.string[start : reader.index])


def parse_objectshape_table(reader: StringReader, string_table: list[str]) -> list[list]:
    if reader.peek() == ";":
        return []

    shapes = []
    while True:
        shapes.append(parse_objectshape(reader, string_table))
        if (char := reader.peek()) == ";":
            return shapes
        if char == ",":
            reader.consume()


def parse_objectshape(reader: StringReader, string_table: list[str]):
    shape = []
    while True:
        shape.append(parse_object_key(reader, string_table))
        if (char := reader.peek()) in (",", ";"):
            return shape
        if char == ":":
            reader.consume()


def parse_object_key(reader: StringReader, string_table: list[str]) -> str:
    if reader.peek() == '"':
        return parse_json_string(reader)
    if (string_id := parse_base62(reader)) >= len(string_table):
        raise ParseError(f"String ID {string_id} out of range", reader.index)
    return string_table[string_id]


def parse_base62(reader: StringReader) -> int:
    if not reader.peek() in BASE62_ALPHABET:
        raise ParseError("Expected base62 value", reader.index)

    num = 0
    while True:
        num *= 62
        num += BASE62_ALPHANUM[reader.peek()]
        reader.consume()
        if not reader.peek() in BASE62_ALPHABET:
            return num


def parse_value(reader: StringReader, string_table, object_shape_table):
    if (char := reader.peek()) == "[":
        return parse_list_value(reader, string_table, object_shape_table)
    if char == "(":
        return parse_shaped_object_value(reader, string_table, object_shape_table)
    if char == "{":
        return parse_keyed_object_value(reader, string_table, object_shape_table)
    if char in "iIf0123456789-":
        return parse_number_value(reader)
    if char in 's"':
        return parse_string_value(reader, string_table)
    if char == "b":
        reader.consume()
        return True
    if char == "B":
        reader.consume()
        return False
    if char == "n":
        reader.consume()
        return
    raise ParseError(f"Expected value, got '{char}'", reader.index)


def parse_list_value(reader: StringReader, string_table, objectshape_table):
    reader.skip("[")
    if reader.peek() == "]":
        reader.consume()
        return []

    array = []
    while True:
        array.append(parse_value(reader, string_table, objectshape_table))
        if (char := reader.peek()) == "]":
            reader.consume()
            return array
        if char == ",":
            reader.consume()


def parse_shaped_object_value(reader: StringReader, string_table, objectshape_table):
    reader.skip("(")
    if (shape_id := parse_base62(reader)) >= len(objectshape_table):
        raise ParseError(f"Shape ID {shape_id} out of range", reader.index)

    obj = {}
    for key in objectshape_table[shape_id]:
        if reader.peek() == ",":
            reader.consume()
        obj[key] = parse_value(reader, string_table, objectshape_table)

    reader.skip(")")
    return obj


def parse_keyed_object_value(reader: StringReader, string_table, objectshape_table):
    reader.skip("{")
    if reader.peek() == "}":
        reader.consume()
        return {}

    obj = {}
    while True:
        key = parse_object_key(reader, string_table)
        if reader.peek() == ":":
            reader.consume()

        obj[key] = parse_value(reader, string_table, objectshape_table)
        if (char := reader.peek()) == ",":
            reader.consume()
        elif char == "}":
            reader.consume()
            return obj


def parse_number_value(reader: StringReader):
    if (char := reader.peek()) == "i":
        reader.consume()
        return parse_base62(reader)
    if char == "I":
        reader.consume()
        return -parse_base62(reader)
    return parse_float_value(reader)


def parse_float_value(reader: StringReader):
    # Here, we read the float, but then use JavaScript's float parser,
    # because making a float parser and serializer pair
    # which can round-trip any number is apparently pretty hard

    string = ""
    if (char := reader.peek()) == "-":
        string += char
        reader.consume()

    while (char := reader.peek()).isdigit():
        string += char
        reader.consume()

    if string in ("", "-"):
        raise ParseError("Zero-length number in float literal", reader.index)

    if (char := reader.peek()) == ".":
        string += char
        reader.consume()

        while (char := reader.peek()).isdigit():
            string += char
            reader.consume()

        if string[-1] == ".":
            raise ParseError(
                "Zero-length fractional part in float literal", reader.index
            )

    if (char := reader.peek()) in ("E", "e"):
        string += char
        reader.consume()

        if (char := reader.peek()) in ("+", "-"):
            string += char
            reader.consume()

        while (char := reader.peek()).isdigit():
            string += char
            reader.consume()

        if not string[-1].isdigit():
            raise ParseError(
                "Zero-length exponential part in float literal", reader.index
            )

    return float(string)


def parse_string_value(reader: StringReader, string_table):
    if reader.peek() == '"':
        return parse_json_string(reader)
    reader.skip("s")
    if (string_id := parse_base62(reader)) >= len(string_table):
        raise ParseError(f"String ID {string_id} out of range", reader.index)
    return string_table[string_id]


class ParseError(Exception):
    """
    Exception for when parsing fails.
    An index of where the error occured must be passed.

    :param msg: The message.
    :param index: An integer index of where in the JCOF string made an error occur.
    """
    def __init__(self, msg: str, index: int):
        super(msg)
        self.msg = msg
        self.index = index
