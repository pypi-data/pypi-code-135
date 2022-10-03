# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['telegram']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'pytele',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Simplest telegram bot\nThe simplest telegram bot out there that could be embedded into your apps as a notification service\nand could listen and execute remote commands.\n\n# Installation\n```\npip install pytele\n```\n\n# Introduction\nThe simplest telegram bot out there that could be embedded into your apps as a notification service and can listen and execute remote commands.\n\n```\nfrom telegram import Bot\n\nbot = Bot() # takens the BOT's token from environment variables - TELEGRAM_BOT_TOKEN\nbot.send_msg(to='chait_id', msg='your message')\n```\nThe bot could listen and execute remote commands. In order to get started, please create a .yaml file\nwith the following structure:\n\n```\n# commands.yaml\n\ncommands:\n  1:\n    name: Git status\n    description: Get status of git from current directory\n    command: /gitstatus\n    action: git status\n  2:\n    name: Linux list\n    description: List all file under current directory\n    command: /ls\n    action: ls\n```\n\nThe action field should be exactly the same as the command executed on the CLI, e.g.\n\n```\naction: ls - will list current directory\naction: ls /etc - will list all files under /etc\n```\n\nOnce created, register the commands via register_commands(...) method and start listening.\nThe specified interval, instructs the bot at what intervals to poll messages from telegram servers.\nDefaults to 3 but could be overwritten.\n\n```\nbot.register_commands('example_commands.yaml')\nbot.listen(interval=5)\n```",
    'author': 'Jordan Raychev',
    'author_email': 'jpraychev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
