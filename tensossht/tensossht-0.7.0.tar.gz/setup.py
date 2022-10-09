# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tensossht',
 'tensossht.layers',
 'tensossht.specialfunctions',
 'tensossht.transforms']

package_data = \
{'': ['*']}

install_requires = \
['mypy-extensions>=0.4.3,<0.5.0',
 'numpy>=1.22,<2.0',
 'scipy>=1.4.1,<2.0.0',
 'tensorflow>=2']

extras_require = \
{'docs': ['sphinx>=5,<6', 'groundwork-sphinx-theme>=1,<2', 'Sybil>=3,<4']}

setup_kwargs = {
    'name': 'tensossht',
    'version': '0.7.0',
    'description': 'Fast and exact spherical transform for Tensorflow',
    'long_description': None,
    'author': 'Kagenova',
    'author_email': 'support@kagenova.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tensossht.readthedocs.io/en/main/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
