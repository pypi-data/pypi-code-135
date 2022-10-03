# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['conda_pip_minimal']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'loguru>=0.6.0,<0.7.0',
 'more-itertools>=8.14.0,<9.0.0',
 'semver>=2.13.0,<3.0.0',
 'trio>=0.22.0,<0.23.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['conda-cpm = conda_pip_minimal.cli:app']}

setup_kwargs = {
    'name': 'conda-pip-minimal',
    'version': '0.1.0',
    'description': 'Conda+Pip minimal env exports',
    'long_description': None,
    'author': 'Venky Iyer',
    'author_email': 'indigoviolet@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
