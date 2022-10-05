# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sqeleton']

package_data = \
{'': ['*']}

install_requires = \
['runtype>=0.2.6,<0.3.0']

setup_kwargs = {
    'name': 'sqeleton',
    'version': '0.0.1',
    'description': 'Library for building SQL queries',
    'long_description': '# Sqeleton',
    'author': 'Erez Shinan',
    'author_email': 'erezshin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/erezsh',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
