# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['igviz']

package_data = \
{'': ['*']}

install_requires = \
['ipywidgets>=7.7.1,<8.0.0', 'networkx>=2.8.5,<3.0.0', 'plotly>=5.10.0,<6.0.0']

setup_kwargs = {
    'name': 'igviz',
    'version': '0.5.0',
    'description': 'Create interactive network graph visualizations.',
    'long_description': 'None',
    'author': 'Ashton Sidhu',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
