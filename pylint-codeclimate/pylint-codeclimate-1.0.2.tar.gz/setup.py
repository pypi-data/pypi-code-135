#!/usr/bin/env python3

from setuptools import setup

with open("requirements.txt", "r", encoding="UTF-8") as fd:
    requirements = fd.read().splitlines()

setup(install_requires=requirements)
