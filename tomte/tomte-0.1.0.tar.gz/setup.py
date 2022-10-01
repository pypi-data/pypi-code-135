# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tomte']

package_data = \
{'': ['*']}

install_requires = \
['bandit==1.7.0',
 'black==21.6b0',
 'darglint==1.8.0',
 'flake8-bugbear==21.9.1',
 'flake8-docstrings==1.6.0',
 'flake8-eradicate==1.1.0',
 'flake8-isort==4.0.0',
 'flake8==3.9.2',
 'isort==5.9.3',
 'mypy==0.910',
 'pylint==2.11.1',
 'safety==1.10.3',
 'tox==3.24.4',
 'vulture==2.3']

extras_require = \
{'docs': ['mkdocs==1.3.0',
          'mkdocs-material==7.1.10',
          'mkdocs-macros-plugin==0.7.0',
          'pydoc-markdown==4.3.2',
          'pydocstyle==6.1.1',
          'pymdown-extensions==8.2'],
 'tests': ['pytest==7.0.0',
           'pytest-asyncio==0.18.0',
           'pytest-cov==3.0.0',
           'pytest-randomly==3.11.0',
           'pytest-rerunfailures==10.0']}

setup_kwargs = {
    'name': 'tomte',
    'version': '0.1.0',
    'description': 'A library that wraps many useful tools (linters, analysers, etc) to keep Python code clean, secure, well-documented and optimised.',
    'long_description': None,
    'author': 'David Minarsch',
    'author_email': 'david.minarsch@googlemail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
