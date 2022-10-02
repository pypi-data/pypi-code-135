# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepcoil', 'deepcoil.utils']

package_data = \
{'': ['*'], 'deepcoil': ['models/*', 'weights/*']}

install_requires = \
['allennlp==0.9.0',
 'biopython==1.79',
 'overrides==3.1.0',
 'pandas==1.3.0',
 'seaborn>=0.12.0,<0.13.0',
 'tensorflow>=2.3,<3.0']

entry_points = \
{'console_scripts': ['deepcoil = deepcoil.run_deepcoil:main']}

setup_kwargs = {
    'name': 'deepcoil',
    'version': '2.0.2',
    'description': 'Fast and accurate prediction of coiled coil domains in protein sequences',
    'long_description': None,
    'author': 'Jan Ludwiczak',
    'author_email': 'j.ludwiczak@cent.uw.edu.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '<3.9',
}


setup(**setup_kwargs)
