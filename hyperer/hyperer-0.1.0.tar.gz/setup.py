# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hyperer']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['hyperer-cargo = hyperer.hcargo:main',
                     'hyperer-rg = hyperer.hrg:main']}

setup_kwargs = {
    'name': 'hyperer',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Charlie Groves',
    'author_email': 'c@sevorg.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
