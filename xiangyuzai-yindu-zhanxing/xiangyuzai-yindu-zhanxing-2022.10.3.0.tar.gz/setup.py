#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import XiangyuzaiYinduZhanxing
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('XiangyuzaiYinduZhanxing'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="xiangyuzai-yindu-zhanxing",
    version=XiangyuzaiYinduZhanxing.__version__,
    url="https://github.com/apachecn/xiangyuzai-yindu-zhanxing",
    author=XiangyuzaiYinduZhanxing.__author__,
    author_email=XiangyuzaiYinduZhanxing.__email__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Natural Language :: Chinese (Simplified)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Documentation",
        "Topic :: Documentation",
    ],
    description="相遇在印度占星",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "xiangyuzai-yindu-zhanxing=XiangyuzaiYinduZhanxing.__main__:main",
            "XiangyuzaiYinduZhanxing=XiangyuzaiYinduZhanxing.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
