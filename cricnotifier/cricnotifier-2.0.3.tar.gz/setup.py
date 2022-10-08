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
    'version': '2.0.3',
    'description': 'A cli application for real time cricket match notifications.',
    'long_description': '# cricNotifier [![GitHub release (latest by date)](https://img.shields.io/github/v/release/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/releases) [![GitHub](https://img.shields.io/github/license/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/commits/main) [![GitHub issues](https://img.shields.io/github/issues/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/issues) [![Build Status](https://img.shields.io/travis/zweack/cricNotifier?style=flat-square)](https://travis-ci.org/zweack/cricNotifier)\n\nA CLI based application for real time cricket score updates. \n\n\n## Features\n- Rich command line interface\n- Choose among multiple live matches\n- Cross platform notifications, works on Windows and Linux systems\n\n\n## Installation \n\nMake sure you have python > 3.5 and pip installed, you can install it from [here](https://www.python.org/downloads/ "here")\n\nFor Linux systems, if you want to enable notifications, install dependencies for dbus-python as per specifications from your distro, e.g. for Ubuntu based distros, install following:\n```\nsudo apt-get -y install libglib2.0-dev libdbus-1-3 libdbus-1-dev\n```\n### Install using pip\n```\npip install cricNotifier\n```\n\n## Running the Application \n\nRun following command on your terminal\n```\ncricNotifier [argument]\n```\nArguments:\n```\ncommentary        Fetch commentary for last few overs.\ninfo              Fetch info for a match.\nlist              List all available matches.\nscore             Fetch latest score for a match.\nselect            Select a match with an ID.\n````\n\n## Examples\n### Get list of currently available matches\n\n![image](https://user-images.githubusercontent.com/15276039/194712651-3bcb3358-53b2-445c-8b3f-e59e072611b4.png)\n\n### Select a match using ID\n\n![image](https://user-images.githubusercontent.com/15276039/194712851-5c77d88a-ac4d-48d6-9d7e-07940074cb26.png)\n\n### Get info about selected match\n\n![image](https://user-images.githubusercontent.com/15276039/194713000-6c258b95-f044-42a4-9934-6b044e4b1cbf.png)\n\nAlternatively you can pass an ID which will override the preserved ID using select (for current command only).\n\n![image](https://user-images.githubusercontent.com/15276039/194713095-e7b9aebd-d65f-4a71-9e6e-6b44ddde8dfb.png)\n\n### Get squads for the match\n\n![image](https://user-images.githubusercontent.com/15276039/194713131-393c6651-d3e6-46e7-9fac-9c60ea70bcbf.png)\n\n### Get latest score\n\n![image](https://user-images.githubusercontent.com/15276039/194713334-3894e4b1-e64c-45e0-82f3-540cde082e59.png)\n\n### Get text commentary of the match\n\n![image](https://user-images.githubusercontent.com/15276039/194713428-1ac34fc1-1334-4662-82ea-91fb2b1bd04d.png)\n\n\n## Contributing\nThis project welcomes contributions and suggestions. Please feel free to create a PR, report an issue or put up a feature request.\n\n### Build cricNotifier locally\n#### Clone the Repository\n```\ngit clone https://github.com/zweack/cricNotifier.git && cd cricNotifier\n```\n#### Install Dependencies\nInstall [poetry](https://python-poetry.org/docs/#installation) for dependency management and run\n```\npoetry install\n```\nAlternatively, you can use pip \n```\npip install -r requirements.txt\n```\nYou are ready to roll!\n\n## License\ncricNotifier is licensed under the [MIT License](https://github.com/zweack/cricNotifier/blob/dev/LICENSE).\n',
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
