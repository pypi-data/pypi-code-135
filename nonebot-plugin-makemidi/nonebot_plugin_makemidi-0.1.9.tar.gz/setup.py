# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_makemidi']

package_data = \
{'': ['*'], 'nonebot_plugin_makemidi': ['resources/*']}

install_requires = \
['fluidsynth',
 'midi2audio',
 'mido',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot2>=2.0.0-beta.4,<3.0.0',
 'pydub>=0.25.1,<0.26.0']

setup_kwargs = {
    'name': 'nonebot-plugin-makemidi',
    'version': '0.1.9',
    'description': 'Easy midi maker',
    'long_description': None,
    'author': 'RandomEnch',
    'author_email': 'randomench@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
