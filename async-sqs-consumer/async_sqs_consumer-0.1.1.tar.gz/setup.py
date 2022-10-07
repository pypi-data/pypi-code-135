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
    'version': '0.1.1',
    'description': '',
    'long_description': '# Async SQS consumer\n\nThis is a simple asynchronous worker for consuming messages from AWS SQS\n\n### Usage\n```python\nfrom async_sqs_consumer.worker import (\n    Worker,\n)\n\nworker = Worker(\n    queue_url="https://sqs.us-east-1.amazonaws.com/xxxxxxx/queue_name"\n)\n\n\n@worker.task("report")\nasync def report(text: str) -> None:\n    print(text)\n\nworker.start()\n\n```\n',
    'author': 'Diego Restrepo',
    'author_email': 'drestrepo@fluidattacks.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/drestrepom/async_sqs_consumer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
