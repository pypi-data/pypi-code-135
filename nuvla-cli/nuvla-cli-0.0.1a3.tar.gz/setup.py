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
    'version': '0.0.1a3',
    'description': 'CLI tool for local management of Nuvla and NuvlaEdges via terminal',
    'long_description': "# Nuvla Command-Line interface client\nNuvla CLI client. Allows to control some Nuvla functionalities from a terminal. It \ncurrently supports the creation of Edges and Fleets, as well as  geolocation.\n\n---\n### First steps\nTo use this library it is required to have an account in https://nuvla.io. If you don't have one, go to [Nuvla](https://nuvla.io/ui/sign-up) and start with the User Interface.\n\nOnce the account is created, you will need to create an API Key credential in Nuvla/UI credentials sections. Due to security reasons, the CLI does not support user/password authentications.\n\n### 1. Install Nuvla CLI\n\nThe package can be installed directly from PyPi repository for convenience. \n```shell\n$ pip install nuvla-cli\n```\n\nOr download the pre-compiled packages from [here](https://pypi.org/project/nuvla-cli/#files)\n\n#### Requirements\n * All the dependencies are installed with pip.\n * Python >= 3.8\n\n\n### 2. Create credentials in Nuvla\nAs mentioned before, to use the CLI it is required to have API credentials in Nuvla.io.\n\nTo create them:\n 1. Go to [credentials](https://nuvla.io/ui/credentials) tab. \n 2. Click on add in the top left corner.\n 3. Select Nuvla API-Key and provide the name and description that suits better for your needs.\n 4. Copy the key-secret as this is the only time it will be provided. If lost, you will need to delete this credential and create a new one.\n\n\n### 3. Login the CLI\nThe CLI provides two login possibilities: environmental variables or cli options.\n\n**ENV Variables:**\n```shell\n$ export NUVLA_API_KEY='your_api_key'\n$ export NUVLA_API_SECRET='your_secret_key'\n$ nuvla-cli login\n```\n\n**CLI Options**\n```shell\n$ nuvla-cli login --key 'your_api_key' --secret 'your_secret_key'\n```\n\n---\nThe session is persistent and stored in the user's path under ~/.nuvla/. To remove the session just logout using the CLI.\n\nFor further details, the whole help depiction on the CLI can be found [here](help_documentation.md) \n",
    'author': 'Nacho',
    'author_email': 'nacho@sixsq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nuvla/cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
