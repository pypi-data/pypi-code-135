# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['pgbelt', 'pgbelt.cmd', 'pgbelt.config', 'pgbelt.util']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.8,<22.2',
 'asyncpg>=0.26.0,<0.27.0',
 'pydantic>=1.10.1,<1.11.0',
 'tabulate>=0.8.9,<0.9.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['belt = pgbelt.main:app']}

setup_kwargs = {
    'name': 'pgbelt',
    'version': '0.1.2',
    'description': 'A CLI tool used to manage Postgres data migrations from beginning to end, for a single database or a fleet, leveraging pglogical replication.',
    'long_description': '# Pgbelt\n\n<p align="center">\n    <img src="https://github.com/Autodesk/pgbelt/blob/main/pgbelt.png?raw=true" width="400">\n</p>\n\n<p align="center">\n    <a href="https://github.com/autodesk/pgbelt" target="_blank">\n        <img src="https://img.shields.io/github/last-commit/autodesk/pgbelt" alt="Latest Commit">\n    </a>\n    <img src="https://github.com/Autodesk/pgbelt/actions/workflows/ci.yml/badge.svg">\n    <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank">\n        <img src="https://img.shields.io/github/license/Autodesk/pgbelt">\n    </a>\n</p>\n\nPgBelt is a CLI tool used to manage Postgres data migrations from beginning to end,\nfor a single database or a fleet, leveraging pglogical replication.\n\nIt was built to assist in migrating data between postgres databases with as\nlittle application downtime as possible. It works in databases running different versions\nof postgres and makes it easy to run many migrations in parallel during a single downtime.\n\n| :exclamation: This is very important                                                                                                            |\n| :---------------------------------------------------------------------------------------------------------------------------------------------- |\n| As with all Data Migration tasks, **there is a risk of data loss**. Please ensure you have backed up your data before attempting any migrations |\n\n## Installation\n\n### Install From PyPi\n\nIt is recommended to install pgbelt inside a virtual environment:\n\n- [pyenv](https://github.com/pyenv/pyenv)\n- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)\n\nYou must also have:\n\n- Postgres Client Tools (pg_dump, pg_restore). Mac: `brew install libpq`. Ubuntu: `sudo apt-get install postgresql-client`\n\nInstall pgbelt locally:\n\n    pip3 install pgbelt\n\n## Quickstart with Pgbelt\n\nSee [this doc](docs/quickstart.md)!\n\n## Contributing\n\nWe welcome contributions! See [this doc](CONTRIBUTING.md) on how to do so, including setting up your local development environment.\n',
    'author': 'Varjitt Jeeva',
    'author_email': 'varjitt.jeeva@autodesk.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
