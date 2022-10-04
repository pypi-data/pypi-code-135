# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ppgee', 'ppgee.pages']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'beautifulsoup4>=4.11.1,<5.0.0']

setup_kwargs = {
    'name': 'ppgee',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'tiagovla',
    'author_email': 'tiagovla@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
