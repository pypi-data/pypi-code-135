# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fox_orm', 'fox_orm.internal']

package_data = \
{'': ['*']}

install_requires = \
['databases>=0.5.3,<0.6.0']

setup_kwargs = {
    'name': 'fox-orm',
    'version': '0.3.6.1',
    'description': 'Simple databases based ORM with pythonic syntax',
    'long_description': 'None',
    'author': 'vanutp',
    'author_email': 'hello@vanutp.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
