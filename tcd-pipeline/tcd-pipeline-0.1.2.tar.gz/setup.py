# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tcd_pipeline', 'tcd_pipeline.commands', 'tcd_pipeline.config']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['tcd-pipeline = tcd_pipeline.main:cli']}

setup_kwargs = {
    'name': 'tcd-pipeline',
    'version': '0.1.2',
    'description': '',
    'long_description': '# TCD pipeline tool\n',
    'author': 'chitchai',
    'author_email': 'chitchaic@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
