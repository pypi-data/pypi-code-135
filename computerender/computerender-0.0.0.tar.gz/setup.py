# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['computerender']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0', 'aiodns>=3.0.0', 'aiohttp>=3.8.3,<4.0']

setup_kwargs = {
    'name': 'computerender',
    'version': '0.0.0',
    'description': 'Computerender',
    'long_description': "# Computerender\n\n[![PyPI](https://img.shields.io/pypi/v/computerender.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/computerender.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/computerender)][pypi status]\n[![License](https://img.shields.io/pypi/l/computerender)][license]\n\n[![Read the documentation at https://computerender.readthedocs.io/](https://img.shields.io/readthedocs/computerender/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/john-parton/computerender/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/john-parton/computerender/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/computerender/\n[read the docs]: https://computerender.readthedocs.io/\n[tests]: https://github.com/john-parton/computerender/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/john-parton/computerender\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _Computerender_ via [pip] from [PyPI]:\n\n```console\n$ pip install computerender\n```\n\n## Usage\n\nPlease see the [Command-line Reference] for details.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\nthis python binding for _Computerender_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/john-parton/computerender-py/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/john-parton/computerender-py/blob/main/LICENSE\n[contributor guide]: https://github.com/john-parton/computerender-py/blob/main/CONTRIBUTING.md\n[command-line reference]: https://computerender.readthedocs.io/en/latest/usage.html\n",
    'author': 'John Parton',
    'author_email': 'john.parton.iv@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/john-parton/computerender',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
