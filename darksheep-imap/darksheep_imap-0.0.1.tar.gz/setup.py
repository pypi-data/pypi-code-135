import os
import re
import sys
import glob
import builtins
from contextlib import contextmanager

import setuptools
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from setuptools.command.install import install as _install

setup(
    name="darksheep_imap",
    version="0.0.1",
    author="Dark Sheep",
    description="Dark sheep's imap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
