# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['async_sqs_consumer', 'async_sqs_consumer.utils']

package_data = \
{'': ['*']}

install_requires = \
['aioboto3>=10.1.0,<11.0.0',
 'aiobotocore>=2.4.0,<3.0.0',
 'click>=8.1.3,<9.0.0',
 'jsonschema>=4.16.0,<5.0.0']

setup_kwargs = {
    'name': 'async-sqs-consumer',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Diego Restrepo',
    'author_email': 'drestrepo@fluidattacks.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
