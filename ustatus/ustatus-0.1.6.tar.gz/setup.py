# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ustatus', 'ustatus.graphics', 'ustatus.modules', 'ustatus.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.0,<4.0.0',
 'dbus-next>=0.2.3,<0.3.0',
 'gbulb>=0.6.2,<0.7.0',
 'jsonschema>=4.4.0,<5.0.0',
 'psutil==5.8.0',
 'pulsectl-asyncio>=0.2.0,<0.3.0',
 'python-reactive-ui>=0.1.0,<0.2.0',
 'tomli>=1.2.2,<2.0.0']

entry_points = \
{'console_scripts': ['ustatus = ustatus.main:main',
                     'ustatus_docgen = ustatus.docgen:generate_docs']}

setup_kwargs = {
    'name': 'ustatus',
    'version': '0.1.6',
    'description': 'GTK-based status window for wayland shells.',
    'long_description': 'None',
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
