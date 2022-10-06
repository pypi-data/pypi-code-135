# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycryptaes']

package_data = \
{'': ['*']}

install_requires = \
['pycryptodome>=3.15.0,<4.0.0']

setup_kwargs = {
    'name': 'pycryptaes',
    'version': '0.1.4',
    'description': 'Encrypt and Decrypt Data via AES encryption - a pycryptodome python package wrapper',
    'long_description': None,
    'author': 'Gwang Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
