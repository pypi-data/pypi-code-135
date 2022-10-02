#!/usr/bin/env python
"""Telly Python client setup script
"""
# SPDX-License-Identifier: Apache-2.0
# (c) Copyright Telly, LLC 2022.

from setuptools import setup, find_packages

# get README content for metadata inclusion
with open("README.md") as readme_file:
    readme = readme_file.read()

# setup requirements lists - yes, these are empty!
requirements = []

# setup config to import outside of setup() call
VERSION = "0.9.2"

# setup package metadata object
setup(
    author="Telly LLC",
    author_email="it@gotelly.io",
    maintainer="Telly LLC",
    python_requires=">=2.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Development Status :: 4 - Beta",
    ],
    install_requires=requirements,
    license="Apache-2.0",
    description="telly - simple, privacy-friendly usage statistics for your open source software",
    long_description=readme,
    description_content_type="text/markdown",
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="telly, telemetry, statistics, privacy, open source, usage",
    name="telly",
    package_dir={"": "lib"},
    py_modules=["telly"],
    url="https://github.com/telly-llc/",
    version=VERSION,
)
