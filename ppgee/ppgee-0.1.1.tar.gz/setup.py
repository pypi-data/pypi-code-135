# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ppgee', 'ppgee.pages']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0', 'beautifulsoup4>=4.11.1,<5.0.0']

entry_points = \
{'console_scripts': ['ppgee = ppgee.__main__:main']}

setup_kwargs = {
    'name': 'ppgee',
    'version': '0.1.1',
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
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
