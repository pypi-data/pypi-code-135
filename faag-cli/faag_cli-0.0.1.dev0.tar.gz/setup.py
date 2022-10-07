# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['faag_cli', 'faag_cli.constants', 'faag_cli.core', 'faag_cli.utils']

package_data = \
{'': ['*'], 'faag_cli': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['faag = faag_cli.faag:typer_app']}

setup_kwargs = {
    'name': 'faag-cli',
    'version': '0.0.1.dev0',
    'description': 'Flask/FastAPI Architecture Application Generator',
    'long_description': '# Faag-CLI\n\n**FastAPI/Flask project generator with the best folder structure.** (Fast/Flask Architecture App Generator)\nFlask / FastAPI app generator with a maintainable architecture and sample codes for the best practices.\nCurrently supports generation of FastAPI apps only. Flask support is coming soon. Currently in `pre-release`. Feel free\nto raise suggesstions and issues. This package is made with [Typer](https://typer.tiangolo.com/).\n\n## Installation\n\n```bash\npoetry add faag-cli\n```\n\n```bash\npip install faag-cli\n```\n\n\n# Usage\n\n```bash\nUsage: faag [OPTIONS]\n\n Generate a new FastAPI/Flask project\n \n╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮\n│ --app                 -a       TEXT  Type of that should be generated. Default type is fast_api. Valid Options are: [fast_api, flask] [default: fast_api        |\n│ --app-name            -an      TEXT  Name of the app [default: sampel_app]                                                                                      |\n│ --install-completion                 Install completion for the current shell.                                                                                  |\n│ --show-completion                    Show completion for the current shell, to copy it or customize the installation.                                           |\n│ --help                               Show this message and exit.                                                                                                |\n╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n\n1. Help\n    ```bash\n    faag --help\n    ```\n\n2. Generate a FastAPI app\n    ```bash\n   faag\n    ```\n\n3. Generate a Fast APP with custom app name\n    ```bash\n   faag --app-name myapp\n   faag -an myapp\n    ```\n   ',
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
