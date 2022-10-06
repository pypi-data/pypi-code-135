# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rocksdb_statistics']

package_data = \
{'': ['*']}

install_requires = \
['black==22.8.0', 'isort==5.10.1', 'mypy==0.982']

setup_kwargs = {
    'name': 'rocksdb-statistics',
    'version': '0.0.2',
    'description': 'Parses db_bench.log files outputted from RocksDB',
    'long_description': '# rocksdb-statistics\n\nSmall python script to generate basic pgfplots axes using regex\n\n## Usage\n\n`pip install rocksdb-statistics`\n`python -m rocksdb-statistics db_bench.log`\n',
    'author': 'Hans-Wilhelm Warlo',
    'author_email': 'hw@warlo.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/warlo/rocksdb-statistics/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
