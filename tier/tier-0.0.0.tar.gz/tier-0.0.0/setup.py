# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tier']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tier',
    'version': '0.0.0',
    'description': 'Python Versioning CLI',
    'long_description': '# tier\nPython Versioning CLI\n',
    'author': 'Josh Wycuff',
    'author_email': 'Joshua.Wycuff@turner.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
