# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['whitesmith']

package_data = \
{'': ['*'], 'whitesmith': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'blacksmith>=1.0.2,<2.0.0',
 'pydantic-factories>=1.9.0,<2.0.0']

entry_points = \
{'console_scripts': ['whitesmith = whitesmith.entrypoint:main']}

setup_kwargs = {
    'name': 'whitesmith',
    'version': '0.1.0',
    'description': 'A ',
    'long_description': 'Whitesmith\n==========\n\nTest helper for blacksmith resources.\n\n\nMotivation\n----------\n\nWhile using blacksmith, resources are declared using pydantic, and, while testing,\nwe never do http calls.\n\nWhitesmith is a helper that create pytest fixtures for blacksmith resources and\ngenerate handlers for tests.\n\n\nUsage\n-----\n\n::\n\n  whitesmith generate -m my_package.resources --out-dir tests/\n\n\nThe commande above will generate a folder ``tests/whitesmith`` containing\nhandlers for all the api call with a default implementation.\n\n\n.. note::\n    | If you run the command again, the command does not overrite generated files.\n    | To generate newer version, use the ``--overwrite`` flag.\n\n\nThe command will generate also a `conftest.py` file containing two fixtures,\n\nfor sync and async version.\n\n\nTests that require those fixture are suppose to be created inside the whitesmith folder.\n\nTo create the test elsewhere, you have to copy create your own fixtures by copy,\npasting and adapting import path.\n',
    'author': 'Guillaume Gauvrit',
    'author_email': 'guillaume@gauvr.it',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
