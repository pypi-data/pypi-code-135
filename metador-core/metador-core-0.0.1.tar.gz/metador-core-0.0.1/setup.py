# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metador_core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'metador-core',
    'version': '0.0.1',
    'description': 'Core of Metador, the FAIR metadata-first research data management framework.',
    'long_description': '',
    'author': 'a.pirogov',
    'author_email': 'a.pirogov@fz-juelich.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
