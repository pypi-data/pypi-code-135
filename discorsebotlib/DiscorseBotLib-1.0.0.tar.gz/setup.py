# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.base']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'discorsebotlib',
    'version': '1.0.0',
    'description': 'A bot lib for Discorse based Fourms',
    'long_description': None,
    'author': 'ShowierData9978',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
