# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sdto']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'sdto',
    'version': '0.1.0',
    'description': 'Subdomain takeover finder',
    'long_description': 'None',
    'author': 'godpleaseno',
    'author_email': 'zfrty@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
