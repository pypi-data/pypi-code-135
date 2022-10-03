# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinxarg', 'test']

package_data = \
{'': ['*']}

install_requires = \
['sphinx>=1.2.0']

extras_require = \
{'markdown': ['CommonMark>=0.5.6']}

setup_kwargs = {
    'name': 'sphinx-argparse',
    'version': '0.3.2',
    'description': 'A sphinx extension that automatically documents argparse commands and options',
    'long_description': '[![Documentation Status](https://readthedocs.org/projects/sphinx-argparse/badge/?version=stable)](http://sphinx-argparse.readthedocs.org/)\n[![PyPI version](https://badge.fury.io/py/sphinx-argparse.svg)](https://badge.fury.io/py/sphinx-argparse)\n[![Install with conda](https://anaconda.org/conda-forge/sphinx-argparse/badges/installer/conda.svg)](https://github.com/conda-forge/sphinx-argparse-feedstock)\n![Conda downloads](https://anaconda.org/conda-forge/sphinx-argparse/badges/downloads.svg)\n\nsphinx-argparse\n===============\n\nA sphinx extension that automatically documents argparse commands and options.\n\nFor installation and usage details see the [documentation](http://sphinx-argparse.readthedocs.org/en/latest/). The changelog is also [found there](http://sphinx-argparse.readthedocs.org/en/latest/changelog.html).\n\nThis project used to live at [alex-rudakov/sphinx-argparse](https://github.com/alex-rudakov/sphinx-argparse/) that the original maintainer disappears so I have taken over the project under this new home.\n',
    'author': 'Ash Berlin-Taylor',
    'author_email': 'ash_github@firemirror.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ashb/sphinx-argparse',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
