# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['help_desk_client']

package_data = \
{'': ['*']}

install_requires = \
['zenpy>=2.0.25,<3.0.0']

setup_kwargs = {
    'name': 'help-desk-client',
    'version': '0.1.8',
    'description': 'A Python client for interfacing with helpdesk services.',
    'long_description': '# helpdesk-client\n\nA Python client for interfacing with helpdesk services.\n\n## Requirements\n\n- [poetry](https://python-poetry.org)\n\n## Setup local development\n\n1. `poetry install`\n\n## Run tests\n\n1. `make test`\n\n## Create a PyPI release (and create tag)\n\n* Merge PR into main (making sure you have bumped the version in the .toml)\n\n* Pull the main branch to your machine\n\n* `git tag [new version #]`\n\n* `git push origin --tags`\n\n* `make publish`\n',
    'author': 'Sam Dudley',
    'author_email': 'sam.dudley@digital.trade.gov.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
