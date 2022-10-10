# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['oiseau']

package_data = \
{'': ['*'], 'oiseau': ['cpp/*']}

install_requires = \
['numpy>=1.22.4,<2.0.0', 'scipy>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'oiseau',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'tiagovla',
    'author_email': 'tiagovla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
