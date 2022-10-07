# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reactivetools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'reactivetools',
    'version': '0.1.0',
    'description': 'Typesafe, reactive tooling in Python with data descriptions',
    'long_description': '# Reactive Tools\n\nThis Pure-Python, no-dependency library brings reactivity to native Python.\n\n## Example\n\nTo see a working example, please refer to the tests.\n',
    'author': 'Sam Roeca',
    'author_email': 'samuel.roeca@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
