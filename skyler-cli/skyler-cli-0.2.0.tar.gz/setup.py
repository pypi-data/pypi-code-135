# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['skyler_cli', 'skyler_cli.cli', 'skyler_cli.core', 'skyler_cli.core.bootstrap']

package_data = \
{'': ['*'], 'skyler_cli.core.bootstrap': ['system_template/*']}

install_requires = \
['chevron==0.14.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['sc = skyler_cli.cli.main:app']}

setup_kwargs = {
    'name': 'skyler-cli',
    'version': '0.2.0',
    'description': "Skyler's toolbox of handy CLI utils",
    'long_description': "# Skyler's CLI\n[![Test](https://github.com/bouldersky/skylers-cli/actions/workflows/test.yml/badge.svg)](https://github.com/bouldersky/skylers-cli/actions/workflows/test.yml)\n\nThis is a modular CLI tool box that I tailor to my needs over time. It includes:\n\n- Nothing! Just this readme for now\n",
    'author': 'bouldersky',
    'author_email': 'skyarnold1@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
