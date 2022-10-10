# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pooch_cli']

package_data = \
{'': ['*']}

install_requires = \
['pooch', 'tqdm', 'typer']

entry_points = \
{'console_scripts': ['pooch = pooch_cli.main:app']}

setup_kwargs = {
    'name': 'pooch-cli',
    'version': '0.1.1',
    'description': 'Command-line interface for Pooch',
    'long_description': '# pooch-cli\n\n```\npooch dl https://pub.danilohorta.me/deciphon/PF02545.hmm\n```\n',
    'author': 'Danilo Horta',
    'author_email': 'danilo.horta@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
