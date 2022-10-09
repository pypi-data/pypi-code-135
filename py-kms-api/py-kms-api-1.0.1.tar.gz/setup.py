# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_kms_api']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-kms-api',
    'version': '1.0.1',
    'description': 'PyKMS API',
    'long_description': '# PyKMS API\n\n[`GitHub`](https://github.com/joe733/py-kms-api) | [`PyPI`](https://pypi.org/project/py-kms-api/)\n',
    'author': 'Jovial Joe Jayarson',
    'author_email': 'jovial7joe@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/joe733/py-kms-api',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
