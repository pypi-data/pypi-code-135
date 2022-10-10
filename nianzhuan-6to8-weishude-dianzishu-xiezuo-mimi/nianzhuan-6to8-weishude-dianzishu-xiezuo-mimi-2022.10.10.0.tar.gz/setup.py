#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import Nianzhuan6to8WeishudeDianzishuXiezuoMimi
import os
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

for subdir, _, _ in os.walk('Nianzhuan6to8WeishudeDianzishuXiezuoMimi'):
    fname = path.join(subdir, '__init__.py')
    open(fname, 'a').close()
    
setuptools.setup(
    name="nianzhuan-6to8-weishude-dianzishu-xiezuo-mimi",
    version=Nianzhuan6to8WeishudeDianzishuXiezuoMimi.__version__,
    url="https://github.com/apachecn/nianzhuan-6to8-weishude-dianzishu-xiezuo-mimi",
    author=Nianzhuan6to8WeishudeDianzishuXiezuoMimi.__author__,
    author_email=Nianzhuan6to8WeishudeDianzishuXiezuoMimi.__email__,
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
    description="年赚6-8位数的电子书写作秘密",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[],
    install_requires=[],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            "nianzhuan-6to8-weishude-dianzishu-xiezuo-mimi=Nianzhuan6to8WeishudeDianzishuXiezuoMimi.__main__:main",
            "Nianzhuan6to8WeishudeDianzishuXiezuoMimi=Nianzhuan6to8WeishudeDianzishuXiezuoMimi.__main__:main",
        ],
    },
    packages=setuptools.find_packages(),
    package_data={'': ['*']},
)
