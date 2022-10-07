# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eospyo']

package_data = \
{'': ['*']}

install_requires = \
['base58>=2.1.1,<3.0.0',
 'httpx>=0.22',
 'pycryptodome>=3.15.0,<4.0.0',
 'pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'eospyo',
    'version': '0.6.4',
    'description': 'Interact with EOSIO blockchain networks',
    'long_description': "# Deprecation Warning\n**eospyo** was renamed to **[pyntelope](https://pypi.org/project/pyntelope/)**  \nThis package won't be maintained anymore.  \n**pyntelope** is just a fork with the same api (for now). Please follow its instructions to migrate your code to use it.  \n",
    'author': 'Edson',
    'author_email': 'eospyo@facings.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/FACINGS/eospyo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
