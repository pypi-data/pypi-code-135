# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dvbctrl']

package_data = \
{'': ['*']}

install_requires = \
['psutil>=5.9.1,<6.0.0']

setup_kwargs = {
    'name': 'dvbctrl',
    'version': '0.2.8',
    'description': 'Controls a local dvbstreamer',
    'long_description': '# dvbctrl\n\n## starting\n\n```python\nfrom dvbctrl.dvbstreamer import DVBStreamer\n\nadaptor = 0\ndvbs = DVBStreamer(adaptor)\nrunning = dvbs.start()\nif not running:\n    raise Exception(f"Failed to start dvbstreamer on adaptor {adaptor}")\n```\n\n## stopping\n\n```python\nfrom dvbctrl.dvbstreamer import DVBStreamer\n\nadaptor = 0\ndvbs = DVBStreamer(adaptor)\n\n...\n\nif dvbs.isRunning():\n    dvbs.stop()\n```\n',
    'author': 'ccdale',
    'author_email': 'chris.charles.allison+dvbctrl@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
