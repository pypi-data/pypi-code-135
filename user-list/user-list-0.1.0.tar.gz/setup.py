# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['user_list']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<2.0.0', 'pandas>=1.5.0,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'user-list',
    'version': '0.1.0',
    'description': 'Package to create a CSV or HTML file for a determine url.',
    'long_description': '',
    'author': 'Asdrubal Gonzalez Penton',
    'author_email': 'agpenton@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
