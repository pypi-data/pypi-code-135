# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['picsellia', 'picsellia.sdk', 'picsellia.types']

package_data = \
{'': ['*'], 'picsellia': ['conf/*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'beartype==0.9.1',
 'orjson>=3.7.11,<4.0.0',
 'picsellia-annotations==0.3.0',
 'picsellia-connexion-services>=0.1.3,<0.2.0',
 'pydantic>=1.9.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tdqm>=0.0.1,<0.0.2']

setup_kwargs = {
    'name': 'picsellia',
    'version': '6.0.0',
    'description': 'Python SDK package for Picsellia MLOps platform',
    'long_description': 'None',
    'author': 'Pierre-Nicolas Tiffreau',
    'author_email': 'pierre-nicolas@picsellia.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0.0',
}


setup(**setup_kwargs)
