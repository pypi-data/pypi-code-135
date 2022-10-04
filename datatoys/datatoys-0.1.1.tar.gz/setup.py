# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datatoys']

package_data = \
{'': ['*']}

install_requires = \
['lxml>=4.9.1,<5.0.0',
 'numpy>=1.23.3,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'pyreadr>=0.4.7,<0.5.0']

setup_kwargs = {
    'name': 'datatoys',
    'version': '0.1.1',
    'description': "Let's play with data! We prepared toy data for data newbies.",
    'long_description': None,
    'author': 'Dongook Son',
    'author_email': '60206749+donny-son@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>3.8,<3.11',
}


setup(**setup_kwargs)
