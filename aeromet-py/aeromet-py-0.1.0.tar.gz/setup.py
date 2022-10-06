# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aeromet_py',
 'aeromet_py.database',
 'aeromet_py.reports',
 'aeromet_py.reports.models',
 'aeromet_py.reports.models.base',
 'aeromet_py.reports.models.metar',
 'aeromet_py.reports.models.taf',
 'aeromet_py.utils']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'aeromet-py',
    'version': '0.1.0',
    'description': 'Python library to parse meteorological information of aeronautical stations.',
    'long_description': 'None',
    'author': 'diego-garro',
    'author_email': 'diego.garromolina@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
