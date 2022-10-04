# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Creates file structure for python.'
LONG_DESCRIPTION = 'A package that allows to build a simple file structure for python.'

# Setting up
setup(
    name="pyfilestructure",
    version=VERSION,
    author="JDSNX",
    author_email="jdsnx24@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'structure', 'python structure'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)