# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vrf_context', 'vrf_context.api', 'vrf_context.migrations']

package_data = \
{'': ['*'], 'vrf_context': ['templates/vrf_context/*']}

install_requires = \
['netbox-bgp>=0.7.0,<0.8.0', 'netbox-static-routes-plugin>=0.2,<0.3']

setup_kwargs = {
    'name': 'netbox-vrf-context',
    'version': '0.1.0',
    'description': 'VRF Context plugin for Netbox',
    'long_description': "# Netbox VRF Context Plugin\n\nThis is a netbox plugin for model VRF Contexts. It has dependencies on:\n\nNetbox BGP - https://pypi.org/project/netbox-bgp/\nStatic Routes - https://github.com/jbparrish17/netbox-static-routes\n\n## Development\n\n```\ncp development/dev.env.example development/dev.env\n# Set a password for POSTGRES_PASSWORD and REDIS_PASSWORD\n# \nvi development/dev.env\n\n\nvirtualenv --python=python3.10 venv\n. ./venv/usr/local/bin/activate\n# pip install -r requirements.txt   (for liniting)\n# or\n# pip install poetry invoke\ninvoke build\ninvoke debug\n```\n\n## Deployment\n\nThe plugin is available as a Python package in pypi and can be installed with pip  \n\n```\npip install netbox-vrf-context\n```\nEnable the plugin in `netbox/netbox/configuration.py` in the `PLUGINS` parameter (which is a list):\n```\nPLUGINS = [\n    'netbox_bgp',\n    'netbox_static_routes',\n    'netbox-vrf-context'\n]\n```\nSave the file and restart the Netbox service.\n",
    'author': 'The Hut Group',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
