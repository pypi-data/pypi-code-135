# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['displate']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

setup_kwargs = {
    'name': 'displate',
    'version': '0.1.0',
    'description': 'a boilterplate coder writter command line utility for discord.py',
    'long_description': '# displate\nThis is a boilerplate writer command line utility for discord.py\n----------\n# commands\n## options\nFollowing are the options for displate\n* --file\nname of the file to write in\n* --type\ntype of boilerplate you want to write\nfor example: main and cogs\n\n## commands\n* displate --file main --type main\n* displate --file cog --type cogs\n\n### If you think this library is helpful Kindly join my discord server\n[click here](https://discord.gg/c88TAWqYes)',
    'author': 'NaviTheCoderboi',
    'author_email': 'navindersingh568@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
