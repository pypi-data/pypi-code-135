# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['color_fish']
setup_kwargs = {
    'name': 'color-fish',
    'version': '0.1.3',
    'description': 'fish()',
    'long_description': 'None',
    'author': 'pavelsv',
    'author_email': 'p6282813@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
