# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coucou', 'coucou.routing', 'coucou.routing.tsp']

package_data = \
{'': ['*']}

install_requires = \
['ruff>=0.0.57,<0.0.58']

setup_kwargs = {
    'name': 'coucou',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Mehdi Zouitine',
    'author_email': 'mehdizouitinegm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
