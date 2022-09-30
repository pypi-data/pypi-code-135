# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_http']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0', 'nornir>=3,<4']

setup_kwargs = {
    'name': 'nornir-http',
    'version': '0.1.2',
    'description': 'http plugins for nornir',
    'long_description': '# nornir_http\n\nCollection of simple plugins for [nornir](github.com/nornir-automation/nornir/)\n\n\n## Install\n\n```bash\npip install nornir_http\n```\n\n## Tasks\n\n- `http_method` - Simple task for sending http requests.\n\n\n## Examples\n\nExamples can be found in the file [`demo.py`](demo.py)',
    'author': 'ubaumann',
    'author_email': 'github@m.ubaumann.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/InfrastructureAsCode-ch/nornir_http',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
