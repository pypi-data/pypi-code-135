# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rate_limiters']

package_data = \
{'': ['*']}

install_requires = \
['ready-logger>=0.1.0,<0.2.0']

extras_require = \
{'distributed': ['redis>=4.1.1,<5.0.0']}

setup_kwargs = {
    'name': 'rate-limiters',
    'version': '0.2.8',
    'description': 'Rate limiters for APIs and web scraping.',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
