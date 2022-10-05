#!/usr/bin/env python
# coding: utf-8

# Copyright (c) KaivnD.
# Distributed under the terms of the Modified BSD License.

import pytest

from ..example import DisplayPortal


def test_example_creation_blank():
    w = DisplayPortal()
    assert w.value == 'Hello World'
