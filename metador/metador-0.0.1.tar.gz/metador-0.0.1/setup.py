# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['metador']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'metador',
    'version': '0.0.1',
    'description': 'The metadata-first research data management framework.',
    'long_description': '# Metador\n\nStub, to be published by end 2022 / early 2023.\n',
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
