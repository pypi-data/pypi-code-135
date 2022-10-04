# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trackerstatus']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'trackerstatus',
    'version': '0.1.0',
    'description': 'A python library for gathering data from the trackerstatus.info website',
    'long_description': '',
    'author': 'mauvehed',
    'author_email': 'mh@mvh.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
