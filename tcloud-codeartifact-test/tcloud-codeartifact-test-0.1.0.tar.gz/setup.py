# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['artifacts', 'artifacts.awsutils']

package_data = \
{'': ['*']}

install_requires = \
['Faker==8.4.0']

setup_kwargs = {
    'name': 'tcloud-codeartifact-test',
    'version': '0.1.0',
    'description': 'Code artifact of tcloud',
    'long_description': '# tcloud-codeartifact\nGerenciador de layers dos projetos tcloud .\n',
    'author': 'pyaoponto',
    'author_email': 'pyaoponto@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
