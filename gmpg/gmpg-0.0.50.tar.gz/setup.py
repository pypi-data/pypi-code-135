# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gmpg', 'gmpg._pkg', 'gmpg._pkg.licensing']

package_data = \
{'': ['*']}

install_requires = \
['clicks>=0.0.61,<0.0.62',
 'pendulum>=2.1.2,<3.0.0',
 'pydeps>=1.10.24,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest-gevent>=1.1.0,<2.0.0',
 'pytest-pep8>=1.0.6,<2.0.0',
 'pytest>=7.1.3,<8.0.0',
 'radon>=5.1.0,<6.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['gmpg = gmpg.__main__:main']}

setup_kwargs = {
    'name': 'gmpg',
    'version': '0.0.50',
    'description': 'tools for decentralized software development',
    'long_description': "Git is distributed by design. It's use has centralized through GitHub. Host\nyour own repositories on your own website and decentralize.\n\nPython is distributed by design. It's use has centralized through PyPI. Host\nyour own package index on your own website and decentralize.\n\nDesign in accordance with the meta system.\n",
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
