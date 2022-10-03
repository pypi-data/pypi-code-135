#!/usr/bin/env python3
# coding=utf-8
# SPDX-License-Identifier: GPL-3.0-or-later
"""Functions for translating Python -> JCOF."""
import collections
import dataclasses
import json
import math
import re

import jcof.loading


def stringify(value) -> str:
    writer = StringWriter()
    analysis = analyze(value)

    stringify_string_table(writer, analysis.string_list)
    writer.write(";")
    stringify_objectshape_table(writer, analysis)
    writer.write(";")
    stringify_value(writer, analysis, value)
    return writer.string


class StringWriter:
    def __init__(self):
        self.string = ""
        self.next_maybe_sep = None
        self.prev_char = None

    @staticmethod
    def issep(char: str) -> bool:
        """
        Return if ``char`` is a separator: ``[]{}(),:"``

        :param char: The character to test for.
        :return: If ``char`` is a separator.
        """
        return char[0] in '[]{}(),:"'

    def write(self, string: str):
        if self.next_maybe_sep:
            if not self.issep(self.prev_char) and not self.issep(string):
                self.string += self.next_maybe_sep
            self.next_maybe_sep = None

        self.string += string
        self.prev_char = string[-1]

    def maybesep(self, sep):
        if self.next_maybe_sep is not None:
            self.write(self.next_maybe_sep)
        self.next_maybe_sep = sep


def stringify_string_table(writer: StringWriter, string_list: list[str]):
    if len(string_list) == 0:
        return

    stringify_string(writer, string_list[0])
    for i in range(1, len(string_list)):
        writer.maybesep(",")
        stringify_string(writer, string_list[i])


def stringify_string(writer: StringWriter, string: str):
    if re.match("^[a-zA-Z0-9]+$", string):
        writer.write(string)
    else:
        writer.write(json_dumps_compact(string))


@dataclasses.dataclass
class Analysis:
    """A dataclass of the result from """
    string_list: list[str]
    string_ids: dict
    object_shape_list: list[list]
    object_shape_ids: dict


def stringify_objectshape_table(writer: StringWriter, meta: Analysis):
    if not meta.object_shape_list:
        return

    stringify_objectshape(writer, meta, meta.object_shape_list[0])
    for i in range(1, len(meta.object_shape_list)):
        writer.write(",")
        stringify_objectshape(writer, meta, meta.object_shape_list[i])


def stringify_objectshape(writer: StringWriter, meta: Analysis, shape):
    stringify_object_key(writer, meta.string_ids, shape[0])
    for i in range(1, len(shape)):
        writer.maybesep(":")
        stringify_object_key(writer, meta.string_ids, shape[i])


def stringify_object_key(writer: StringWriter, string_ids: dict, key) -> None:
    """
    Write an object key to ``writer``.
    If the key is already present in the string IDs, it will be written as a Base62 ID.
    If not, it will be written as a JSON-compatible string.

    :param writer: The writer instance.
    :param string_ids: A dictionary of ``{key_string: id}``.
    :param key: The key to search for.
    """
    if string_id := string_ids.get(key):
        stringify_base62(writer, string_id)
    else:
        writer.write(json_dumps_compact(key))


def stringify_base62(writer: StringWriter, number: float | int) -> None:
    """
    Convert ``num`` into a Base62 string, and write it to ``writer``.

    Parts from `<https://stackoverflow.com/a/2549514>`_.

    :param writer: The writer instance.
    :param number: The number to convert.
    """
    codepoints: collections.deque[int] = collections.deque()
    while True:
        codepoints.append(ord(jcof.loading.BASE62_ALPHABET[number % 62]))
        if not (number := math.floor(number / 62)) > 0:
            break
    for codepoint in reversed(codepoints):
        writer.write(chr(codepoint))


def stringify_value(writer: StringWriter, meta: Analysis, value):
    if isinstance(value, list):
        writer.write("[")
        if len(value) == 0:
            writer.write("]")
            return

        stringify_value(writer, meta, value[0])
        for index in range(1, len(value)):
            writer.maybesep(",")
            stringify_value(writer, meta, value[index])
        writer.write("]")
    elif isinstance(value, dict) and value:
        keys = sorted(value.keys())
        if (shape_id := meta.object_shape_ids.get(json_dumps_compact(keys))) is None:
            stringify_keyed_object_value(writer, meta, value, keys)
        else:
            stringify_shaped_object_value(writer, meta, value, keys, shape_id)
    # Must also be above ifnumber, bools are int but ints aren't bools
    elif isinstance(value, bool):
        if value:
            writer.write("b")
        else:
            writer.write("B")
    elif isinstance(value, (float, int)):
        if (isinstance(value, int) or value == math.floor(value)) and (value < 0 or value > 10):
            if value < 0:
                writer.write("I")
                stringify_base62(writer, -value)
            else:
                writer.write("i")
                stringify_base62(writer, value)
        elif math.isinf(value) or math.isnan(value):
            writer.write("n")
        else:
            # JavaScript's float to string function seems to always generate a
            # JCOF-compatible string
            writer.write(str(value))

    elif isinstance(value, str):
        if (string_id := meta.string_ids.get(value)) is None:
            writer.write(json_dumps_compact(value))
        else:
            writer.write("s")
            stringify_base62(writer, string_id)
    elif value is None:
        writer.write("n")
    else:
        raise ValueError(f"Can't serialize value: {value}")


