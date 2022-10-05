# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['textual',
 'textual.cli',
 'textual.cli.previews',
 'textual.css',
 'textual.devtools',
 'textual.drivers',
 'textual.layouts',
 'textual.renderables',
 'textual.widgets']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata>=4.11.3,<5.0.0',
 'nanoid>=2.0.0,<3.0.0',
 'rich>=12.6.0,<13.0.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.0.0,<5.0.0'],
 'dev': ['aiohttp>=3.8.1,<4.0.0', 'click==8.1.2', 'msgpack>=1.0.3,<2.0.0']}

entry_points = \
{'console_scripts': ['textual = textual.cli.cli:run']}

setup_kwargs = {
    'name': 'textual',
    'version': '0.2.0b1',
    'description': 'Text User Interface using Rich',
    'long_description': None,
    'author': 'Will McGugan',
    'author_email': 'willmcgugan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Textualize/textual',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
