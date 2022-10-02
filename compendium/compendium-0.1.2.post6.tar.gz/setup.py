# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['compendium', 'compendium.filetypes']

package_data = \
{'': ['*']}

install_requires = \
['anytree>=2.8.0,<3.0.0',
 'dpath>=2.0.1,<3.0.0',
 'ruamel.yaml>=0.16.10,<0.17.0',
 'tomlkit>=0.7.0,<0.8.0']

extras_require = \
{'xml': ['xmltodict>=0.12.0,<0.13.0']}

setup_kwargs = {
    'name': 'compendium',
    'version': '0.1.2.post6',
    'description': 'Simple layered configuraion tool',
    'long_description': "# Compendium\n\n[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)\n[![Build Status](https://travis-ci.org/kuwv/python-compendium.svg?branch=master)](https://travis-ci.org/kuwv/python-compendium)\n[![codecov](https://codecov.io/gh/kuwv/python-compendium/branch/master/graph/badge.svg)](https://codecov.io/gh/kuwv/python-compendium)\n\n## Overview\n\nCompendium is a layered configuration management tool. It has the capability\nto manage configuration files writen in JSON, TOML, XML and YAML. Settings\nfrom these configuration files can then be managed easily with the help of\ndpath.\n\n## Documentation\n\nhttps://kuwv.github.io/python-compendium/\n\n### Install\n\n```\npip install compendium\n```\n\n### Manage a configuration file\n\n```python\n>>> import os\n>>> from compendium import ConfigFile\n\n>>> basedir = os.path.join(os.getcwd(), 'tests')\n>>> filepath = os.path.join(basedir, 'config.toml')\n\n>>> cfg = ConfigFile(filepath)\n>>> settings = cfg.load()\n\nSimple lookup for title\n>>> settings['/title']\n'TOML Example'\n\nQuery values within list\n>>> settings.values('/servers/**/ip')\n['10.0.0.1', '10.0.0.2']\n\nCheck the current server IP address\n>>> settings['/database/server']\n'192.168.1.1'\n\nUpdate the server IP address\n>>> settings['/database/server'] = '192.168.1.2'\n>>> settings['/database/server']\n'192.168.1.2'\n\nCheck the database max connections\n>>> settings['/database/connection_max']\n5000\n\nDelete the max connections\n>>> del settings['/database/connection_max']\n\nCheck that the max connections have been removed\n>>> settings.get('/database/connection_max')\n\n```\n\n### Manage multiple layered configurations\n\nThe `ConfigManager` is a layered dictionary mapping. It allows multiple\nconfigurations to be loaded from various files. Settings from each file\nis overlapped in order so that the first setting found will be used.\n\n```python\n>>> import os\n\n>>> from compendium import ConfigManager\n\nReference config files from examples\n>>> basedir = os.path.join(os.getcwd(), 'examples', 'config_manager')\n>>> config1 = os.path.join(basedir, 'config1.toml')\n>>> config2 = os.path.join(basedir, 'config2.toml')\n\nRetrieve settings from config files\n>>> cfg = ConfigManager(name='app', filepaths=[config1, config2])\n\nGet using dpath\n>>> cfg.get('/default/foo2')\n'bar2'\n\nLookup with multi-query\n>>> cfg.lookup('/example/settings/foo', '/default/foo')\n'baz'\n\n```\n\n### Manage nested configurations\n\n```python\n>>> import os\n\n>>> from anytree import RenderTree\n>>> from compendium.config_manager import ConfigManager, TreeConfigManager\n\n>>> basedir = os.path.join(os.getcwd(), 'examples', 'tree')\n\n>>> cfg = TreeConfigManager(\n...     name='fruit',\n...     basedir=basedir,\n...     filename='node.toml',\n...     load_root=True,\n...     load_children=True,\n... )\n\n>>> cfg.defaults == {}\nTrue\n\n>>> 'succulant' in cfg['/fruit/children']\nTrue\n\n>>> succulant = cfg.get_config('/fruit/succulant')\n>>> succulant.name\n'succulant'\n\n```\n\n### Manage configurations using Hierarchy File System (HFS)\n\nTBD\n<!--\n# ```python\n# import os\n#\n# from compendium.config_manager import HierarchyConfigManager\n#\n# import pytest\n#\n# Setup base paths\n# >>> base_filepath = os.path.dirname(__file__)\n# >>> global_filepath = os.path.expanduser('~')\n#\n# System paths\n# >>> fs.add_real_file(\n# ...     source_path=os.path.join(base_filepath, 'settings1.toml'),\n# ...     target_path=os.path.join(os.sep, 'etc', 'hierarchy', 'config.toml')\n# ... )\n#\n# User paths\n# >>> fs.add_real_file(\n# ...     source_path=os.path.join(base_filepath, 'settings2.toml'),\n# ...     target_path=os.path.join(global_filepath, '.hierarchy.toml')\n# ... )\n#\n# >>> fs.add_real_file(\n# ...     source_path=os.path.join(base_filepath, 'settings3.toml'),\n# ...     target_path=os.path.join(\n# ...         global_filepath, '.hierarchy.d', 'config.toml'\n# ...     )\n# ... )\n#\n# >>> cfg = HierarchyConfigManager(\n# ...     name='hierarchy',\n# ...     filename='config.toml',\n# ...     merge_strategy='overlay',\n# ...     enable_system_filepaths=True,\n# ...     enable_global_filepaths=True\n# ... )\n# >>> cfg.load_configs()\n#\n# ```\n-->\n\n### Development\n\n```\npoetry shell\npoetry install\npython -m doctest README.md\n```\n",
    'author': 'Jesse P. Johnson',
    'author_email': 'jpj6652@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kuwv/python-compendium',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
