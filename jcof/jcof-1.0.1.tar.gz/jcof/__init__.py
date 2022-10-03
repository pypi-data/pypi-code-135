#!/usr/bin/env python3
# coding=utf-8
# SPDX-License-Identifier: GPL-3.0-or-later
"""
JCOF: JSON-like Compact Object Format

JCOF is a drop-in replacement for JSON, and aims to compact JSON, both
by utilizing string lookup tables and eliminating whitespace.

This is a Python port of `<https://github.com/mortie/jcof>`_; specifically, the
`reference implementation <https://github.com/mortie/jcof/tree/main/implementations/javascript>`_.

The :mod:`jcof` module provides 4 basic JCOF serialization functions. Their signatures are
similar to :mod:`json`, *but not identical*.

- :func:`dumps(obj)`, for Python -> JCOF
- :func:`loads(jcof)`, for JCOF -> Python
- :func:`dump(obj, fp)`, for Python -> JCOF as file
- :func:`load(jcof, fp)` for JCOF -> Python as file

.. warning:: These functions do not implement :mod:`json`'s
    ``skipkeys, cls, ensure_ascii`` and the like; only ``obj`` and ``s``.

.. warning:: The data returned by these functions is **not** immediately-valid JSON data;
    it is a Python value. Use :mod:`json` to load and dump converted Python values back to JSON.

The Javascript implementation's ``parse`` and ``stringify`` functions are still available,
but in :mod:`jcof.loading` and :mod:`jcof.dumping` respectively. They have the same signature.

----

You should read `<https://github.com/mortie/jcof>`_ for information on the format,
but for a condensed version:

A JCOF string is made up of three "tables": ``"<string table>?;<object table>?;<value>"``, where:

* |``<string table>`` is a comma-separated list of duplicated strings.
  | Their index in this list is their "string ID".

* | ``<object table>`` is a quote-split list of duplicated dictionary keys.
  | These are used to construct dictionaries that have the same key structure.

* ``<value>`` is either a compacted list, dictionary, number, string, boolean, or None.

Numbers outside 0 to 10 are encoded in
`base62 <https://en.wikipedia.org/wiki/Base62>`_ to save space.
"""
import jcof.dumping
import jcof.loading

__version__ = "1.0.1"
__author__ = "WhoAteMyButter"

EXAMPLE = {
    "people": [
        {"first-name": "Bob", "age": 32, "occupation": "Plumber", "full-time": True},
        {
            "first-name": "Alice",
            "age": 28,
            "occupation": "Programmer",
            "full-time": True,
        },
        {"first-name": "Bernard", "age": 36, "occupation": None, "full-time": None},
        {"first-name": "El", "age": 57, "occupation": "Programmer", "full-time": False},
    ]
}


def dumps(obj) -> str:
    """
    Serialize ``obj`` to a JCOF string.

    :param obj: Any non-class Python object.
    :return: A JCOF string of ``obj``.
    """
    return jcof.dumping.stringify(obj)


def dump(obj, file_pointer):
    """
    Same as :func:`jcof.dumps`, but writes to a file pointer instead.

    :param obj: Any non-class Python object.
    :param file_pointer: A file pointer.
    """
    file_pointer.write(dumps(obj))


def load(file_pointer):
    """
    Same as :func:`jcof.loads`, but reads from a file pointer instead.

    :param file_pointer: A file pointer.
    """
    with open(file_pointer, encoding="utf-8") as open_fp:
        return loads(open_fp.read())


def loads(jcof_string: str):
    """
    Deserialize ``jcof_string`` (a string containing a JCOF document) to a Python object.

    :param jcof_string: The JCOF string.
    """
    return jcof.loading.parse(jcof_string)
