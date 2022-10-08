# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rocksdb_statistics']

package_data = \
{'': ['*']}

install_requires = \
['black==22.8.0', 'isort==5.10.1', 'mypy==0.982']

entry_points = \
{'console_scripts': ['rocksdb-statistics = '
                     'rocksdb_statistics.rocksdb_statistics:main']}

setup_kwargs = {
    'name': 'rocksdb-statistics',
    'version': '0.0.9',
    'description': 'Parses db_bench.log files outputted from RocksDB',
    'long_description': '# rocksdb-statistics\n\n[![PyPI version](https://badge.fury.io/py/rocksdb-statistics.svg)](https://badge.fury.io/py/rocksdb-statistics)\n\nA small snippet I wrote to generate plots for my thesis on [Auto-tuning RocksDB](https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2506148/19718_FULLTEXT.pdf)\n\nParses db_bench.log files outputted from RocksDB\nOutputs CSV-files and pgfplot of write, compaction and stall statistics.\n\n#### Supported statistics:\n\n- interval_writes\n- cumulative_writes\n- interval_stall\n- cumulative_stall\n- interval_compaction\n- cumulative_compaction\n\n## Usage\n\n`pip install rocksdb-statistics`\n\n`rocksdb-statistics db_bench.log`\n\nParsed stats are outputted to `output/` in the current directory\n\nAlternatively specify what stats to output\n`rocksdb-statistics db_bench.log --statistics "interval_writes,interval_compaction"`\n\n## Example\n\nRun db_bench with statistics using `stats_interval_seconds` to retrieve stats for each second. Make sure to set `stats_per_interval` to make db_bench output `** DB stats **` for each interval.\n\n`./db_bench --benchmarks="fillrandom,stats" -stats_interval_seconds 1 -stats_per_interval 1 &> db_bench.log`\n`rocksdb-statistics db_bench.log`\n\nThe directory `output/` contains the parsed statistics in csv.\nExample files are provided in the `example/` directory.\n\nYou can also add `-statistics` to get a summary of a lot of other things.\n`./db_bench --benchmarks="fillrandom,stats" -statistics -stats_interval_seconds 1 -stats_per_interval 1 &> db_bench.log`\n\n## Example plots\n\nBelow are some plots I generated using this tool for my thesis.\n\n<img src="example/plots.png" style="width: 50%" />\n',
    'author': 'Hans-Wilhelm Warlo',
    'author_email': 'hw@warlo.no',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/warlo/rocksdb-statistics/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
