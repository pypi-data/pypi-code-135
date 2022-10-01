# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simulatte']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'simulatte',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Davide Mezzogori',
    'author_email': 'dmezzogori@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
