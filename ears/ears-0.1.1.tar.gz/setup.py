# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ears', 'ears.providers']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.2.2,<3.0.0',
 'google-cloud-pubsub>=2.13.7,<3.0.0',
 'httpx>=0.23.0,<0.24.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'ears',
    'version': '0.1.1',
    'description': '',
    'long_description': 'None',
    'author': 'Félix Voituret',
    'author_email': 'fvoituret@deezer.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
