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
    'version': '0.0.1a2',
    'description': 'CLI tool for local management of Nuvla and NuvlaEdges via terminal',
    'long_description': '# `nuvla-cli`\n# Nuvla Command-Line interface client\nNuvla CLI client. Allows to control some Nuvla functionalities from a terminal. It \ncurrently supports the creation of Edges and Fleets, as well as  geolocation.\n\nLogin is only supported via API keys. \n\nInstall library \n```shell\n$ pip install nuvla-cli\n```\n\n**Usage**:\n\n```console\n$ nuvla-cli [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `clear`: Clears all the Edges instances for the user...\n* `edge`: Edge management commands\n* `fleet`: Fleet management commands\n* `login`: Login to Nuvla.\n* `logout`: Removes the local Nuvla persistent session...\n* `user`: User management commands\n\n## `nuvla-cli clear`\n\nClears all the Edges instances for the user created by the CLI\n\n:return: None\n\n**Usage**:\n\n```console\n$ nuvla-cli clear [OPTIONS]\n```\n\n**Options**:\n\n* `--force / --no-force`: Force skip clear confirmation [Not recommended  [required]\n* `--help`: Show this message and exit.\n\n## `nuvla-cli edge`\n\nEdge management commands\n\n**Usage**:\n\n```console\n$ nuvla-cli edge [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Creates a new NuvlaEdge\n* `delete`: Removes a NuvlaEdge from Nuvla\n* `geolocate`: Generates a random coordinate within the...\n* `list`: Lists the CLI created edges in the logged-in...\n* `start`: Starts a NuvlaEdge engine in the device...\n* `stop`: Stops a local NuvlaEdge with the Nuvla ID\n\n### `nuvla-cli edge create`\n\nCreates a new NuvlaEdge\n\n**Usage**:\n\n```console\n$ nuvla-cli edge create [OPTIONS]\n```\n\n**Options**:\n\n* `--name TEXT`: Edges name to be created  [default: ]\n* `--description TEXT`: Edge descriptions  [default: ]\n* `--dummy / --no-dummy`: Create a dummy Edge  [default: False]\n* `--fleet-name TEXT`: Attach created Edge to existent fleet  [default: ]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli edge delete`\n\nRemoves a NuvlaEdge from Nuvla\n\n**Usage**:\n\n```console\n$ nuvla-cli edge delete [OPTIONS]\n```\n\n**Options**:\n\n* `--nuvla-id TEXT`: Unique Nuvla ID of the NuvlaEdgeidentifier  [default: ]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli edge geolocate`\n\nGenerates a random coordinate within the provided country and locates the provided\nNuvlaEdge on those coordinates\n\n**Usage**:\n\n```console\n$ nuvla-cli edge geolocate [OPTIONS]\n```\n\n**Options**:\n\n* `--nuvla-id TEXT`: Unique Nuvla ID of the NuvlaEdge identifier  [required]\n* `--country TEXT`: Country to generate a randomcoordinates within  [required]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli edge list`\n\nLists the CLI created edges in the logged-in user\n\n**Usage**:\n\n```console\n$ nuvla-cli edge list [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `nuvla-cli edge start`\n\nStarts a NuvlaEdge engine in the device running this CLI.\n\nIf the NuvlaEdge entity is created as dummy, it will perform the activation and\ncommissioning process\n\n**Usage**:\n\n```console\n$ nuvla-cli edge start [OPTIONS]\n```\n\n**Options**:\n\n* `--nuvla-id TEXT`: Unique Nuvla ID of the NuvlaEdge identifier  [default: ]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli edge stop`\n\nStops a local NuvlaEdge with the Nuvla ID\n\n**Usage**:\n\n```console\n$ nuvla-cli edge stop [OPTIONS]\n```\n\n**Options**:\n\n* `--nuvla-id TEXT`: Unique Nuvla ID of the NuvlaEdge identifier  [default: ]\n* `--help`: Show this message and exit.\n\n## `nuvla-cli fleet`\n\nFleet management commands\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Creates a new Fleet of Edges in Nuvla\n* `geolocate`: Randomly locates the given fleet within a...\n* `list`: Retrieves and prints the list of fleet names...\n* `remove`: Removes a Fleet of Nuvlaedge provided the...\n* `start`: Starts a Fleet in the device running this...\n\n### `nuvla-cli fleet create`\n\nCreates a new Fleet of Edges in Nuvla\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet create [OPTIONS]\n```\n\n**Options**:\n\n* `--name TEXT`: Fleet name desired. Must be unique, as it works as identifier  [required]\n* `--count INTEGER`: # of Edges to create within the fleet  [default: 10]\n* `--dummy / --no-dummy`: Create a fleet of dummy edges  [default: False]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli fleet geolocate`\n\nRandomly locates the given fleet within a country\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet geolocate [OPTIONS]\n```\n\n**Options**:\n\n* `--name TEXT`: Fleet name to be geolocated  [required]\n* `--country TEXT`:  Country within to locate the fleet  [required]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli fleet list`\n\nRetrieves and prints the list of fleet names created by CLI\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet list [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `nuvla-cli fleet remove`\n\nRemoves a Fleet of Nuvlaedge provided the unique fleet name\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet remove [OPTIONS]\n```\n\n**Options**:\n\n* `--name TEXT`: Fleet unique name  [required]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli fleet start`\n\nStarts a Fleet in the device running this CLI. Only for dummy fleets\n\nIf the fleet entity is created as dummy, it will perform the activation and\ncommissioning process\n\n**Usage**:\n\n```console\n$ nuvla-cli fleet start [OPTIONS]\n```\n\n**Options**:\n\n* `--fleet-name TEXT`: Fleet name to be started  [required]\n* `--help`: Show this message and exit.\n\n## `nuvla-cli login`\n\nLogin to Nuvla. The login is persistent and only with API keys. To create the Key pair\ngo to Nuvla/Credentials sections and add a new Nuvla API credential.\n\nLogin is possible via 3 ways: Environmental variables (NUVLA_API_KEY and\nNUVLA_API_SECRET), arguments (key and secret) or via toml configuration file\n\n**Usage**:\n\n```console\n$ nuvla-cli login [OPTIONS]\n```\n\n**Options**:\n\n* `--key TEXT`: Nuvla API key  [default: ]\n* `--secret TEXT`: Nuvla API Secret  [default: ]\n* `--config-file TEXT`: Optional configuration file path where the keys are stored.  [default: ]\n* `--help`: Show this message and exit.\n\n## `nuvla-cli logout`\n\nRemoves the local Nuvla persistent session and stops any open connection\n\n**Usage**:\n\n```console\n$ nuvla-cli logout [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `nuvla-cli user`\n\nUser management commands\n\n**Usage**:\n\n```console\n$ nuvla-cli user [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `login`: Login to Nuvla.\n* `logout`: Removes the local Nuvla persistent session...\n\n### `nuvla-cli user login`\n\nLogin to Nuvla. The login is persistent and only with API keys. To create the Key pair\ngo to Nuvla/Credentials sections and add a new Nuvla API credential.\n\nLogin is possible via 3 ways: Environmental variables (NUVLA_API_KEY and\nNUVLA_API_SECRET), arguments (key and secret) or via toml configuration file\n\n**Usage**:\n\n```console\n$ nuvla-cli user login [OPTIONS]\n```\n\n**Options**:\n\n* `--key TEXT`: Nuvla API key  [default: ]\n* `--secret TEXT`: Nuvla API Secret  [default: ]\n* `--config-file TEXT`: Optional configuration file path where the keys are stored.  [default: ]\n* `--help`: Show this message and exit.\n\n### `nuvla-cli user logout`\n\nRemoves the local Nuvla persistent session and stops any open connection\n\n**Usage**:\n\n```console\n$ nuvla-cli user logout [OPTIONS]\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n',
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
