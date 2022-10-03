# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gcc_play']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['gcc_play = gcc_play.cli:gcc_play']}

setup_kwargs = {
    'name': 'gcc-play',
    'version': '0.2.0',
    'description': 'linux commands built with python for my own use.',
    'long_description': 'None',
    'author': 'rai',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
