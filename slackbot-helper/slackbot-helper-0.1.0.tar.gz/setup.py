# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slackbot_helper']

package_data = \
{'': ['*']}

install_requires = \
['baseblock', 'slack-bolt>=1.14.3,<2.0.0', 'slackclient>=2.9.4,<3.0.0']

setup_kwargs = {
    'name': 'slackbot-helper',
    'version': '0.1.0',
    'description': 'Helper Functions for Slackbots',
    'long_description': '# Climate Bot (climate-bot)\n\napp level token:\nxapp-1-A04676B21CY-4187437745827-e204f6d0772de37aae27bbb48e5e63af317f83555c3f38818138a2d6340d0072\n\nuser oauth\nxoxp-4180854157238-4211164773392-4172960334695-5198b5b5b86d5ae9247067fe3eb15b2d\n\nbot user oauth\nxoxb-4180854157238-4187434730291-YtgCYbziFGJURokANQgwT5Xs',
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': 'Craig Trim',
    'maintainer_email': 'craigtrim@gmail.com',
    'url': 'https://github.com/craigtrim/slackbot-helper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
