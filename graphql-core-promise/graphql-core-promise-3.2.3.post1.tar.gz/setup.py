# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphql_core_promise', 'graphql_core_promise.execute']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'graphql-core-promise',
    'version': '3.2.3.post1',
    'description': 'Add support for promise-based dataloaders and resolvers to graphql-core v3+',
    'long_description': '# Graphql core promise\nAdd support for promise-based dataloaders and resolvers to graphql-core v3+',
    'author': 'Shen Li',
    'author_email': 'dustet@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
