# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['merge_csv']
install_requires = \
['PySimpleGUI>=4.60.3,<5.0.0', 'pandas>=1.4.3,<2.0.0']

entry_points = \
{'console_scripts': ['mcsv = merge_csv:merge_csv',
                     'merge_csv = merge_csv:merge_csv']}

setup_kwargs = {
    'name': 'merge-csv',
    'version': '0.1.1',
    'description': 'A Simple Program to Merge Multiple CSV Files Into One File',
    'long_description': '# Merge CSV\n\n## Installation\n```shell\npip install merge_csv\n```\n\n## Usage\n```shell\nmcsv  # or merge_csv\n```\n\n![screenshot](static/screenshot.png)\n',
    'author': 'Mohammad Alyetama',
    'author_email': 'malyetama@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Alyetama/Merge_CSV',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
