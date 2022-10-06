# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycsbinarywriter', 'pycsbinarywriter.cstypes', 'pycsbinarywriter.test']

package_data = \
{'': ['*']}

install_requires = \
['pytz>=2022.2.1,<2023.0.0']

setup_kwargs = {
    'name': 'pycsbinarywriter',
    'version': '0.0.4',
    'description': 'Helpers for parsing binary data created by dotnet BinaryWriters.',
    'long_description': "# pyCSBinaryWriter\n\nA simple library for .NET binary (de)serialization.\n\n## Limitations\n\n* Decimal is not implemented yet. Pull requests are welcome.\n\n## Installation\n\n```shell\n$ pip install -U pycsbinarywriter\n```\n\n## Usage\n\n```python\nfrom pycsbinarywriter import cstypes\n\n# Decode .NET 7-bit-prefixed string\nassert 'abc123' == cstypes.string.unpack(b'\\x06\\x61\\x62\\x63\\x31\\x32\\x33')\n\n# Decode .NET uint8 (ubyte)\nassert 127 == cstypes.uint8.unpack(b'\\x7f')\n\n# Encode .NET int16\nassert b'\\x2e\\xfb' == cstypes.int16.pack(-1234)\n```\n\n## License\n\nMIT License\n",
    'author': 'Rob Nelson',
    'author_email': 'nexisentertainment@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/N3X15/pycsbinarywriter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
