# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nuvla_cli',
 'nuvla_cli.action_entity_cmd',
 'nuvla_cli.common',
 'nuvla_cli.entity_action_cmd',
 'nuvla_cli.nuvlaio',
 'nuvla_cli.nuvlaio.device',
 'nuvla_cli.schemas']

package_data = \
{'': ['*']}

install_requires = \
['Shapely>=1.8.4,<2.0.0',
 'docker>=6.0.0,<7.0.0',
 'fabric>=2.7.1,<3.0.0',
 'nuvla-api>=3.0.8,<4.0.0',
 'pydantic>=1.10.0,<2.0.0',
 'pyshp>=2.3.1,<3.0.0',
 'rich>=12.5.1,<13.0.0',
 'toml>=0.10.2,<0.11.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['nuvla-cli = nuvla_cli.__main__:app_cli']}

setup_kwargs = {
    'name': 'nuvla-cli',
    'version': '0.0.1a0',
    'description': 'CLI tool for local management of Nuvla and NuvlaEdges via terminal',
    'long_description': '# Nuvla Command-Line interface client\nNuvla CLI client. Allows to control some Nuvla functionalities from a terminal. It \ncurrently supports the creation of Edges and Fleets, as well as  geolocation.\n\nLogin is only supported via API keys. \n\nInstall library \n```shell\n$ pip install dist/nuvla_cli-0.1.0-py3-none-any.whl\n```\n\nCLI Base Commands\n```shell\n$ ./nuvla_cli --help\n\nCommands:\n clear     Clears all the Edges instances for the user created by the CLI                                                                                                                                    \n edge      Edge management commands                                                                                                                                                                          \n fleet     Fleet management commands                                                                                                                                                                         \n login     Login to Nuvla. The login is persistent and only with API keys. To create the Key pair go to Nuvla/Credentials sections and add a new Nuvla API credential.                                       \n logout    Removes the local Nuvla persistent session and stops any open connection                                                                                                                          \n user      User management commands            \n```\n',
    'author': 'Nacho',
    'author_email': 'nacho@sixsq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
