# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyanypay', 'pyanypay.exceptions', 'pyanypay.types']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0', 'msgspec>=0.9.0,<0.10.0']

setup_kwargs = {
    'name': 'pyanypay',
    'version': '0.1.0',
    'description': 'Universal library for AnyPay API',
    'long_description': '# WIP\n',
    'author': 'FeeeeK',
    'author_email': '26704473+FeeeeK@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/FeeeeK/pyAnyPay',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
