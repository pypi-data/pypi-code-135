# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['purepress']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=1.1.2,<1.2.0',
 'Markdown>=3.2.2,<3.3.0',
 'MarkupSafe>=2.0.1,<2.1.0',
 'PyYAML>=5.4.1,<5.5.0',
 'Werkzeug>=1.0.1,<1.1.0',
 'click>=7.1.2,<7.2.0',
 'colorama>=0.4.3,<0.5.0',
 'importlib-metadata<5.0',
 'py-gfm>=1.0.0,<1.1.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['purepress = purepress.__main__:cli.main']}

setup_kwargs = {
    'name': 'purepress-arts',
    'version': '0.5.0',
    'description': 'PurePress for Arts.',
    'long_description': '# PurePress Arts\n\n[![PyPI](https://img.shields.io/pypi/v/purepress-arts.svg)](https://pypi.org/project/purepress-arts/)\n![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)\n\n**PurePress Arts** is a variant of [PurePress](https://github.com/verilab/purepress), specialized for displaying artworks.\n\nCases:\n\n- [Amanda Ninji Arts](https://www.amandaninjiarts.com)\n',
    'author': 'Richard Chien',
    'author_email': 'stdrc@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/richardchien/purepress-arts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<3.11',
}


setup(**setup_kwargs)
