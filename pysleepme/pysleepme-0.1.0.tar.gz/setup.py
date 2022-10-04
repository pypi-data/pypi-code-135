# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysleepme',
 'pysleepme.py_sleep_me_api',
 'pysleepme.py_sleep_me_api.api',
 'pysleepme.py_sleep_me_api.api.device_control',
 'pysleepme.py_sleep_me_api.models',
 'tests']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.3.0',
 'httpx>=0.15.4,<0.24.0',
 'python-dateutil>=2.8.0,<3.0.0',
 'respx>=0.20.0,<0.21.0']

extras_require = \
{'dev': ['tox>=3.20.1,<4.0.0',
         'virtualenv>=20.2.2,<21.0.0',
         'pip>=20.3.1,<21.0.0',
         'twine>=3.3.0,<4.0.0',
         'pre-commit>=2.12.0,<3.0.0',
         'toml>=0.10.2,<0.11.0',
         'bump2version>=1.0.1,<2.0.0'],
 'doc': ['mkdocs>=1.1.2,<2.0.0',
         'mkdocs-include-markdown-plugin>=1.0.0,<2.0.0',
         'mkdocs-material>=6.1.7,<7.0.0',
         'mkdocstrings>=0.15.2,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0'],
 'test': ['black>=21.5b2,<22.0',
          'isort>=5.8.0,<6.0.0',
          'flake8>=3.9.2,<4.0.0',
          'flake8-docstrings>=1.6.0,<2.0.0',
          'mypy>=0.900,<0.901',
          'pytest>=6.2.4,<7.0.0',
          'pytest-cov>=2.12.0,<3.0.0']}

setup_kwargs = {
    'name': 'pysleepme',
    'version': '0.1.0',
    'description': 'Python Sleep Me API Wrapper for Home Assistant Use.',
    'long_description': '# PySleepMe\n\n\n[![pypi](https://img.shields.io/pypi/v/pysleepme.svg)](https://pypi.org/project/pysleepme/)\n[![python](https://img.shields.io/pypi/pyversions/pysleepme.svg)](https://pypi.org/project/pysleepme/)\n[![Build Status](https://github.com/jeeftor/pysleepme/actions/workflows/dev.yml/badge.svg)](https://github.com/jeeftor/pysleepme/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/jeeftor/pysleepme/branch/main/graphs/badge.svg)](https://codecov.io/github/jeeftor/pysleepme)\n\n\n\nPython [Sleep Me API](https://docs.developer.sleep.me/api/) Wrapper for Home Assistant Use\n\n\n* Documentation: <https://jeeftor.github.io/pysleepme>\n* GitHub: <https://github.com/jeeftor/pysleepme>\n* PyPI: <https://pypi.org/project/pysleepme/>\n* Free software: MIT\n\n# TODO\n\n- [ ] - Have them actually ship my order\n- [x] - Code API to query devices\n- [ ] - Code API Calls for specific device\n- [ ] - Add control logic\n\n## Background\n\nThe SleepMe API documentation is available [here](https://docs.developer.sleep.me/api/). This library uses [openapi-python-client](https://www.google.com/search?client=safari&rls=en&q=openapi-python-client&ie=UTF-8&oe=UTF-8) with a slightly modified version of the API (there is an issue with one of the endpoint names) to create an OpenAPI 3.0 client.\n\nThis library then wraps those features for easier usage.\n## Quickstart\n\nFirst you must get an API Token this is done somewhere:\n',
    'author': 'Jeff Stein',
    'author_email': 'jeffstein@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jeeftor/pysleepme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
