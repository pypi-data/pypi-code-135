# -*- coding: UTF-8 -*-
"""
Created on 06.10.22
Script for indexing text files using line offsets.

:author:     Martin Dočekal
"""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(name='fileindexer',
      version='1.0.2',
      description='Script for indexing text files using line offsets.',
      long_description_content_type="text/markdown",
      long_description=README,
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      entry_points={
          'console_scripts': [
              'fileindexer = fileindexer.__main__:main'
          ]
      },
      author='Martin Dočekal',
      keywords=['indexing', 'text files'],
      url='https://github.com/mdocekal/fileindexer',
      python_requires='>=3.6',
      install_requires=[
          "tqdm>=4.62.3"
      ]
      )
