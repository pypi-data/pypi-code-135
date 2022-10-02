# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['otherworlds']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['otherworlds = console:run']}

setup_kwargs = {
    'name': 'otherworlds',
    'version': '0.9.0b1',
    'description': 'A name generator for new worlds',
    'long_description': "# Otherworlds\n\nA simple name generator. Mixes Klingon and real Exoplanets and star designations.\n\n\n## How to install\n\n1. Clone this repo\n2. Run `poetry install`\n\n\n## How to generate world names\n\n\nThis command generates names using real stars and exoplanets:\n\n```\npoetry run otherworlds\n```\n\nTo mix in some Klingon, use the '--klingon' flag:\n\n\n```\npoetry run otherworlds --klingon\n```\n\n\nYou can view the full help with this command:\n\n```\npoetry run otherworlds --help\n```\n",
    'author': 'Jurnell Cockhren',
    'author_email': 'jurnell@civichacker.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
