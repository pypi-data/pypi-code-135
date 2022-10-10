# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['epimodels', 'epimodels.continuous', 'epimodels.discrete', 'epimodels.tools']

package_data = \
{'': ['*']}

install_requires = \
['cython==0.29.32',
 'matplotlib>=3.6.1,<4.0.0',
 'mypy==0.982',
 'numpy>=1.23.3,<2.0.0',
 'pyitlib',
 'scipy>=1.9.2,<2.0.0',
 'sphinx',
 'sympy>=1.11.1,<2.0.0']

setup_kwargs = {
    'name': 'epimodels',
    'version': '0.4.0',
    'description': 'Library of mathematical epidemic models for use in simulation studies and inference',
    'long_description': None,
    'author': 'Flávio Codeço Coelho',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fccoelho/epimodels',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
