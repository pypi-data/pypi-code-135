# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wizwad']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'more-itertools>=8.14.0,<9.0.0']

entry_points = \
{'console_scripts': ['wizwad = wizwad.__main__:main']}

setup_kwargs = {
    'name': 'wizwad',
    'version': '0.3.0',
    'description': '',
    'long_description': '# wizwad\nA fast extractor and packer for wizard101/pirate101 wad files\n\n## cli usage\n```shell\n# extract a wad\n$ wizwad extract path/to/Wad.wad directory/to/extract/to/\n# list the files in a wad\n$ wizwad list path/to/Wad.wad\n# pack a directory into a wad\n$ wizwad pack path/to/Wad.wad directory/to/pack\n```\n\n## library usage\n```python\nimport wizwad\n\nwad = wizwad.Wad("path/to/Wad.wad")\n\nsome_file = wad.read("name/of/file")\nprint(some_file)\n```\n',
    'author': 'StarrFox',
    'author_email': 'starrfox6312@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/StarrFox/wizwad',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
