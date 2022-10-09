# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lacuscore']

package_data = \
{'': ['*']}

install_requires = \
['defang>=0.5.3,<0.6.0',
 'playwrightcapture>=1.15.7,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'ua-parser>=0.16.1,<0.17.0']

extras_require = \
{'docs': ['Sphinx>=5.2.3,<6.0.0']}

setup_kwargs = {
    'name': 'lacuscore',
    'version': '0.4.5',
    'description': 'Core of Lacus, usable as a module',
    'long_description': '# Modulable Lacus\n\nLacus, but as a simple module.\n\n# Installation\n\n```bash\npip install lacuscore\n```\n\n# Design\n\n`LacusCore` is the part taking care of enqueuing and capturing URLs or web enabled documents.\nIt can be used as a module in your own project, see below for the usage\n\n[Lacus](https://github.com/ail-project/lacus) is the webservice that uses `LacusCore`,\nand you can use [Pylacus](https://github.com/ail-project/pylacus) to query it.\n\nThe `enqueue`, `get_capture_status`, and `get_capture` methods if `LacusCore` and `PyLacus` have\nthe same parameters which means you can easily use them interchangeably in your project.\n\n\n# Usage\n\nThe recommended way to use this module is as follows:\n\n1. Enqueue what you want to capture with `enqueue` (it returns a UUID)\n2. Trigger the capture itself. For that, you have two options\n\n  * The `capture` method directly, if you pass it the UUID you got from `enqueue`.\n    This is what you want to use to do the capture in the same process as the one enqueuing the capture\n\n  * If you rather want to enqueue the captures in one part of your code and trigger the captures in an other one,\n    use `consume_queue` which will pick a capture from the queue and trigger the capture.\n    I this case, you should use `get_capture_status` to check if the capture is over before the last step.\n\n3. Get the capture result with `get_capture` with the UUID from you got from `enqueue`.\n',
    'author': 'Raphaël Vinot',
    'author_email': 'raphael.vinot@circl.lu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
