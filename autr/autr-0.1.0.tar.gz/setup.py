# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autr']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'pandas>=1.3.5,<2.0.0']

setup_kwargs = {
    'name': 'autr',
    'version': '0.1.0',
    'description': 'Automatic file reader',
    'long_description': 'None',
    'author': 'Gabriel Guarisa',
    'author_email': 'gabrielguarisa@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
