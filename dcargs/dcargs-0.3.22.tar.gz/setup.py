# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dcargs', 'dcargs._shtab', 'dcargs.conf', 'dcargs.extras']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'docstring-parser>=0.14.1,<0.15.0',
 'frozendict>=2.3.4,<3.0.0',
 'rich>=11.1.0',
 'typing-extensions>=4.3.0,<5.0.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['backports.cached-property>=1.0.2,<2.0.0'],
 ':sys_platform == "win32"': ['colorama>=0.4.0,<0.5.0']}

setup_kwargs = {
    'name': 'dcargs',
    'version': '0.3.22',
    'description': 'Deprecated! Install tyro instead',
    'long_description': '*dcargs* is now [*tyro*](https://pypi.org/project/tyro).\n',
    'author': 'brentyi',
    'author_email': 'brentyi@berkeley.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/brentyi/dcargs',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
