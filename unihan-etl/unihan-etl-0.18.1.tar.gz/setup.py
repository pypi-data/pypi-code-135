# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['unihan_etl']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML', 'appdirs', 'unicodecsv', 'zhon']

entry_points = \
{'console_scripts': ['unihan-etl = unihan_etl.__main__:run']}

setup_kwargs = {
    'name': 'unihan-etl',
    'version': '0.18.1',
    'description': 'Export UNIHAN data of Chinese, Japanese, Korean to CSV, JSON or YAML',
    'long_description': '# unihan-etl &middot; [![Python Package](https://img.shields.io/pypi/v/unihan-etl.svg)](https://pypi.org/project/unihan-etl/) [![License](https://img.shields.io/github/license/cihai/unihan-etl.svg)](https://github.com/cihai/unihan-etl/blob/master/LICENSE) [![Code Coverage](https://codecov.io/gh/cihai/unihan-etl/branch/master/graph/badge.svg)](https://codecov.io/gh/cihai/unihan-etl)\n\n[ETL] tool for Unicode\'s Han Unification\n([UNIHAN](http://www.unicode.org/charts/unihan.html)) database releases. unihan-etl retrieves\n(downloads), extracts (unzips), and transforms the database from Unicode\'s website to a flat,\ntabular or structured, tree-like format.\n\nunihan-etl can be used as a python library through its\n[API](https://unihan-etl.git-pull.com/en/latest/api.html), to retrieve data as a python object, or\nthrough the [CLI](https://unihan-etl.git-pull.com/en/latest/cli.html) to retrieve a CSV, JSON, or\nYAML file.\n\nPart of the [cihai](https://cihai.git-pull.com) project. Similar project:\n[libUnihan](http://libunihan.sourceforge.net/).\n\nUNIHAN Version compatibility (as of unihan-etl v0.10.0):\n[11.0.0](https://www.unicode.org/reports/tr38/tr38-25.html#History) (released 2018-05-08, revision\n25).\n\n[UNIHAN](http://www.unicode.org/charts/unihan.html)\'s data is dispersed across multiple files in the\nformat of:\n\n    U+3400  kCantonese  jau1\n    U+3400  kDefinition (same as U+4E18 丘) hillock or mound\n    U+3400  kMandarin   qiū\n    U+3401  kCantonese  tim2\n    U+3401  kDefinition to lick; to taste, a mat, bamboo bark\n    U+3401  kHanyuPinyin    10019.020:tiàn\n    U+3401  kMandarin   tiàn\n\nValues vary in shape and structure depending on their field type.\n[kHanyuPinyin](http://www.unicode.org/reports/tr38/#kHanyuPinyin) maps Unicode codepoints to\n[Hànyǔ Dà Zìdiǎn](https://en.wikipedia.org/wiki/Hanyu_Da_Zidian), where `10019.020:tiàn` represents\nan entry. Complicating it further, more variations:\n\n    U+5EFE  kHanyuPinyin    10513.110,10514.010,10514.020:gǒng\n    U+5364  kHanyuPinyin    10093.130:xī,lǔ 74609.020:lǔ,xī\n\n_kHanyuPinyin_ supports multiple entries delimited by spaces. ":" (colon) separate locations in the\nwork from pinyin readings. "," (comma) separate multiple entries/readings. This is just one of 90\nfields contained in the database.\n\n[etl]: https://en.wikipedia.org/wiki/Extract,_transform,_load\n\n## Tabular, "Flat" output\n\n### CSV (default)\n\n```console\n$ unihan-etl\n```\n\n```csv\nchar,ucn,kCantonese,kDefinition,kHanyuPinyin,kMandarin\n㐀,U+3400,jau1,(same as U+4E18 丘) hillock or mound,,qiū\n㐁,U+3401,tim2,"to lick; to taste, a mat, bamboo bark",10019.020:tiàn,tiàn\n```\n\nTo preview in the CLI, try [tabview](https://github.com/TabViewer/tabview) or\n[csvlens](https://github.com/YS-L/csvlens).\n\n### JSON\n\n```console\n$ unihan-etl -F json --no-expand\n```\n\n```json\n[\n  {\n    "char": "㐀",\n    "ucn": "U+3400",\n    "kDefinition": "(same as U+4E18 丘) hillock or mound",\n    "kCantonese": "jau1",\n    "kHanyuPinyin": null,\n    "kMandarin": "qiū"\n  },\n  {\n    "char": "㐁",\n    "ucn": "U+3401",\n    "kDefinition": "to lick; to taste, a mat, bamboo bark",\n    "kCantonese": "tim2",\n    "kHanyuPinyin": "10019.020:tiàn",\n    "kMandarin": "tiàn"\n  }\n]\n```\n\nTools:\n\n- View in CLI: [python-fx](https://github.com/cielong/pyfx),\n  [jless](https://github.com/PaulJuliusMartinez/jless) or\n  [fx](https://github.com/antonmedv/fx).\n- Filter via CLI: [jq](https://github.com/stedolan/jq),\n  [jql](https://github.com/yamafaktory/jql),\n  [gojq](https://github.com/itchyny/gojq).\n\n### YAML\n\n```console\n$ unihan-etl -F yaml --no-expand\n```\n\n```yaml\n- char: 㐀\n  kCantonese: jau1\n  kDefinition: (same as U+4E18 丘) hillock or mound\n  kHanyuPinyin: null\n  kMandarin: qiū\n  ucn: U+3400\n- char: 㐁\n  kCantonese: tim2\n  kDefinition: to lick; to taste, a mat, bamboo bark\n  kHanyuPinyin: 10019.020:tiàn\n  kMandarin: tiàn\n  ucn: U+3401\n```\n\nFilter via the CLI with [yq](https://github.com/mikefarah/yq).\n\n## "Structured" output\n\nCodepoints can pack a lot more detail, unihan-etl carefully extracts these values in a uniform\nmanner. Empty values are pruned.\n\nTo make this possible, unihan-etl exports to JSON, YAML, and python list/dicts.\n\n<div class="admonition">\n\nWhy not CSV?\n\nUnfortunately, CSV is only suitable for storing table-like information. File formats such as JSON\nand YAML accept key-values and hierarchical entries.\n\n</div>\n\n### JSON\n\n```console\n$ unihan-etl -F json\n```\n\n```json\n[\n  {\n    "char": "㐀",\n    "ucn": "U+3400",\n    "kDefinition": ["(same as U+4E18 丘) hillock or mound"],\n    "kCantonese": ["jau1"],\n    "kMandarin": {\n      "zh-Hans": "qiū",\n      "zh-Hant": "qiū"\n    }\n  },\n  {\n    "char": "㐁",\n    "ucn": "U+3401",\n    "kDefinition": ["to lick", "to taste, a mat, bamboo bark"],\n    "kCantonese": ["tim2"],\n    "kHanyuPinyin": [\n      {\n        "locations": [\n          {\n            "volume": 1,\n            "page": 19,\n            "character": 2,\n            "virtual": 0\n          }\n        ],\n        "readings": ["tiàn"]\n      }\n    ],\n    "kMandarin": {\n      "zh-Hans": "tiàn",\n      "zh-Hant": "tiàn"\n    }\n  }\n]\n```\n\n### YAML\n\n```console\n$ unihan-etl -F yaml\n```\n\n```yaml\n- char: 㐀\n  kCantonese:\n    - jau1\n  kDefinition:\n    - (same as U+4E18 丘) hillock or mound\n  kMandarin:\n    zh-Hans: qiū\n    zh-Hant: qiū\n  ucn: U+3400\n- char: 㐁\n  kCantonese:\n    - tim2\n  kDefinition:\n    - to lick\n    - to taste, a mat, bamboo bark\n  kHanyuPinyin:\n    - locations:\n        - character: 2\n          page: 19\n          virtual: 0\n          volume: 1\n      readings:\n        - tiàn\n  kMandarin:\n    zh-Hans: tiàn\n    zh-Hant: tiàn\n  ucn: U+3401\n```\n\n## Features\n\n- automatically downloads UNIHAN from the internet\n- strives for accuracy with the specifications described in\n  [UNIHAN\'s database design](http://www.unicode.org/reports/tr38/)\n- export to JSON, CSV and YAML (requires [pyyaml](http://pyyaml.org/)) via `-F`\n- configurable to export specific fields via `-f`\n- accounts for encoding conflicts due to the Unicode-heavy content\n- designed as a technical proof for future CJK (Chinese, Japanese, Korean) datasets\n- core component and dependency of [cihai](https://cihai.git-pull.com), a CJK library\n- [data package](http://frictionlessdata.io/data-packages/) support\n- expansion of multi-value delimited fields in YAML, JSON and python dictionaries\n- supports >= 3.7 and pypy\n\nIf you encounter a problem or have a question, please\n[create an issue](https://github.com/cihai/unihan-etl/issues/new).\n\n## Installation\n\nTo download and build your own UNIHAN export:\n\n```console\n$ pip install --user unihan-etl\n```\n\nor by [pipx](https://pypa.github.io/pipx/docs/):\n\n```console\n$ pipx install unihan-etl\n```\n\n### Developmental releases\n\n[pip](https://pip.pypa.io/en/stable/):\n\n```console\n$ pip install --user --upgrade --pre unihan-etl\n```\n\n[pipx](https://pypa.github.io/pipx/docs/):\n\n```console\n$ pipx install --suffix=@next \'unihan-etl\' --pip-args \'\\--pre\' --force\n// Usage: unihan-etl@next load yoursession\n```\n\n## Usage\n\n`unihan-etl` offers customizable builds via its command line arguments.\n\nSee [unihan-etl CLI arguments](https://unihan-etl.git-pull.com/en/latest/cli.html) for information\non how you can specify columns, files, download URL\'s, and output destination.\n\nTo output CSV, the default format:\n\n```console\n$ unihan-etl\n```\n\nTo output JSON:\n\n```console\n$ unihan-etl -F json\n```\n\nTo output YAML:\n\n```console\n$ pip install --user pyyaml\n$ unihan-etl -F yaml\n```\n\nTo only output the kDefinition field in a csv:\n\n```console\n$ unihan-etl -f kDefinition\n```\n\nTo output multiple fields, separate with spaces:\n\n```console\n$ unihan-etl -f kCantonese kDefinition\n```\n\nTo output to a custom file:\n\n```console\n$ unihan-etl --destination ./exported.csv\n```\n\nTo output to a custom file (templated file extension):\n\n```console\n$ unihan-etl --destination ./exported.{ext}\n```\n\nSee [unihan-etl CLI arguments](https://unihan-etl.git-pull.com/en/latest/cli.html) for advanced\nusage examples.\n\n## Code layout\n\n```console\n# cache dir (Unihan.zip is downloaded, contents extracted)\n{XDG cache dir}/unihan_etl/\n\n# output dir\n{XDG data dir}/unihan_etl/\n  unihan.json\n  unihan.csv\n  unihan.yaml   # (requires pyyaml)\n\n# package dir\nunihan_etl/\n  process.py    # argparse, download, extract, transform UNIHAN\'s data\n  constants.py  # immutable data vars (field to filename mappings, etc)\n  expansion.py  # extracting details baked inside of fields\n  util.py       # utility / helper functions\n\n# test suite\ntests/*\n```\n\n## Developing\n\n```console\n$ git clone https://github.com/cihai/unihan-etl.git\n```\n\n```console\n$ cd unihan-etl\n```\n\n[Bootstrap your environment and learn more about contributing](https://cihai.git-pull.com/contributing/). We use the same conventions / tools across all cihai projects: `pytest`, `sphinx`, `flake8`, `mypy`, `black`, `isort`, `tmuxp`, and file watcher helpers (e.g. `entr(1)`).\n\n## More information\n\n[![Docs](https://github.com/cihai/unihan-etl/workflows/docs/badge.svg)](https://unihan-etl.git-pull.com/)\n[![Build Status](https://github.com/cihai/unihan-etl/workflows/tests/badge.svg)](https://github.com/cihai/unihan-etl/actions?query=workflow%3A%22tests%22)\n',
    'author': 'Tony Narlock',
    'author_email': 'tony@git-pull.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://unihan-etl.git-pull.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
