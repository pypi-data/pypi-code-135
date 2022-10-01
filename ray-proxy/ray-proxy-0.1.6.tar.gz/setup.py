# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ray_proxy']

package_data = \
{'': ['*']}

install_requires = \
['bidict', 'loguru', 'ray>=2.0.0,<3.0.0', 'returns']

setup_kwargs = {
    'name': 'ray-proxy',
    'version': '0.1.6',
    'description': 'A library which enables the creation of proxy variables for remote python interpreter in ray cluster.',
    'long_description': None,
    'author': 'proboscis',
    'author_email': 'nameissoap@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
