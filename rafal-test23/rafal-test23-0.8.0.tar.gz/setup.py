# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rafaltest']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rafal-test23',
    'version': '0.8.0',
    'description': '',
    'long_description': None,
    'author': 'Rafał Majewski',
    'author_email': 'goodheropl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
