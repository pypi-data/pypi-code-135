# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydantic_remote_config',
 'pydantic_remote_config.aws',
 'pydantic_remote_config.enum']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'pydantic-remote-config',
    'version': '0.0.1',
    'description': 'Utility to fetch configuration values from remote sources that integrates with Pydantic settings models',
    'long_description': '# pydantic-remote-config\npydantic extension to fetch configuration from various remote sources including SSM, SecretsManager, Vault, etc.\n\n## Contributing\n\n#### Installation\n\n#### Development Dependencies\n* `asdf` for managing multiple python version\n* `pre-commit` for formatting & linting code before commits\n*\n',
    'author': 'nplutt',
    'author_email': 'nplutt@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nplutt/pydantic-remote-config',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
