# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['numpydoc_tools']

package_data = \
{'': ['*']}

install_requires = \
['numpydoc>=1.4.0,<2.0.0']

entry_points = \
{'console_scripts': ['main = src.main:main']}

setup_kwargs = {
    'name': 'numpydoc-tools',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Sam Hedin',
    'author_email': 'sam.hedin@gmail.com',
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
