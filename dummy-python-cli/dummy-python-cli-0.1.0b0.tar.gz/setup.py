# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dummy-python-cli']

package_data = \
{'': ['*']}

install_requires = \
['click==8.1.3']

entry_points = \
{'console_scripts': ['dummy-cli = entry:main']}

setup_kwargs = {
    'name': 'dummy-python-cli',
    'version': '0.1.0b0',
    'description': '',
    'long_description': '# python-cli-pypi-publishing\n\nAdapted from https://levelup.gitconnected.com/how-to-publish-a-python-command-line-application-to-pypi-5b97a6d586f1\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
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
