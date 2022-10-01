""" jouissance """

import os
import glob
import pytest


def test_jouissance(pattern=None):
    """ run the test suite """
    if pattern is None:
        return pytest.main([
            "-vv",
            "-rA",
            os.path.dirname(os.path.realpath(__file__))
        ])

    return [pytest.main([
        "-vv",
        "-rA",
        _fn
    ]) for _fn in glob.glob(
        os.path.dirname(os.path.realpath(__file__)) +
        f"/test/*{pattern}*.py")]


__version__ = "0.1.8"
