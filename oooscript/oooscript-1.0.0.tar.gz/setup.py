# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oooscript',
 'oooscript.build',
 'oooscript.cfg',
 'oooscript.cli',
 'oooscript.lib',
 'oooscript.models',
 'oooscript.models.script_cfg',
 'oooscript.res',
 'oooscript.res.docs',
 'oooscript.utils']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'scriptmerge>=1.0.0,<2.0.0']

entry_points = \
{'console_scripts': ['oooscript = oooscript.cli.main:main']}

setup_kwargs = {
    'name': 'oooscript',
    'version': '1.0.0',
    'description': 'Compiles several python scripts into a single script that can be eaisly used by LibreOffice as a macro.',
    'long_description': '# oooscript\n\n![Tests](https://github.com/Amourspirit/python_libreoffice_oooscript/actions/workflows/tests.yml/badge.svg)\n\nCompiles one or more python scripts into a single script that can easily used as a LibreOffice macro.\n\nDocumentation can be founc on [Read the Docs](https://oooscript.readthedocs.io/en/latest/)\n',
    'author': ':Barry-Thomas-Paul: Moss',
    'author_email': 'vibrationoflife@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Amourspirit/python_libreoffice_oooscript',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
