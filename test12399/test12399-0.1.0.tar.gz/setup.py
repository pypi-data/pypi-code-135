# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test12399']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['run_tester = entry:main']}

setup_kwargs = {
    'name': 'test12399',
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
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
