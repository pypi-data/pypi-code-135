# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['args_enum']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.1,<2.0.0']

setup_kwargs = {
    'name': 'args-enum',
    'version': '0.1.0',
    'description': 'Use Enums as containers for command-line options.',
    'long_description': 'None',
    'author': 'MKUltra-Violet',
    'author_email': 'clockworktux@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
