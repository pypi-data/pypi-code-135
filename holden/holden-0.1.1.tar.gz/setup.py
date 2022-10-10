# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['holden']

package_data = \
{'': ['*']}

install_requires = \
['amos>=0.1.7,<0.2.0', 'miller>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'holden',
    'version': '0.1.1',
    'description': 'lightweight, accessible, flexible composite data structures',
    'long_description': "[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Documentation Status](https://readthedocs.org/projects/holden/badge/?version=latest)](http://holden.readthedocs.io/?badge=latest)\n\n[It is all connected](https://media.giphy.com/media/3ornjRyce6SukW8INi/giphy.gif)\n\nThe goal of holden is provide a lightweight, turnkey, extensible composite data structures.\n\nholden's framework supports a wide range of coding styles. You can create complex multiple inheritance structures wit mixins galore or simpler, compositional objects. Even though the data structures are necessarily object-oriented, all of the tools to modify them are also available as functions, for those who prefer a more funcitonal approaching to programming.\n\nThe project is also highly documented so that users and developers and make holden work with their projects. It is designed for Python coders at all levels. Beginners should be able to follow the readable code and internal documentation to understand how it works. More advanced users should find complex and tricky problems addressed through efficient code.\n",
    'author': 'Corey Rayburn Yung',
    'author_email': 'coreyrayburnyung@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/WithPrecedent/holden',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
