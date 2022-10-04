# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['construct_classes']

package_data = \
{'': ['*']}

install_requires = \
['construct>=2.10,<3.0']

setup_kwargs = {
    'name': 'construct-classes',
    'version': '0.1.0',
    'description': 'Parse your binary structs into dataclasses',
    'long_description': None,
    'author': 'matejcik',
    'author_email': 'ja@matejcik.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/matejcik/construct-classes',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
