# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raicontours']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'raicontours',
    'version': '0.2.0',
    'description': '',
    'long_description': '# raicontours\n',
    'author': 'Simon Biggs',
    'author_email': 'simon.biggs@radiotherapy.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
