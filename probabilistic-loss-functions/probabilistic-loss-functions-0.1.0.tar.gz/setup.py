# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['probabilistic_loss_functions']

package_data = \
{'': ['*']}

install_requires = \
['tensorflow-probability>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'probabilistic-loss-functions',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ninpnin',
    'author_email': 'vainoyrjanainen@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
