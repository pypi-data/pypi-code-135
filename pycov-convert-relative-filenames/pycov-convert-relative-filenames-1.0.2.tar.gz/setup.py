#!/usr/bin/env python3
from setuptools import setup

setup(
    entry_points={
        "console_scripts": [
            "pycov-convert-relative-filenames = pycov_convert_relative_filenames.__main__:main",
        ],
    },
)
