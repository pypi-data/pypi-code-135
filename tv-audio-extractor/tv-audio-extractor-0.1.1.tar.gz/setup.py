# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tv_audio_extractor']

package_data = \
{'': ['*']}

install_requires = \
['parse-torrent-title>=2.4,<3.0', 'rich>=12.6.0,<13.0.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['tv-audio-extractor = tv_audio_extractor.main:main']}

setup_kwargs = {
    'name': 'tv-audio-extractor',
    'version': '0.1.1',
    'description': 'Extracts audio from tv shows and tags them appropriately',
    'long_description': None,
    'author': 'David Padbury',
    'author_email': 'david@davidpadbury.com',
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
