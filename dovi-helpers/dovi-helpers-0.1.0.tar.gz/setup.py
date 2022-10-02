# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dovi_helpers',
 'dovi_helpers.cli',
 'dovi_helpers.cli.commands',
 'dovi_helpers.models']

package_data = \
{'': ['*']}

install_requires = \
['click', 'colorama', 'pydantic', 'structlog']

entry_points = \
{'console_scripts': ['dovi_helpers = dovi_helpers.cli.__main__:main']}

setup_kwargs = {
    'name': 'dovi-helpers',
    'version': '0.1.0',
    'description': 'Command line interface for collection of scripts to convert MKV container into Dolby Vision 8.1 compatible MP4.',
    'long_description': '# Dolby Vision Helpers\n\n## System prerequisites\n\n- [mediainfo](https://mediaarea.net/ru/MediaInfo)\n- [mp4muxer](https://github.com/DolbyLaboratories/dlb_mp4base)\n- [dovi_tool](https://github.com/quietvoid/dovi_tool)\n\n## Usage\n\n```text\nUsage: python -m cli [OPTIONS] COMMAND [ARGS]...\n\n  Command line interface for collection of scripts to convert MKV container\n  into Dolby Vision 8.1 compatible MP4.\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  demux     Demuxing MKV container into HEVC and AC3 streams.\n  info      Gathering mediainfo data into cached file.\n  mux       Muxing HEVC and AC3 streams into compatible MP4 container.\n  pipeline  Command to chain info, demux and mux operations.\n```\n',
    'author': 'Skyross',
    'author_email': 'skyross000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
