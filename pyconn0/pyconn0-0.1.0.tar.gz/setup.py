# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyconn0',
 'pyconn0.client',
 'pyconn0.client.db',
 'pyconn0.client.lake',
 'pyconn0.enum',
 'pyconn0.errors',
 'pyconn0.model',
 'pyconn0.ops',
 'pyconn0.ops.io',
 'pyconn0.ops.sync',
 'pyconn0.utils']

package_data = \
{'': ['*']}

install_requires = \
['Humre>=0.2.0,<0.3.0',
 'addict>=2.4.0,<3.0.0',
 'bson>=0.5.10,<0.6.0',
 'orjson>=3.8.0,<4.0.0',
 'pampy>=0.3.0,<0.4.0',
 'pendulum>=2.1.2,<3.0.0',
 'psycopg[binary]>=3.1.2,<4.0.0',
 'pydantic>=1.10.1,<2.0.0',
 'sqlglot>=5.3.1,<6.0.0',
 'sqlmodel>=0.0.8,<0.0.9',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'pyconn0',
    'version': '0.1.0',
    'description': 'python database manipulation with advanced features',
    'long_description': None,
    'author': 'Thompson',
    'author_email': '51963680+thompson0012@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
