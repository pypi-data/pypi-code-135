# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lmdemo']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.3,<2.0.0']

entry_points = \
{'console_scripts': ['lm_demo = lmdemo:__main__.main']}

setup_kwargs = {
    'name': 'lmdemo',
    'version': '1.0.0',
    'description': '',
    'long_description': None,
    'author': 'chase mateusiak',
    'author_email': 'chase.mateusiak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
