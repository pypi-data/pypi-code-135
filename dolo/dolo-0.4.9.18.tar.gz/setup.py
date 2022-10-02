# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dolo',
 'dolo.algos',
 'dolo.compiler',
 'dolo.misc',
 'dolo.numeric',
 'dolo.numeric.discretization',
 'dolo.numeric.extern',
 'dolo.numeric.optimize',
 'dolo.tests']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'dolang>=0.0.18,<0.0.19',
 'interpolation>=2.2.4,<3.0.0',
 'ipython>=8.5.0,<9.0.0',
 'matplotlib>=3.6.0,<4.0.0',
 'multipledispatch>=0.6.0,<0.7.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.5.0,<2.0.0',
 'quantecon>=0.5.3,<0.6.0',
 'scipy>=1.9.1,<2.0.0',
 'xarray>=2022.6.0,<2023.0.0']

setup_kwargs = {
    'name': 'dolo',
    'version': '0.4.9.18',
    'description': 'Economic Modeling in Python',
    'long_description': 'Complete documentation with installation instruction, available at https://www.econforge.org/dolo.py.\n\nJoin the chat at https://gitter.im/EconForge/dolo\n\n[![codecov](https://codecov.io/gh/EconForge/dolo.py/branch/master/graph/badge.svg?token=hLAd1OaTRp)](https://codecov.io/gh/EconForge/dolo.py)\n\n![CI](https://github.com/EconForge/dolo.py/workflows/CI/badge.svg)\n\n![Publish docs via GitHub Pages](https://github.com/EconForge/dolo.py/workflows/Publish%20docs%20via%20GitHub%20Pages/badge.svg)\n\n[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/EconForge/dolo.git/master?urlpath=lab)\n',
    'author': 'Winant Pablo',
    'author_email': 'pablo.winant@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
