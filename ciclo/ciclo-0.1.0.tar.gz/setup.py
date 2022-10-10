# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['ciclo']
install_requires = \
['flax>=0.6.1', 'jax>=0.3.21', 'jaxlib>=0.3.20', 'pkbar>=0.5', 'tqdm>=4.64.1']

setup_kwargs = {
    'name': 'ciclo',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Cristian Garcia',
    'author_email': 'cgarcia.e88@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
