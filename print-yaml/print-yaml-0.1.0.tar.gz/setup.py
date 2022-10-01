# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['print_yaml']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['print_yaml = print_yaml.main:run']}

setup_kwargs = {
    'name': 'print-yaml',
    'version': '0.1.0',
    'description': '',
    'long_description': '# print-yaml\n\nprint-yaml is a CLI tool that prints yaml files according to the desired depth.\n\n## Installation\n\n```\n# using pip\n$ pip install print_yaml\n\n# using poetry\n$ poetry add print_yaml\n```\n\n## Usage\n\nLet\'s say you have the following yaml file.\n\n```yaml\n# data.yaml\n\na:\n  b: 1\n  c:\n    - one\n    - two\n    - three:\n        A: 6\n        B: 7\n    - four:\n        - 8\n        - 9\n  d:\n    e: 3\n    f: 4\ng: 5\n```\n\n### Basic\n\nThe following values can be obtained using `print_yaml`\n\n```bash\n$ print_yaml tests/data.yaml -d 1\n\na: \ng: \n```\n\n\n```bash\n$ print_yaml tests/data.yaml -d 2\n\na:\n  b: \n  c: \n  d: \ng: 5\n```\n\n```bash\n$ print_yaml tests/data.yaml -d 3\n\na:\n  b: 1\n  c:\n  - one\n  - two\n  - three: \n  - four: \n  d:\n    e: \n    f: \ng: 5\n```\n\n### With value\n\nBy default, only the "key" in the yaml file is output.  \nIf you add the \'--value\' or \'-v\' option, it also outputs a single value.\n\n```bash\n$ print_yaml tests/data.yaml -d 1 -v\n\na: \ng: 5\n```\n\n```bash\n$ print_yaml tests/data.yaml -d 2 -v\na:\n  b: 1\n  c: \n  d: \ng: 5\n```\n\n```bash\n$ print_yaml tests/data.yaml -d 3 -v\na:\n  b: 1\n  c:\n  - one\n  - two\n  - three: \n  - four: \n  d:\n    e: 3\n    f: 4\ng: 5\n```\n\n### All Commands\n\n```bash\n$ print_yaml --help\n                                                                                                             \n Usage: print_yaml [OPTIONS] FILE_PATH                                                                       \n                                                                                                             \n╭─ Arguments ───────────────────────────────────────────────────────────────────────────────────────────────╮\n│ *    file_path      TEXT  [default: None] [required]                                                      │\n╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────╮\n│                       -d      INTEGER RANGE [x>=0]  [default: 0]                                          │\n│ --value               -v                                                                                  │\n│ --install-completion                                Install completion for the current shell.             │\n│ --show-completion                                   Show completion for the current shell, to copy it or  │\n│                                                     customize the installation.                           │\n│ --help                                              Show this message and exit.                           │\n╰───────────────────────────────────────────────────────────────────────────────────────────────────────────╯\n```\n',
    'author': 'heumsi',
    'author_email': 'heumsi@naver.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
