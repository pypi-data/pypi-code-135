# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['drcomp']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.2', 'scikit-learn>=1.1.2']

setup_kwargs = {
    'name': 'drcomp',
    'version': '0.0.1a0',
    'description': 'Dimensionality Reduction Comparison',
    'long_description': "# Dimensionality Reduction Comparison (drcomp)\n\n[![PyPI](https://img.shields.io/pypi/v/drcomp.svg)][pypi_]\n[![Status](https://img.shields.io/pypi/status/drcomp.svg)][status]\n[![Python Version](https://img.shields.io/pypi/pyversions/drcomp)][python version]\n[![License](https://img.shields.io/pypi/l/drcomp)][license]\n\n[![Read the documentation at https://drcomp.readthedocs.io/](https://img.shields.io/readthedocs/drcomp/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/MoritzM00/drcomp/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/MoritzM00/drcomp/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi_]: https://pypi.org/project/drcomp/\n[status]: https://pypi.org/project/drcomp/\n[python version]: https://pypi.org/project/drcomp\n[read the docs]: https://drcomp.readthedocs.io/\n[tests]: https://github.com/MoritzM00/drcomp/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/MoritzM00/drcomp\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- TODO\n\n## Requirements\n\n- TODO\n\n## Installation\n\nYou can install _drcomp_ via [pip] from [PyPI]:\n\n```console\npip install drcomp\n```\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_drcomp_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project is based on [@cjolowicz]'s [Hypermodern Python Cookiecutter] template and\nwas modified better fit my needs and to remove some not needed features.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/MoritzM00/drcomp/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/MoritzM00/drcomp/blob/main/LICENSE\n",
    'author': 'Moritz Mistol',
    'author_email': 'moritz.mistol@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MoritzM00/drcomp',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
