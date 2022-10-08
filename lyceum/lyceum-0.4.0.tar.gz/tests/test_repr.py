#!/usr/bin/env python

"""Tests for `lyceum.repr` package."""
import pytest

from lyceum.repr import ascii2bin, bin2dec, dec2bin, dec2hex, hex2dec


def test_bin():
    # TODO
    assert bin2dec("111") == 7


def test_ascii2bin():
    with pytest.raises(AssertionError):
        ascii2bin("ab")
    with pytest.raises(AssertionError):
        ascii2bin("€")

    assert ascii2bin("O") == "01001111"
    assert ascii2bin("O", sep="_") == "0100_1111"
