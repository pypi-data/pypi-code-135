# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slackette']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'slackette',
    'version': '0.2.5',
    'description': 'Small toolkit to build Slack applications',
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
