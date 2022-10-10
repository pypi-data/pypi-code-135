# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['drlogger']

package_data = \
{'': ['*']}

install_requires = \
['graypy>=2.1.0,<3.0.0', 'python-json-logger>=2.0.4,<3.0.0']

setup_kwargs = {
    'name': 'drlogger',
    'version': '1.0.2a0',
    'description': '',
    'long_description': '<h1 align="center">DrLogger</h1>\n<p align="center">A python package for logging</p>\n\n> :warning:\tNOT production ready, don\'t use in production\n',
    'author': 'Ajamal Khan',
    'author_email': '13559558+khan-ajamal@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
