# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wiki_random']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'wiki-random',
    'version': '0.1.5',
    'description': 'get random article from wikipedia',
    'long_description': '',
    'author': 'Igor Moryto',
    'author_email': '56959606+Ezykill@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ezykill/wiki_random',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
