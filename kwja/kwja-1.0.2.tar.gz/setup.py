# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kwja',
 'kwja.callbacks',
 'kwja.cli',
 'kwja.datamodule',
 'kwja.datamodule.datasets',
 'kwja.datamodule.examples',
 'kwja.datamodule.extractors',
 'kwja.evaluators',
 'kwja.models',
 'kwja.models.models',
 'kwja.preprocessors',
 'kwja.utils']

package_data = \
{'': ['*']}

install_requires = \
['BetterJSONStorage>=1.3.0,<2.0.0',
 'dartsclone>=0.10.2,<0.11.0',
 'hydra-core>=1.2,<2.0',
 'ipadic>=1.0.0,<2.0.0',
 'jinf>=1.0.4,<2.0.0',
 'kyoto-reader>=2.5.2,<3.0.0',
 'omegaconf>=2.1,<3.0',
 'pandas>=1.4.2,<2.0.0',
 'protobuf>=3.20,<4.0',
 'python-Levenshtein>=0.12.2,<0.13.0',
 'python-dotenv>=0.20.0,<0.21.0',
 'pytorch-lightning>=1.6.5,<2.0.0',
 'rhoknp>=0.4.0,<0.5.0',
 'rich>=12.4.4,<13.0.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'seqeval>=1.2.2,<2.0.0',
 'tinydb>=4.7.0,<5.0.0',
 'tokenizers>=0.12.1,<0.13.0',
 'torch>=1.11.0,<1.12.0',
 'transformers>=4.19.2,<4.20.0',
 'typer>=0.6.1,<0.7.0',
 'wandb>=0.13.3,<0.14.0']

entry_points = \
{'console_scripts': ['kwja = kwja.cli.cli:app']}

setup_kwargs = {
    'name': 'kwja',
    'version': '1.0.2',
    'description': 'A unified language analyzer for Japanese',
    'long_description': '# KWJA: Kyoto-Waseda Japanese Analyzer\n\n[![test](https://github.com/ku-nlp/kwja/actions/workflows/test.yml/badge.svg)](https://github.com/ku-nlp/kwja/actions/workflows/test.yml)\n[![codecov](https://codecov.io/gh/ku-nlp/kwja/branch/main/graph/badge.svg?token=A9FWWPLITO)](https://codecov.io/gh/ku-nlp/kwja)\n[![PyPI](https://img.shields.io/pypi/v/kwja)](https://pypi.org/project/kwja/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kwja)\n\nKWJA is a Japanese language analyzer based on pre-trained language models.\nKWJA performs many language analysis tasks, including:\n- Typo correction\n- Tokenization\n- Morphological analysis\n- Named entity recognition\n- Dependency parsing\n- PAS analysis\n- Coreference resolution\n- Discourse relation analysis\n- etc.\n\n## Requirements\n\n- Python: 3.9+\n- Dependencies: See [pyproject.toml](./pyproject.toml).\n\n## Getting Started\n\nInstall KWJA with pip:\n\n```shell\n$ pip install kwja\n```\n\nPerform language analysis with the `kwja` command (the result is in the KNP format):\n\n```shell\n# Analyze a text\n$ kwja --text "KWJAは日本語の統合解析ツールです。汎用言語モデルを利用し、様々な言語解析を統一的な方法で解いています。"\n\n# Analyze a text file\n$ kwja --file path/to/file.txt\n```\n\n## Usage from Python\n\nMake sure you have `kwja` command in your path:\n\n```shell\n$ which kwja\n/path/to/kwja\n```\n\nInstall [rhoknp](https://github.com/ku-nlp/rhoknp):\n\n```shell\n$ pip install rhoknp\n```\n\nPerform language analysis with the `kwja` instance:\n\n```python\nfrom rhoknp import KWJA\nkwja = KWJA()\nanalyzed_document = kwja.apply(\n    "KWJAは日本語の統合解析ツールです。汎用言語モデルを利用し、様々な言語解析を統一的な方法で解いています。"\n)\n```\n\n## Citation\n\n```bibtex\n@InProceedings{植田2022,\n  author    = {植田 暢大 and 大村 和正 and 児玉 貴志 and 清丸 寛一 and 村脇 有吾 and 河原 大輔 and 黒橋 禎夫},\n  title     = {KWJA：汎用言語モデルに基づく日本語解析器},\n  booktitle = {第253回自然言語処理研究会},\n  year      = {2022},\n  address   = {京都},\n}\n```\n',
    'author': 'Hirokazu Kiyomaru',
    'author_email': 'kiyomaru@i.kyoto-u.ac.jp',
    'maintainer': 'Hirokazu Kiyomaru',
    'maintainer_email': 'kiyomaru@i.kyoto-u.ac.jp',
    'url': 'https://github.com/ku-nlp/kwja',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
