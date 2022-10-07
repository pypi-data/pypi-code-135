#!/usr/bin/env python

"""Tests for `konesyntees.py` package."""


import unittest

from konesyntees.konesyntees import konesyntees


class TestKonesyntees(unittest.TestCase):
    """Tests for `konesyntees.py` package."""

    def test_000(self):
        """Test the package."""

        return print(konesyntees("Hello, world!", 1, -4))
    