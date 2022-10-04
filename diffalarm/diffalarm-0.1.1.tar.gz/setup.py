# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diffalarm']

package_data = \
{'': ['*']}

install_requires = \
['beepy>=1.0.7,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'docopt>=0.6.2,<0.7.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['diffalarm = diffalarm:main']}

setup_kwargs = {
    'name': 'diffalarm',
    'version': '0.1.1',
    'description': 'alarms when web page has diff',
    'long_description': '# diffalarm\nalarms when a web pages has diff\n',
    'author': 'scarf',
    'author_email': 'greenscarf005@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/scarf005/diffalarm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
