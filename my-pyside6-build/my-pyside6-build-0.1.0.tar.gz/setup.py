# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dummy']

package_data = \
{'': ['*']}

install_requires = \
['pyside6 @ PySide6-6.3.1-6.3.1-cp310-cp310-linux_x86_64.whl',
 'shiboken6 @ shiboken6-6.3.1-6.3.1-cp310-cp310-linux_x86_64.whl',
 'shiboken6_generator @ '
 'shiboken6_generator-6.3.1-6.3.1-cp310-cp310-linux_x86_64.whl']

setup_kwargs = {
    'name': 'my-pyside6-build',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Nir',
    'author_email': '88795475+nrbnlulu@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
