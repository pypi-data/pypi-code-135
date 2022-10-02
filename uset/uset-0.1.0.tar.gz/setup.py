# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uset']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'uset',
    'version': '0.1.0',
    'description': '',
    'long_description': "# Universal Settings Library\n\nFind out of this name is available, I have the code almost ready to go.\nDon't want to do a bunch of work for a name that I can't use so seeing if this name is ok to use\nwith pypi.\n",
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
