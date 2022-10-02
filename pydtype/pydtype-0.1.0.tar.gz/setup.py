# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydtype', 'pydtype.core', 'pydtype.frameworks']

package_data = \
{'': ['*']}

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.4,<5.0',
                             'typing-extensions>=4.1,<5.0']}

setup_kwargs = {
    'name': 'pydtype',
    'version': '0.1.0',
    'description': 'Translate data type specifiers between common frameworks',
    'long_description': '# pydtype\n\n[![PyPI](https://img.shields.io/pypi/v/pydtype.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/pydtype/)\n[![Python](https://img.shields.io/pypi/pyversions/pydtype.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/pydtype/)\n[![Test](https://img.shields.io/github/workflow/status/KaoruNishikawa/pydtype/Test?logo=github&label=Test&style=flat-square)](https://github.com/KaoruNishikawa/pydtype/actions)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](https://github.com/KaoruNishikawa/pydtype/blob/main/LICENSE)\n\nTranslate data type specifiers between common frameworks.\n\n## Features\n\nThis library provides:\n\n- Translator of data type spacifier such as [format character in struct](https://docs.python.org/3/library/struct.html#format-characters) and [dtype in Numpy](https://numpy.org/doc/stable/reference/arrays.dtypes.html#specifying-and-constructing-data-types).\n\n## Installation\n\n```shell\npip install pydtype\n```\n\n## Usage\n\nTo translate struct format `h` (2-byte integer) to Numpy format, run the following script.\n\n```python\n>>> import pydtype\n>>> pydtype.translate("h", "struct", "numpy")\n\'i16\'\n```\n\n---\n\nThis library is using [Semantic Versioning](https://semver.org).\n',
    'author': 'KaoruNishikawa',
    'author_email': 'k.nishikawa@a.phys.nagoya-u.ac.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/KaoruNishikawa/pydtype',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
