# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tibber-influx']

package_data = \
{'': ['*']}

install_requires = \
['influxdb-client[async]>=1.32.0,<2.0.0',
 'pyTibber>=0.25.2,<0.26.0',
 'python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'tibber-influx',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Tibber-Influx extractor\n\nExtract price- and power usage data from Tibber, and store in InfluxDB. ',
    'author': 'Kristian Aurlien',
    'author_email': 'kristian@aurlien.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
