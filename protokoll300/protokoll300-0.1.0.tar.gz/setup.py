# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['protokoll300']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'protokoll300',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Zofia Kubrak',
    'author_email': 'zofiakubrak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
