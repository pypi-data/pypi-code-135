# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fixed_that_for_you']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fixed-that-for-you',
    'version': '1.0.0',
    'description': 'A Python library that fixes attribute name misspellings',
    'long_description': None,
    'author': 'megahomyak',
    'author_email': 'g.megahomyak@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
