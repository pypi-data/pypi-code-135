#!/usr/bin/env python3

from setuptools import setup

setup(
    entry_points={
        'console_scripts': ['joj-auth=joj_auth.command_line:main'],
    }
)
