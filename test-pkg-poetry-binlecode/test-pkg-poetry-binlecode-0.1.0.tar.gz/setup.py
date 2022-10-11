# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_pkg_poetry_binlecode']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-pkg-poetry-binlecode',
    'version': '0.1.0',
    'description': '',
    'long_description': '\n\npyproject.toml is created by poetry with format of PEP 518 package specs.\n\n',
    'author': 'Bin Le',
    'author_email': 'bin.le.code@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
