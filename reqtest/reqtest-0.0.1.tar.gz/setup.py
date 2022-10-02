# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reqtest']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'reqtest',
    'version': '0.0.1',
    'description': 'Automate everything HTTP.',
    'long_description': None,
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/vcokltfre/reqtest',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
