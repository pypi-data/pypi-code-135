# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['powerbrain']

package_data = \
{'': ['*']}

install_requires = \
['requests']

setup_kwargs = {
    'name': 'powerbrain',
    'version': '0.1.0',
    'description': 'A simple library for interfacing with the REST API of cFos Powerbrain / charging manager EV wallbox charging controllers.',
    'long_description': '# py-powerbrain\nPython library for interfacing with a cFos Powerbrain wallbox or controller\n',
    'author': 'Kevin Read',
    'author_email': 'me@kevin-read.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
