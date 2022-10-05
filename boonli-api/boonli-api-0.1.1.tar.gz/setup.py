# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boonli_api']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'icalendar>=4.1.0,<5.0.0',
 'lxml>=4.9.1,<5.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests-toolbelt>=0.9.1,<0.10.0',
 'requests>=2.28.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.3.0,<4.4.0']}

setup_kwargs = {
    'name': 'boonli-api',
    'version': '0.1.1',
    'description': 'API allowing you to fecth menus from boonli.com',
    'long_description': '# Boonli API\n\n[![Build Status](https://app.travis-ci.com/beaufour/boonli_api.svg?branch=main)](https://app.travis-ci.com/beaufour/boonli_api) [![Coverage Status](https://coveralls.io/repos/github/beaufour/boonli_api/badge.svg?branch=main)](https://coveralls.io/github/beaufour/boonli_api?branch=main) [![PyPI version](https://badge.fury.io/py/boonli_api.svg)](https://badge.fury.io/py/boonli_api)\n\nThis API allows you to retrieve the menus that were chosen on [Boonli](https://boonli.com).\n\n## Usage\n\nTo get the menu information run:\n\n    > boonli_api/api.py -c <customer_id> -u <username> -p <password>\n\nWhere `customer_id` is the first part of the domain name where you login, like `my_school` in `https://myschool.boonli.com`.\n\nTo enable a lot of debug logging you can add `-v`.\n\n## Web API\n\nI have also created an API that can be deployed on Google Cloud Function that returns the menus as an iCalendar here: <https://github.com/beaufour/boonli_calendar>\n\n## Notes\n\nBoonli does not have an official API, so I reverse engineered it. It involves parsing two web pages which is always fragile. So it will probably break at some point.\n',
    'author': 'Allan Beaufour',
    'author_email': 'allan@beaufour.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/beaufour/boonli_api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
