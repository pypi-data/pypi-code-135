# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boka_mpl_templates', 'boka_mpl_templates.schemas']

package_data = \
{'': ['*'], 'boka_mpl_templates': ['resources/*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'papersize>=1.2.0,<2.0.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'boka-mpl-templates',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'mbet',
    'author_email': 'maarten.betman@boskalis.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
