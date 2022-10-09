# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['butter_backup']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pydantic>=1.9.1,<2.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['butter-backup = butter_backup.cli:cli']}

setup_kwargs = {
    'name': 'butter-backup',
    'version': '3.1.0',
    'description': 'Vollverschlüsselte, pseudoinkrementelle Sicherungskopien leicht gemacht',
    'long_description': 'None',
    'author': 'Max Görner',
    'author_email': 'max@familie-goerner.eu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
