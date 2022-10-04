# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balconyapp', 'balconyapp.iamhelper']

package_data = \
{'': ['*']}

install_requires = \
['balcony>=0.0.4,<0.0.5']

setup_kwargs = {
    'name': 'balconyapp',
    'version': '0.0.15',
    'description': 'Balcony App template package',
    'long_description': '# balcony-app-template\nA template repository for creating new Balcony Apps.\n',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
