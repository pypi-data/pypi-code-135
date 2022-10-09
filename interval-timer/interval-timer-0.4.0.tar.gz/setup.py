# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['interval_timer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'interval-timer',
    'version': '0.4.0',
    'description': '',
    'long_description': '# interval-timer\n\nAn interval timer iterator that synchronises iterations to within specific time intervals.\n\nThe time taken for code execution within each iteration will not affect the interval timing, provided that the execution time is not longer than the interval period. The caller can check if this is the case by checking the `missed` attribute on the returned `Interval` instance.\n\n## Installation\n\n    pip install interval-timer\n\n## Usage\n\n    from interval_timer import IntervalTimer\n    \n    for interval in IntervalTimer(1):\n        print(interval)\n        \n        # Do time synchronised task once per second here...\n',
    'author': 'morefigs',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/morefigs/interval-timer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
