# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mitre_attack',
 'mitre_attack.api',
 'mitre_attack.cli',
 'mitre_attack.data',
 'mitre_attack.data.types']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.28,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'coverage[toml]>=6.1.1,<7.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'setuptools>=58.5.3,<59.0.0',
 'stix2>=3.0.1,<4.0.0',
 'taxii2-client>=2.3.0,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['mitre-attack = mitre_attack.cli:main']}

setup_kwargs = {
    'name': 'mitre-attack',
    'version': '1.0.1',
    'description': '',
    'long_description': None,
    'author': 'Tyler Fisher',
    'author_email': 'tylerfisher@tylerfisher.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