def stringify_shaped_object_value(
        writer: StringWriter,
        meta: Analysis,
        value,
        keys,
        shape_id: int,
) -> None:
    writer.write("(")
    stringify_base62(writer, shape_id)
    if len(keys) == 0:
        writer.write(")")
        return

    for key in keys:
        writer.maybesep(",")
        stringify_value(writer, meta, value[key])

    writer.write(")")


def stringify_keyed_object_value(
        writer: StringWriter, meta: Analysis, value, keys
):
    writer.write("{")
    if len(keys) == 0:
        writer.write("}")
        return

    stringify_key_value_pair(writer, meta, keys[0], value[keys[0]])
    for i in range(1, len(keys)):
        writer.maybesep(",")
        stringify_key_value_pair(writer, meta, keys[i], value[keys[i]])

    writer.write("}")


def stringify_key_value_pair(
        writer: StringWriter, meta: Analysis, key, value
):
    stringify_object_key(writer, meta.string_ids, key)
    writer.maybesep(":")
    stringify_value(writer, meta, value)


@dataclasses.dataclass
class ObjectShape:
    """An object shape."""
    count: int
    keys: list


@dataclasses.dataclass
class StringCount:
    """A simple string occurence counter."""
    count: int = 1


def analyze_value(
        value: list or dict or str,
        strings: dict[str, StringCount],
        object_shapes: dict[str, ObjectShape],
):
    """
    Modifies strings, object_shapes in place.
    Value is untouched.

    :param value: The value to analyze.
    :param strings: A dictionary of ``{string: count}``.
    :param object_shapes: A dictionary of ``{object id: shape}``.
    """
    if not value:
        pass
    if isinstance(value, list):
        for val in value:
            analyze_value(val, strings, object_shapes)
    elif isinstance(value, dict):
        keys = sorted(list(value.keys()))
        if len(keys) > 1:
            if shape := object_shapes.get(shape_hash := json_dumps_compact(keys)):
                shape.count += 1
            else:
                object_shapes[shape_hash] = ObjectShape(1, keys)
        elif len(keys) == 1:
            if string := strings.get(keys[0]):
                string.count += 1
            else:
                strings[keys[0]] = StringCount()
        for key in keys:
            analyze_value(value[key], strings, object_shapes)
    elif isinstance(value, str):
        if string := strings.get(value):
            string.count += 1
        else:
            strings[value] = StringCount()


def analyze(value) -> Analysis:
    """
    Given a value, return stringlist, stringids, objectshapelist, objectshapeids.

    :param value: The value to analyze.
    :return: An :class:`Analysis` instance.
    """
    strings: dict[str, StringCount] = {}
    object_shapes: dict[str, ObjectShape] = {}
    analyze_value(value, strings, object_shapes)
    for shape_hash, shape in list(object_shapes.items()):
        if shape.count == 1:
            del object_shapes[shape_hash]
        for key in shape.keys:
            if (string := strings.get(key)) is None:
                strings[key] = StringCount()
            else:
                string.count += 1

    for string, string_count in list(strings.items()):
        if string_count.count == 1:
            del strings[string]

    string_list: list[str] = sorted(strings.keys(), key=lambda a: strings[a].count)
    string_ids: dict[str, int] = {}
    for index, string_id in enumerate(string_list):
        string_ids[string_id] = index

    object_shape_list: list[list] = []
    object_shape_ids: dict[str, int] = {}
    for shape_hash, shape in object_shapes.items():
        object_shape_ids[shape_hash] = len(object_shape_list)
        object_shape_list.append(shape.keys)

    return Analysis(string_list, string_ids, object_shape_list, object_shape_ids)


def json_dumps_compact(string) -> str:
    """
    Mimic Javascript's `JSON.stringify()`, return string as a JSON string but without separation.

    :param string: The string.
    :return: A compact JSON string.
    """
    return json.dumps(string, separators=(",", ":"), ensure_ascii=False)
