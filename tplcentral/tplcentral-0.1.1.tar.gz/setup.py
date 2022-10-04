#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
    tpl API

    :license: MIT, see LICENSE for more details

"""
from setuptools import setup


setup(
    name="tplcentral",
    version="0.1.1",
    url="https://github.com/candidco/python-tpl",
    license="MIT",
    author="Dhinesh D",
    author_email="dvdhinesh.mail@gmail.com",
    description="3PL REST API Client",
    long_description=open("README.rst").read(),
    packages=["client"],
    platforms="any",
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
