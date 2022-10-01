from io import open
from setuptools import setup

version = "1.1.5"

setup(
    name = "bigchin",
    version = version,
    author = "DFWastaken",
    author_email = "dfwastaken.work@gmail.com",
    description = (
        u"A small library for your projects"
    ),
    long_description = "https://raw.githubusercontent.com/DFekatsaW/Big-Chin./main/README.md",
    url = "https://github.com/DFekatsaW/Big-Chin.",
    download_url = "https://raw.githubusercontent.com/DFekatsaW/Big-Chin./main/bigchin.py",
    license = "Apache License 2.0",
    packages = ['bigchin_api'],
    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ]
)