# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flooss', 'flooss.aggregation', 'flooss.plot', 'flooss.report']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=2.4.3,<3.0.0', 'openpyxl>=3.0.10,<4.0.0', 'pandas==1.3.5']

setup_kwargs = {
    'name': 'flooss',
    'version': '0.1.2',
    'description': 'A Python package to track personal expenses and build meaningful reports.',
    'long_description': '# flooss\nA Python package to track personal expenses and build meaningful reports.\n',
    'author': 'Taha GHAZOUANI',
    'author_email': 'ghazouani.taha@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
