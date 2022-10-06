# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['src', 'src.starknet_interface_generator', 'starknet_interface_generator']

package_data = \
{'': ['*']}

install_requires = \
['cairo-lang>=0.10.0,<0.11.0', 'click==8.1.3', 'toml==0.10.2']

entry_points = \
{'console_scripts': ['starknet-interface-generator = src.cli:main']}

setup_kwargs = {
    'name': 'starknet-interface-generator',
    'version': '0.1.5',
    'description': 'Generate interfaces for your Starknet contracts',
    'long_description': "# Starknet interface generator\n\nGenerate / check the interfaces corresponding to your Starknet contracts.\n\n## Installation\n\n`pip install starknet-interface-generator`\n\n## Usage\n\nOptions :\n\n### Generate interfaces\n\n```\nUsage: starknet-interface-generator generate [OPTIONS]\n\nOptions:\n  --files TEXT          File paths\n  -p, --protostar       Uses `protostar.toml` to get file paths\n  -d, --directory TEXT  Output directory for the interfaces. If unspecified,\n                        they will be created in the same directory as the\n                        contracts\n  --help                Show this message and exit.\n```\n\n### Check existing interfaces\n\n```\nstarknet-interface-generator check [OPTIONS]\n\nOptions:\n  --files TEXT          Contracts to check\n  -p, --protostar       Uses `protostar.toml` to get file paths\n  -d, --directory TEXT  Directory of the interfaces to check. Interfaces must\n                        be named `i_<contract_name>.cairo`\n  --help                Show this message and exit.\n```\n\n## Example\n\nGenerate interfaces for the contracts in `contracts/` and put them in `interfaces/`:\n\n```\nfind contracts/ -iname '*.cairo' -exec starknet-interface-generator generate --files {} \\;\n```\n\nCheck the interface for `test/main.cairo` against the interface `i_main.cairo` in interfaces/:\n\n```\nstarknet-interface-generator check --files test/main.cairo -d interfaces\n```\n\n## Protostar\n\nYou can use starknet-interface-generator in a protostar project.\nThis can be paired with a github action to automatically generate the interfaces for the contracts\nthat specified inside the `protostar.toml` file.\n\n`starknet-interface-generator [generate||check] --protostar`\n",
    'author': 'msaug',
    'author_email': 'msaug@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
