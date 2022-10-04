# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['troncos',
 'troncos.frameworks',
 'troncos.frameworks.django',
 'troncos.frameworks.gunicorn',
 'troncos.frameworks.requests',
 'troncos.frameworks.starlette',
 'troncos.logs',
 'troncos.traces']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=1.0,<2.0',
 'opentelemetry-exporter-otlp-proto-grpc>=1.12.0,<2.0.0',
 'opentelemetry-propagator-b3>=1.12.0,<2.0.0',
 'opentelemetry-propagator-jaeger>=1.12.0,<2.0.0']

setup_kwargs = {
    'name': 'troncos',
    'version': '0.0.14',
    'description': 'Observability tools and boilerplate for use in Oda python apps',
    'long_description': 'None',
    'author': 'Karl Fredrik Haugland',
    'author_email': 'karlfredrik.haugland@oda.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
