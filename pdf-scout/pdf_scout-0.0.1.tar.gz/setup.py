# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdf_scout', 'pdf_scout.tests', 'pdf_scout.tests.snapshots']

package_data = \
{'': ['*']}

install_requires = \
['PyPDF2>=2.10.9,<3.0.0',
 'joblib>=1.2.0,<2.0.0',
 'pdfplumber>=0.7.4,<0.8.0',
 'rich>=12.5.1,<13.0.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['pdf_scout = pdf_scout.app:start']}

setup_kwargs = {
    'name': 'pdf-scout',
    'version': '0.0.1',
    'description': 'automatically create bookmarks in a PDF file',
    'long_description': None,
    'author': 'Huey',
    'author_email': 'hello@huey.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
