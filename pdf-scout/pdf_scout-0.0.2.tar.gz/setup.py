# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pdf_scout']

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
    'version': '0.0.2',
    'description': 'automatically create bookmarks in a PDF file',
    'long_description': "# pdf_scout\n\nThis CLI tool automatically generates PDF bookmarks (also known as an 'outline' or a 'table of contents') for computer-generated PDF documents.\n\n```bash\ncd pdf_scout\npoetry install\npoetry run python ./src/app.py\n```\n\n![screenshot](./assets/screenshot.png)\n\nThis project is a work in progress and will likely only generate accurate bookmarks for documents that conform to the following requirements:\n\n* Single column of text (not multiple columns)\n* Font size of header text >= font size of body text\n* Header text is justified or left-aligned\n\n## Development\n\nThis project manages its dependencies using [poetry](https://python-poetry.org) and is only supported for Python ^3.9. After installing poetry and entering the project folder, run the following to install the dependencies:\n\n```bash\npoetry install\n```\n\nTo open a virtualenv in the project folder with the dependencies, run:\n\n```bash\npoetry shell\n```\n\nTo run a script directly, run:\n\n```bash\npoetry run python ./src/app.py\n```\n\n### Tests\n\nThere are snapshot tests. Input PDFs are not provided at the moment, so you will have populate the `/pdf` folder manually:\n\n```bash\npoetry run pytest\npoetry run pytest --snapshot-update\n```",
    'author': 'Huey',
    'author_email': 'hello@huey.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hueyy/pdf_scout',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
