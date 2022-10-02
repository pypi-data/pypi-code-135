# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.0,<0.86.0', 'mypy>=0.981,<0.982']

setup_kwargs = {
    'name': 'adworld-render-worker',
    'version': '0.1.0',
    'description': 'The render worker for the adworld pipeline',
    'long_description': '# Coming soon...',
    'author': 'Ezra Goss',
    'author_email': 'ezragoss@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
