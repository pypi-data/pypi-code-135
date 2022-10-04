# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['backbone',
 'backbone.asyncio',
 'backbone.cli',
 'backbone.common',
 'backbone.common.cord',
 'backbone.common.models',
 'backbone.common.protocol',
 'backbone.sync']

package_data = \
{'': ['*']}

install_requires = \
['PyNaCl>=1.4.0,<2.0.0',
 'halo>=0.0.31,<0.0.32',
 'httpx>=0.21.1,<0.22.0',
 'typer>=0.4.0,<0.5.0',
 'zxcvbn>=4.4.28,<5.0.0']

entry_points = \
{'console_scripts': ['backbone = backbone:main']}

setup_kwargs = {
    'name': 'backbone',
    'version': '0.6.0',
    'description': 'Tools for development with Backbone',
    'long_description': '# Backbone\n\n[![PyPI Version](https://img.shields.io/pypi/v/backbone.svg)](https://pypi.python.org/pypi/backbone/)\n\n[Backbone](https://backbone.dev) is a framework for building end-to-end encrypted applications.\n\nWith Backbone, you and your users can share sensitive data securely and build tamper-proof infrastructure. Preserve user privacy, reduce compliance requirements and protect yourself from sophisticated cyber attacks. \n\n#### Basic Usage\n\n```python\n# Import the synchronous backbone module\nfrom backbone import sync as backbone\n\n# Login to your user account\nwith backbone.from_master_secret(user_name="dumbledore", master_secret="the-deathly-hallows") as client:\n    # Operate within the hogwarts workspace\n    workspace = client.with_workspace("hogwarts")\n    \n    # Create a spells namespace and store an end-to-end-encrypted incantation\n    workspace.namespace.create("spells")\n    workspace.entry.set("spells/disarm", "expelliarmus")\n```\n\n#### Documentation\nOur [developer documentation](https://backbone.dev/docs) is the best resource to get started quickly. From our motivation behind the project, architecture overview to instructions on how to build and collaborate with Backbone.\n\n#### Community\nBackbone has a [Discord community](https://discord.gg/36M4yb6XSG) to provide support, discuss features and build together. Join us to help make Backbone better for everyone.\n\n#### License\n\nThe Backbone Python SDK and Backbone Python CLI are developed and distributed under the BSL 1.1 license with a transition to the Apache 2.0 license planned on October 5th 2026.\n',
    'author': 'Backbone Founders',
    'author_email': 'root@backbone.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://backbone.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
