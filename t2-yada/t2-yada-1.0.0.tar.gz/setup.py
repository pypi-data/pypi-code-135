# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yada']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 't2-yada',
    'version': '1.0.0',
    'description': 'Yet another dataclass argparse',
    'long_description': "# yada\n\n![PyPI](https://img.shields.io/pypi/v/t2-yada)\n![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)\n[![GitHub Issues](https://img.shields.io/github/issues/binh-vu/yada.svg)](https://github.com/binh-vu/yada/issues)\n![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\nYada (**Y**et **A**nother **D**ataclass **A**rgument Parser!) is a library to automatically generate `argparse.ArgumentParser` given data classes. Compared to some available options such as: [Huggingface's HfArgumentParser](https://huggingface.co/transformers/v4.2.2/_modules/transformers/hf_argparser.html), [argparse_dataclass](https://github.com/mivade/argparse_dataclass), and [tap](https://github.com/swansonk14/typed-argument-parser), it offers the following benefits:\n\n1. Static Type Checking\n2. Nested data classes and complex types\n3. Easy to extend and customize the parser\n4. Generate command line arguments given the data classes.\n\n## Installation\n\nInstall via PyPI (requires Python 3.8+):\n\n```bash\npip install t2-yada\n```\n",
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/binh-vu/yada',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
