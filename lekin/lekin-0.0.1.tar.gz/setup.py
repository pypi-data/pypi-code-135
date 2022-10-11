# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lekin', 'lekin.dashboard', 'lekin.objective', 'lekin.solver', 'lekin.struct']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib', 'pandas>=1.3.0,<2.0.0', 'scipy>=1.8,<2.0']

setup_kwargs = {
    'name': 'lekin',
    'version': '0.0.1',
    'description': 'Flexible job shop scheduler in Python',
    'long_description': '[license-image]: https://img.shields.io/badge/License-Apache%202.0-blue.svg\n[license-url]: https://opensource.org/licenses/Apache-2.0\n[pypi-image]: https://badge.fury.io/py/python-lekin.svg\n[pypi-url]: https://pypi.python.org/pypi/python-lekin\n[build-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml/badge.svg?branch=master\n[build-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/test.yml?query=branch%3Amaster\n[lint-image]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml/badge.svg?branch=master\n[lint-url]: https://github.com/LongxingTan/python-lekin/actions/workflows/lint.yml?query=branch%3Amaster\n[docs-image]: https://readthedocs.org/projects/python-lekin/badge/?version=latest\n[docs-url]: https://python-lekin.readthedocs.io/en/latest/\n[coverage-image]: https://codecov.io/gh/longxingtan/python-lekin/branch/master/graph/badge.svg\n[coverage-url]: https://codecov.io/github/longxingtan/python-lekin?branch=master\n[codeql-image]: https://github.com/longxingtan/python-lekin/actions/workflows/codeql-analysis.yml/badge.svg\n[codeql-url]: https://github.com/longxingtan/python-lekin/actions/workflows/codeql-analysis.yml\n\n<h1 align="center">\n<img src="./docs/source/_static/logo.svg" width="490" align=center/>\n</h1><br>\n\n[![LICENSE][license-image]][license-url]\n[![PyPI Version][pypi-image]][pypi-url]\n[![Build Status][build-image]][build-url]\n[![Lint Status][lint-image]][lint-url]\n[![Docs Status][docs-image]][docs-url]\n[![Code Coverage][coverage-image]][coverage-url]\n[![CodeQL Status][codeql-image]][codeql-url]\n\n**[Documentation](https://python-lekin.readthedocs.io)** | **[Tutorials](https://python-lekin.readthedocs.io/en/latest/tutorials.html)** | **[Release Notes](https://python-lekin.readthedocs.io/en/latest/CHANGELOG.html)** | **[中文](https://github.com/LongxingTan/python-lekin/blob/master/README_CN.md)**\n\n**python-lekin** is a Flexible Job Shop Scheduler Library, named after and inspired by [Lekin](https://web-static.stern.nyu.edu/om/software/lekin/). As a core function in **APS (advanced planning and scheduler)**, it helps to improve factory efficiency.\n\n## Tutorial\n\n**Install**\n\n``` shell\n$ pip install python-lekin\n```\n\n**Usage**\n\n``` python\nfrom lekin import Heuristics, Genetics\nfrom lekin import Scheduler\n\nsolver = Heuristics()\nscheduler = Scheduler(solver)\nscheduler.solve(jobs, machines)\n\nscheduler.draw()\n```\n\n## Examples\n\n## Citation\n```\n@misc{python-lekin2022,\n  author = {Longxing Tan},\n  title = {python lekin},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/longxingtan/python-lekin}},\n}\n```\n',
    'author': 'Longxing Tan',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://python-lekin.readthedocs.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
