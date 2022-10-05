# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['anyrepo', 'anyrepo._cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0', 'coloredlogs', 'pydantic>=1.10.0', 'tomlkit']

entry_points = \
{'console_scripts': ['anyrepo = anyrepo._cli:main']}

setup_kwargs = {
    'name': 'anyrepo',
    'version': '0.4.0',
    'description': 'Multi Repository Management Tool',
    'long_description': 'None',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
