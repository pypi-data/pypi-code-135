# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deucalion', 'deucalion.strategies']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'deucalion',
    'version': '0.0.1',
    'description': 'Deucalion: Edge anomaly detection framework based on Prometheus monitoring.',
    'long_description': '# Deucalion: Edge anomaly detection framework based on Prometheus\n\n## Surviving the flood of monitoring data\n\nThis repository is a monorepo containing:\n- The Deucalion Python library\n- A boilerplate Deucalion application\n- Helm deployment charts\n- Evaluation setup',
    'author': 'Pieter Moens',
    'author_email': 'pieter.moens@ugent.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pimoens/deucalion',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
