# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secure_json']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'secure-json',
    'version': '1.0.1',
    'description': 'Secure settings in json',
    'long_description': "\n## Description\n\nSecure settings in json file\n\n# install\n```\n  pip install secure-json\n```\n\n#### import\n\n```python\nfrom secure_json import Settings\n```\n\n#### Description\n```text\nThe library allows you to encrypt your settings stored in json format.\nIt is possible to convert from a simple storage option to an encrypted one. \nTo work with the encrypted version of the settings, you need to pass the startup parameter - the password with which the encryption took place.\nTry it, the library is very simple.\n```\n\n\n#### Usage\n# Import lib\n```python\n  settings = Settings('Settings.json').data\n```\n\n#### Encoding\\Decoding\n\n```http\nencoding settings:\n    python main.py <password> encode\n\t\ndecoding settings:\n\tpython main.py <password> decode\n\nhelp:\n\tpython main.py help\n```\n",
    'author': 'to101',
    'author_email': 'to101kv@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.1,<4.0',
}


setup(**setup_kwargs)
