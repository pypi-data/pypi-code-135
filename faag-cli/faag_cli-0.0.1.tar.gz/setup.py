# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faag_cli', 'faag_cli.constants', 'faag_cli.core', 'faag_cli.utils']

package_data = \
{'': ['*'], 'faag_cli': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'black[d]>=22.10.0,<23.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['faag = faag_cli.faag:typer_app']}

setup_kwargs = {
    'name': 'faag-cli',
    'version': '0.0.1',
    'description': 'Flask/FastAPI Architecture Application Generator',
    'long_description': '# Faag_CLI\n**FastAPI/Flask project generator with the best folder structure.** (Fast/Flask Architecture App Generator)\n',
    'author': 'Vetrichelvan',
    'author_email': 'pythonhub.py@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pythonhubpy/FAAG',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
