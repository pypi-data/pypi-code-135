# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ti_extras']

package_data = \
{'': ['*'], 'ti_extras': ['static/*', 'static/html/*']}

setup_kwargs = {
    'name': 'ti-extras',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
