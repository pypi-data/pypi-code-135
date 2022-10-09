# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ui_compiler']

package_data = \
{'': ['*'], 'ui_compiler': ['js/*', 'styles/*']}

install_requires = \
['cssselect>=1.1.0,<2.0.0', 'lxml>=4.9.0,<5.0.0']

setup_kwargs = {
    'name': 'ui-compiler',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
