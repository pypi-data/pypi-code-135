# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testing_providers']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6.1,<4.0.0',
 'distmqtt>=0.35.2,<0.36.0',
 'trio-websocket>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'testing-providers',
    'version': '0.1.1a2',
    'description': 'Testing utilities for networking apps.',
    'long_description': '# Testing providers\n\nTo wrap an async function in an async provider.\nVery useful to test network interfaces or to test applications mocking outer services.\n\n## Supported providers\n\n- [x] MQTT broker (anyio)\n- [x] TCP server (anyio)\n- [x] WebSocket server (trio)\n- [ ] WebSocket server (asyncio)\n',
    'author': 'didimelli',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
