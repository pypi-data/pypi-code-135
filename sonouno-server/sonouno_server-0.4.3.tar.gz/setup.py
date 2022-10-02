# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sonouno_server',
 'sonouno_server.models',
 'sonouno_server.routes',
 'sonouno_server.util']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.1,<10.0.0',
 'apischema>=0.17.5,<0.18.0',
 'bcrypt>=3.2.0,<4.0.0',
 'beanie>=1.8.12,<2.0.0',
 'fastapi-jwt-auth>=0.5.0,<0.6.0',
 'fastapi>=0.72.0,<0.73.0',
 'minio>=7.1.8,<8.0.0',
 'networkx>=2.8,<3.0',
 'pydantic[email]>=1.9.0,<2.0.0',
 'python-decouple>=3.6,<4.0',
 'scipy>=1.8.0,<2.0.0',
 'sonounolib>=0.5.1,<0.6.0',
 'streamunolib>=0.4,<0.5',
 'uvicorn>=0.17.0,<0.18.0']

setup_kwargs = {
    'name': 'sonouno-server',
    'version': '0.4.3',
    'description': 'A scientific data sonification platform.',
    'long_description': 'None',
    'author': 'Pierre Chanial',
    'author_email': 'pierre.chanial@apc.in2p3.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
