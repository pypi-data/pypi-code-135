# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basepkg']

package_data = \
{'': ['*']}

extras_require = \
{'aphp': ['datapkgaphp==0.1.0']}

setup_kwargs = {
    'name': 'basepkg',
    'version': '0.2.0',
    'description': '',
    'long_description': '',
    'author': 'Thomas PETIT-JEAN',
    'author_email': 'thomas.petitjean-ext@aphp.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
