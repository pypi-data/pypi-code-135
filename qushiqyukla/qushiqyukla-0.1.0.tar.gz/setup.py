# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['qushiqyukla']
setup_kwargs = {
    'name': 'qushiqyukla',
    'version': '0.1.0',
    'description': "qo'shiqni yuklab oladiga modul",
    'long_description': '',
    'author': 'Xumoyun Rayimov',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
