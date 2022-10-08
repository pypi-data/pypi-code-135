# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sammy_poetry']

package_data = \
{'': ['*']}

install_requires = \
['requests==2.26.0']

setup_kwargs = {
    'name': 'sammy-poetry',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
