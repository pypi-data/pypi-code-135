# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aptos_sdk']

package_data = \
{'': ['*']}

install_requires = \
['PyNaCl>=1.5.0,<2.0.0', 'httpx>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'aptos-sdk',
    'version': '0.4.0',
    'description': 'Aptos SDK',
    'long_description': 'None',
    'author': 'Aptos Labs',
    'author_email': 'opensource@aptoslabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
