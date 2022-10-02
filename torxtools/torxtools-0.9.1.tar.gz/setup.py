#!/usr/bin/env python3

from setuptools import setup

with open("requirements.txt", "r", encoding="UTF-8") as f:
    requirements = f.read().splitlines()

setup(install_requires=requirements)
