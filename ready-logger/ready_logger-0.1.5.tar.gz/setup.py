# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ready_logger']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.1,<6.0.0']

setup_kwargs = {
    'name': 'ready-logger',
    'version': '0.1.5',
    'description': 'Easily configure loggers.',
    'long_description': "## Easily configure loggers.\n\n### Use the default logger:\n```python\nfrom ready_logger import logger\n```\n\n### Use a custom logger:\n```python\nlogger = get_logger(\n    name='my-logger',\n    log_level='DEBUG',\n    log_dir='/home/user/my_logs'\n)\n```\nsee [get_logger]('ready_logger/configure.py#L11') for more details.\n\n### Configuration\nAll `get_logger` arguments besides for `name` can be set via environment variables in the form `READY_LOGGER_{VARIABLE NAME}`.   \n\nTo set configuration specific to a named logger,\nuse the format `{LOGGER NAME}_{VARIABLE NAME}`",
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/djkelleher/ready-logger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
