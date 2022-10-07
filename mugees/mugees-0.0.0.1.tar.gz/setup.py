#!/usr/bin/env python

from setuptools import find_packages, setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
    name="mugees",
    version="0.0.0.1",
    description="A python library for detecting depressive comments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Muhammad Mugees Asif",
    install_requires=[
        "transformers != 4.18.0",  # v4.18.0 fails to properly load the finetuned weights
        "torch >= 1.7.0",
        "sentencepiece >= 0.1.94",
    ],
    packages=find_packages(include=["mugees"], exclude=["tests", "src"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
