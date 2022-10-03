# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reddio']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp']

setup_kwargs = {
    'name': 'reddio',
    'version': '0.0.2',
    'description': 'A simple GET only reddit API wrapper',
    'long_description': 'None',
    'author': 'VarMonke',
    'author_email': 'var.monke@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
