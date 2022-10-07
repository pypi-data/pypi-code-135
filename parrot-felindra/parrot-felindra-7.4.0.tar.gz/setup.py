# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['felindra']

package_data = \
{'': ['*'], 'felindra': ['etc/share/*']}

install_requires = \
['cryptography', 'pycryptodome', 'requests']

entry_points = \
{'console_scripts': ['felindra = felindra.felindra_main:main']}

setup_kwargs = {
    'name': 'parrot-felindra',
    'version': '7.4.0',
    'description': 'Parrot Media Signature Verifier tool',
    'long_description': '# Felindra - Parrot Media Signature Verifier tool\n\nThe *felindra* Python module provides both a library and an executable\nto verify the authenticity and integrity of any signed photo taken by\nan *ANAFI Ai*. The tool can verify photos remotely on a drone by using the\nwebserver API or offline, by checking a directory and its subdirectories.\n\nFor more information, see the *felindra documentation*.\n\n## [Felindra Documentation](https://developer.parrot.com/docs/groundsdk-tools/photo-signature.html#felindra)\n\n## [Parrot developers forums](https://forum.developer.parrot.com/categories)\n\n* **Parrot Anafi Ai:** https://forum.developer.parrot.com/c/anafi-ai/\n\n## Supported platform\n\n* Tested with Python 3.8.10. It should work on newer versions.\n',
    'author': 'Mathieu Le Mauff',
    'author_email': 'mathieu.lemauff@parrot.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
