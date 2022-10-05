# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigma', 'sigma.backends.matano']

package_data = \
{'': ['*'], 'sigma': ['pipelines/*']}

install_requires = \
['black>=22.8.0,<23.0.0', 'pysigma>=0.8.1,<0.9.0']

setup_kwargs = {
    'name': 'pysigma-backend-matano',
    'version': '0.0.1',
    'description': 'Matano backend for pySigma. Convert Sigma rules into Matano detections.',
    'long_description': 'None',
    'author': 'Samrose Ahmed',
    'author_email': 'samrose@matano.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/matanolabs/pySigma-backend-matano',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
