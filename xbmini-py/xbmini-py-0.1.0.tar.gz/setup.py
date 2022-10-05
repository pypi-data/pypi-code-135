# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xbmini']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5,<2.0']

setup_kwargs = {
    'name': 'xbmini-py',
    'version': '0.1.0',
    'description': 'Python Toolkit for the GCDC HAM',
    'long_description': '# xbmini-py\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sco1/xbmini-py/main.svg)](https://results.pre-commit.ci/latest/github/sco1/xbmini-py/main)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)\n[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-VSCode.dev-blue)](https://vscode.dev/github.com/sco1/xbmini-py)\n\nPython Toolkit for the GCDC HAM.\n',
    'author': 'sco1',
    'author_email': 'sco1.git@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sco1/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
