# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['big_sqs']

package_data = \
{'': ['*']}

install_requires = \
['boto3==1.22.7']

setup_kwargs = {
    'name': 'big-sqs',
    'version': '1.1.0',
    'description': 'An SQS client capable of storing oversize message payloads on S3.',
    'long_description': "# BigSQS\nAn SQS client capable of storing oversize message payloads on S3.\n\n## Overview\nAWS SQS is a super useful message queue, but it's sometimes the case that we want to transmit messages larger than the 256KB limit. An official [SQS extended client library](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html) is available for Java, but not for Python. Similar libraries implementing the protocol used by the original Java library are available for Python, but this library has a few additional features:\n\n* **Fully transparent response structure** - MD5 hashes (`MD5OfBody`) and the `content-length` header are recomputed clent-side to be correct to the message *after* resolution of S3 pointers.\n* **Unopinionated configuration** - The library can use your default (environment) AWS creds (useful for deployment in Lambda functions), take your AWS creds as paremeters and even supports using 2 different credential sets for SQS and S3, even if these belong to different AWS accounts.\n* **Leaves boto3 untouched** - This library does not attempt to reconfigure/decorate boto3 with additional functionality.\n* **Fully documented** - The library is fully documented with docstrings, making for an enjoyable development experience.\n\n## Installing\nInstalling the project is very straightforward via [pip](https://pypi.org/project/pip/):\n\n```bash\npip install big-sqs\n```\n\nYou can then import the library into your project:\n\n```python\nfrom big_sqs import BigSqsClient\n```\n\n## Building\nBuilding the library is only necessary if you're doing development work on it, and is not required if you're just importing it to use in your project. To build the library, you'll need to install the Poetry dependency management system for Python. Build the project like so:\n\n```bash\npoetry build\n```\n\n## Usage\nUse the library like so:\n\n```python\nfrom big_sqs import BigSqsClient\n\n# Initialize client.\nsqs = BigSqsClient.from_default_aws_creds(\n    '<my_queue_url>',\n    '<my_s3_bucket_name>',\n    1024, # For any messages bigger than 1KiB, use S3.\n)\n\n# Create 2KiB message.\nPAYLOAD_SIZE = 2048\npayload = '0' * PAYLOAD_SIZE\n\n# Send message.\nsqs.send_message(payload)\n\n# Receive that same message.\ndequeued = sqs.receive_messages(1)\n\n# Print the message payload we got back.\nprint(dequeued)\n\n# Delete messages (S3 objects will also be cleaned up).\nfor message in recv['Messages']:\n    sqs.delete_message(message['ReceiptHandle'])\n```\n\n## Configuration\nYou can configure the library with your SQS credentials in 3 ways:\n\n### Using Default (Environment) Creds\nTo use the default AWS credentials configured for your environment (if any) you can use the `from_default_aws_creds` static factory method:\n\n```python\nfrom big_sqs import BigSqsClient\n\n# Initialize client.\nsqs = BigSqsClient.from_default_aws_creds(\n    '<my_queue_url>',\n    '<my_s3_bucket_name>',\n    1024, # For any messages bigger than 1KiB, use S3.\n)\n```\n\n### User-Specified Creds\nTo make use of user-specified AWS credentials, there's a different factory method for you to use:\n\n```python\nfrom big_sqs import BigSqsClient\n\n# Initialize client.\nsqs = BigSqsClient.from_aws_creds(\n    'us-west-2',\n    '<my_aws_access_key_id>',\n    '<my_aws_secret_access_key>',\n    '<my_queue_url>',\n    '<my_s3_bucket_name>',\n    1024, # For any messages bigger than 1KiB, use S3.\n)\n```\n\n### User-Specified Clients\nTo use a different set of credentials for SQS and S3, or to use different AWS accounts for each, you can supply boto3 clients directly to the `BigSqsClient` constructor.\n\n```python\nfrom big_sqs import BigSqsClient\n\n# Initialize client.\nsqs = BigSqsClient(\n    boto3.client(\n        'sqs',\n        region_name='us-west-2',\n        aws_access_key_id='<my_us_aws_access_key_id>',\n        aws_secret_access_key='<my_us_aws_secret_access_key>',\n    ),\n    boto3.client(\n        's3',\n        region_name='eu-west-2',\n        aws_access_key_id='<my_eu_aws_access_key_id>',\n        aws_secret_access_key='<my_eu_aws_secret_access_key>',\n    ),\n    '<my_queue_url>',\n    '<my_s3_bucket_name>',\n    1024, # For any messages bigger than 1KiB, use S3.\n)\n```\n\n## Acknowledgements\nThe authors acknowledge the contribution of the following projects to this library.\n\n* The original [SQS extended client library](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html) (for Java)\n\n## Contributors\nThe main contributors to this project so far are as follows:\n\n* Saul Johnson ([@lambdacasserole](https://github.com/lambdacasserole))\n",
    'author': 'Saul Johnson',
    'author_email': 'saul.johnson@breachlock.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/security-breachlock/big-sqs.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
