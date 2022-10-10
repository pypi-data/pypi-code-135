# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_lit_urls']

package_data = \
{'': ['*'], 'django_lit_urls': ['templates/*']}

install_requires = \
['Django>3.1', 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'django-lit-urls',
    'version': '0.1.3',
    'description': 'Django URLS delivered as string literal functions in Javascript',
    'long_description': 'None',
    'author': 'Josh Brooks',
    'author_email': 'josh@catalpa.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
