#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import BaolingxinTaluoTaluoNengliangShuziZhanbu
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('BaolingxinTaluoTaluoNengliangShuziZhanbu'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="baolingxin-taluo-taluo-nengliang-shuzi-zhanbu",
    version=BaolingxinTaluoTaluoNengliangShuziZhanbu.__version__,
    url="https://github.com/apachecn/baolingxin-taluo-taluo-nengliang-shuzi-zhanbu",
    author=BaolingxinTaluoTaluoNengliangShuziZhanbu.__author__,
    author_email=BaolingxinTaluoTaluoNengliangShuziZhanbu.__email__,
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
    description="宝灵心塔罗：塔罗能量数字占卜",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "baolingxin-taluo-taluo-nengliang-shuzi-zhanbu=BaolingxinTaluoTaluoNengliangShuziZhanbu.__main__:main",
            "BaolingxinTaluoTaluoNengliangShuziZhanbu=BaolingxinTaluoTaluoNengliangShuziZhanbu.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
