# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cricnotifier']

package_data = \
{'': ['*'], 'cricnotifier': ['static/icon/*']}

install_requires = \
['PyYAML',
 'beautifulsoup4',
 'lxml',
 'plyer',
 'pytest',
 'requests',
 'rich',
 'tabulate',
 'typer[all]>=0.6.1,<0.7.0',
 'win10toast']

entry_points = \
{'console_scripts': ['cricnotifier = cricnotifier.main:app']}

setup_kwargs = {
    'name': 'cricnotifier',
    'version': '0.1.0',
    'description': 'A cli application for real time cricket match notifications.',
    'long_description': '# cricNotifier [![GitHub release (latest by date)](https://img.shields.io/github/v/release/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/releases) [![GitHub](https://img.shields.io/github/license/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/commits/main) [![GitHub issues](https://img.shields.io/github/issues/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/issues) [![Build Status](https://img.shields.io/travis/zweack/cricNotifier?style=flat-square)](https://travis-ci.org/zweack/cricNotifier)\n\nA python application for real time cricket match notifications on Windows and Linux\n\n\n## Features\n- Rich command line UI\n- Choose among multiple live matches\n- Cross platform, works on Windows and Linux systems\n\n\n## Installation \n\nMake sure you have python > 3.5 and pip installed, you can install it from [here](https://www.python.org/downloads/ "here")\n\nFor Linux systems, install dependencies for dbus-python as per specifications from your distro, e.g. for Ubuntu based distros, install following:\n```\nsudo apt-get -y install libglib2.0-dev libdbus-1-3 libdbus-1-dev\n```\n### Install using pip\n```\npip3 install cricNotifier\n```\n### Build and Install\n#### Clone the Repository\n\n```\ngit clone https://github.com/zweack/cricNotifier.git && cd cricNotifier\n```\n\n#### Install Dependencies\n```\npip install -r requirements.txt\n```\n\n## Running the Application \n\nRun following command on your terminal\n```\ncricNotifier [argument]\n```\nArguments:\n```\ncommentary        Fetch commentary for last few overs.\ninfo              Fetch info for a match.\nlist              List all available matches.\nscore             Fetch latest score for a match.\nselect            Select a match with an ID.\n````\n## Contributing\nThis project welcomes contributions and suggestions. Please feel free to create a PR, report an issue or put up a feature request.\n\n## License\ncricNotifier is licensed under the [MIT License](https://github.com/zweack/cricNotifier/blob/dev/LICENSE).',
    'author': 'Jeet Jain',
    'author_email': 'jeet88833@gmail.com',
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
