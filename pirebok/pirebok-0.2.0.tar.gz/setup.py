# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pirebok',
 'pirebok.fuzzers',
 'pirebok.fuzzers.generic',
 'pirebok.fuzzers.sql',
 'pirebok.transformers',
 'pirebok.transformers.generic',
 'pirebok.transformers.sql',
 'tests',
 'tests.fuzzers',
 'tests.transformers',
 'tests.transformers.generic',
 'tests.transformers.sql']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0.1', 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'dev': ['tox>=3.26.0,<4.0.0',
         'virtualenv>=20.16.5,<21.0.0',
         'pip>=22.2.2,<23.0.0',
         'twine>=4.0.1,<5.0.0',
         'pre-commit>=2.20.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.3.1,<2.0.0',
         'mkdocs-include-markdown-plugin>=3.8.1,<4.0.0',
         'mkdocs-material>=8.5.2,<9.0.0',
         'mkdocstrings-python>=0.7.1,<0.8.0',
         'mkdocs-autorefs>=0.4.1,<0.5.0'],
 'test': ['black>=22.8.0,<23.0.0',
          'isort>=5.10.1,<6.0.0',
          'flake8>=5.0.4,<6.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.971,<0.972',
          'pytest>=7.1.3,<8.0.0',
          'pytest-cov>=3.0.0,<4.0.0']}

entry_points = \
{'console_scripts': ['pirebok = pirebok.cli:main']}

setup_kwargs = {
    'name': 'pirebok',
    'version': '0.2.0',
    'description': 'a guided adversarial fuzzer',
    'long_description': '# pîrebok (from Kurdish "witch") - a guided adversarial fuzzer\n\n\n[![pypi](https://img.shields.io/pypi/v/pirebok.svg)](https://pypi.org/project/pirebok/)\n[![python](https://img.shields.io/pypi/pyversions/pirebok.svg)](https://pypi.org/project/pirebok/)\n[![Build Status](https://github.com/dogancanbakir/pirebok/actions/workflows/dev.yml/badge.svg)](https://github.com/dogancanbakir/pirebok/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/dogancanbakir/pirebok/branch/main/graphs/badge.svg)](https://codecov.io/github/dogancanbakir/pirebok)\n\n\n\n* Documentation: <https://dogancanbakir.github.io/pirebok>\n* GitHub: <https://github.com/dogancanbakir/pirebok>\n* PyPI: <https://pypi.org/project/pirebok/>\n* Free software: MIT\n\n\n## Features\n- Random generic fuzzer w/ multiple transformers\n- Random sql fuzzer w/ multiple transformers\n- Guided random sql fuzzer w/ multiple transformers and [metamaska](https://github.com/dogancanbakir/metamaska)\n\n## Credits\n- [Cookiecutter](https://github.com/audreyr/cookiecutter)\n- [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage)\n- [ML-based-WAF](https://github.com/vladan-stojnic/ML-based-WAF)\n- [WAF-A-MoLE](https://github.com/AvalZ/WAF-A-MoLE)\n',
    'author': 'Doğan Can Bakır',
    'author_email': 'dogancanbakir@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dogancanbakir/pirebok',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
