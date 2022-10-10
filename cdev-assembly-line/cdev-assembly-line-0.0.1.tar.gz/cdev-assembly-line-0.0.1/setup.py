# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assembly_line']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cdev-assembly-line',
    'version': '0.0.1',
    'description': 'Tool for generating Pypi ready Python Projects',
    'long_description': '## Pre-steps\n1. Get pyenv going and install multiple python versions (.python-version) file\n\n\n## Steps\n1. Install your Poetry environment `poetry install`\n2. Add the test repo for Pypi `poetry config repositories.testpypi https://test.pypi.org/legacy/`\n3. Add your test key for the Test Pypi repo `poetry config http-basic.testpypi __token__ pypi-your-api-token-here`\n4. Add your production ket for Pypi repo `poetry config pypi-token.pypi pypi-your-token-here`\n\n\n\n### Dev\n1. Open a Poetry shell\n    - `poetry shell`\n\n### Builds\n4. Test your build `poetry build`\n5. Publish the package\n    - test -> `poetry publish -r testpypi`\n    - prod -> `poetry publish`',
    'author': 'Daniel Sanchez',
    'author_email': '15sanchd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
