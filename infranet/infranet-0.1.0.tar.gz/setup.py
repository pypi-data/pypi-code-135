# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['infranet']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.8.6,<3.0.0']

setup_kwargs = {
    'name': 'infranet',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Nishant Yadav',
    'author_email': 'nishant.um@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
