# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djhubspot']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<5.0']

setup_kwargs = {
    'name': 'dj-hubspot',
    'version': '0.1.1',
    'description': 'Project template for Django app, using Poetry.',
    'long_description': "# dj-hubspot - Django + HubSpot Made Easy\n\n[![CI tests](https://github.com/pfouque/dj-hubspot/actions/workflows/ci.yml/badge.svg)](https://github.com/pfouque/dj-hubspot/actions/workflows/ci.yml)\n[![Package Downloads](https://img.shields.io/pypi/dm/dj-hubspot)](https://pypi.org/project/dj-hubspot/)\n[![Documentation](https://img.shields.io/static/v1?label=Docs&message=READ&color=informational&style=plastic)](https://dj-hubspot.github.io/dj-hubspot/)\n[![MIT License](https://img.shields.io/static/v1?label=License&message=MIT&color=informational&style=plastic)](https://github.com/sponsors/dj-hubspot)\n\nHubSpot Models for Django.\n\n## Introduction\n\ndj-hubspot implements all of the HubSpot models, for Django. Set up your\nwebhook endpoint and start receiving model updates. You will then have\na copy of all the HubSpot models available in Django models, as soon as\nthey are updated!\n\n## Features\n\n-   TODO\n\n## Requirements\n\n-   Django >=3.2\n-   Python >=3.8\n-   PostgreSQL engine (recommended) >=9.6\n-   MySQL engine: MariaDB >=10.2 or MySQL >=5.7\n-   SQLite: Not recommended in production. Version >=3.26 required.\n\n## Contribute\n\nDjango app template, using `poetry-python` as dependency manager.\n\nThis project is a template that can be cloned and re-used for\nredistributable apps.\n\nIt includes the following:\n\n* `poetry` for dependency management\n* `isort`, `black`, `pyupgrade` and `flake8` linting\n* `pre-commit` to run linting\n* `mypy` for type checking\n* `tox` and Github Actions for builds and CI\n\nThere are default config files for the linting and mypy.\n\n### Principles\n\nThe motivation for this project is to provide a consistent set of\nstandards across all YunoJuno public Python/Django projects. The\nprinciples we want to encourage are:\n\n* Simple for developers to get up-and-running\n* Consistent style (`black`, `isort`, `flake8`)\n* Future-proof (`pyupgrade`)\n* Full type hinting (`mypy`)\n\n### Versioning\n\nWe currently support Python 3.7+, and Django 3.2+. We will aggressively\nupgrade Django versions, and we won't introduce hacks to support\nbreaking changes - if Django 4 introduces something that 2.2 doesn't\nsupport we'll drop it.\n\n### Coding style\n\nWe use [pre-commit](https://pre-commit.com/) to run code quality tools.\n[Install pre-commit](https://pre-commit.com/#install) however you like (e.g. `pip install pre-commit` with your system python) then set up pre-commit to run every time you commit with:\n\n```bash\n> pre-commit install\n```\n\nYou can then run all tools:\n\n```bash\n> pre-commit run --all-files\n```\n\nFor more info, see the docs, or the code quality chapters in *Boost Your Django DX*.\n\n### Tests\n\n##### Tests package\n\nThe package tests themselves are _outside_ of the main library code, in\na package that is itself a Django app (it contains `models`, `settings`,\nand any other artifacts required to run the tests (e.g. `urls`).) Where\nappropriate, this test app may be runnable as a Django project - so that\ndevelopers can spin up the test app and see what admin screens look\nlike, test migrations, etc.\n\n##### Running tests\n\nThe tests themselves use `pytest` as the test runner. If you have\ninstalled the `poetry` evironment, you can run them thus:\n\n```\n$ poetry run pytest\n```\n\nor\n\n```\n$ poetry shell\n(djhubspot) $ pytest\n```\n\nThe full suite is controlled by `tox`, which contains a set of\nenvironments that will format, lint, and test against all\nsupport Python + Django version combinations.\n\n```\n$ tox\n...\n______________________ summary __________________________\n  fmt: commands succeeded\n  lint: commands succeeded\n  mypy: commands succeeded\n  py37-django22: commands succeeded\n  py37-django32: commands succeeded\n  py37-djangomain: commands succeeded\n  py38-django22: commands succeeded\n  py38-django32: commands succeeded\n  py38-djangomain: commands succeeded\n  py39-django22: commands succeeded\n  py39-django32: commands succeeded\n  py39-djangomain: commands succeeded\n```\n\n##### CI\n\nThere is a `.github/workflows/tox.yml` file that can be used as a\nbaseline to run all of the tests on Github. This file runs the oldest\n(2.2), newest (3.2), and head of the main Django branch.\n",
    'author': 'Pascal Fouque',
    'author_email': 'code@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/pfouque/dj-hubspot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
