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
    'version': '1.0.0',
    'description': 'lookout',
    'long_description': '## Iterkit\n\nHelpful iter methods',
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
