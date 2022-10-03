# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dummy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'my-pyside6-build',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Nir',
    'author_email': '88795475+nrbnlulu@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
