# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alert_msgs']

package_data = \
{'': ['*'], 'alert_msgs': ['styles/*']}

install_requires = \
['dominate>=2.6.0,<3.0.0',
 'pdoc3>=0.10.0,<0.11.0',
 'premailer>=3.10.0,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'ready-logger>=0.1.3,<0.2.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['text_alert = alert_msgs.alerts:text_alert_cmd']}

setup_kwargs = {
    'name': 'alert-msgs',
    'version': '0.1.1',
    'description': 'Utilities for creating HTML and Markdown alert messages.',
    'long_description': None,
    'author': 'Dan Kelleher',
    'author_email': 'kelleherjdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
