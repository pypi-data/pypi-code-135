#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
from visionx import __version__

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


def parse_requirements(filename):
    """ load requirements from a pip requirements file. (replacing from pip.req import parse_requirements)"""
    lineiter = (line.strip() for line in open(filename))
    reqs = [line for line in lineiter if line and not line.startswith("#")]
    return reqs


setup(
    name="visionx",
    version="{}".format(__version__),
    keywords=["vision", "utx", "yolox", "diff", "ui", "tools"],
    description='Video UI analysis tool!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',

    url="https://github.com/openutx",
    author="lijiawei",
    author_email="jiawei.li2@qq.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython"
    ],
    entry_points="""
    [console_scripts]
    visionx = visionx.server:main
    """,
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=parse_requirements('requirements.txt')

)
