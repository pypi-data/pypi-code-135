# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['iterkit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'iterkit',
    'version': '0.1.0',
    'description': 'helpful iter methods',
    'long_description': '## Iterkit\n',
    'author': 'wayfaring-stranger',
    'author_email': 'zw6p226m@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
