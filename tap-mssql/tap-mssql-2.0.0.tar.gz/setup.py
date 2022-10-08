# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tap_mssql', 'tap_mssql.sync_strategies']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=16.3.0',
 'backoff>=1.8.0',
 'pendulum>=1.2.0',
 'pymssql>=2.2.1',
 'singer-python==5.9.0']

entry_points = \
{'console_scripts': ['tap-mssql = tap_mssql.__init__:main']}

setup_kwargs = {
    'name': 'tap-mssql',
    'version': '2.0.0',
    'description': 'A pipelinewise compatible tap for connecting Microsoft SQL Server',
    'long_description': 'None',
    'author': 'Rob Winters',
    'author_email': 'wintersrd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
