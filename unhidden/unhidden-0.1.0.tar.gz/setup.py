# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unhidden']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0', 'requests>=2.28.1,<3.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['unhidden = unhidden.main:app']}

setup_kwargs = {
    'name': 'unhidden',
    'version': '0.1.0',
    'description': '',
    'long_description': 'Hello!',
    'author': 'Burak Akkaya',
    'author_email': 'akkaya.burak@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
