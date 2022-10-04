# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyltk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyltk',
    'version': '0.0.2',
    'description': 'english tokenizer and stemmer',
    'long_description': '## pyltk\n\nperformant english tokenizer and stemmer',
    'author': 'wayfaring-stranger',
    'author_email': 'zw6p226m@duck.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
