# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['running-tools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'running-tools',
    'version': '0.0.1',
    'description': 'A set of helpful tools for runners',
    'long_description': '# Running Tools\n\nA collection of tools for runners.\n\n## Pace Tool',
    'author': 'Ben Davidson',
    'author_email': 'benjamin@idavidson.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tukanuk/running-tools',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
