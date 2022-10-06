# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qrwifi']

package_data = \
{'': ['*']}

install_requires = \
['qrcode>=7.3.1,<8.0.0']

entry_points = \
{'console_scripts': ['qrwifi = qrwifi.__main__:main']}

setup_kwargs = {
    'name': 'qrwifi',
    'version': '0.1.1',
    'description': '',
    'long_description': '# qrwifi\n\nDisplay a QR code for your wifi in the terminal.\n\nCurrently only supports macOS. Create an issue if you want me to support your OS.\n\n## Installation\n\n```\npip install qrwifi\n```\n\n## Usage\n\n```\nqrwifi\n```',
    'author': 'Louis Abraham',
    'author_email': 'louis.abraham@yahoo.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
