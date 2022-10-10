# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mssw', 'mssw.cpp']

package_data = \
{'': ['*'], 'mssw': ['bindings/*', 'src/*']}

install_requires = \
['pybind11>=2.10.0,<3.0.0', 'setuptools>=65.4.1,<66.0.0']

setup_kwargs = {
    'name': 'mssw',
    'version': '0.1.4',
    'description': 'Modern Cpp binding for complete-striped-smith-watern-library',
    'long_description': '[![pypi](https://img.shields.io/pypi/v/mssw.svg)][pypi status]\n[![status](https://img.shields.io/pypi/status/mssw.svg)][pypi status]\n[![python version](https://img.shields.io/pypi/pyversions/mssw)][pypi status]\n[![Tests](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/tests.yml/badge.svg)](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/tests.yml)\n[![Release](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/release.yml/badge.svg)](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/release.yml)\n\n[pypi status]: https://pypi.org/project/mssw/0.1.1/\n\n# Modern C++ Binding for SSW Library\n\n## Changes\n\n- Add Modern C++ Binding\n- Use pybind11 Binding\n- Provide Python api\n\n## Installation\n\n```bash\n$ pip install mssw\n```\n\n## Benchmark\n\nThe result is tested in Linux x86_64  4 cores and 4GB of memory.\n\n### With BioPython\n\n| Query Length | Reference Length | mssw Time (s) | bio python Time (s) | Speedup  |\n| ------------ | ---------------- | ------------- | ------------------- | :------- |\n| 15           | 39               | 4.470348e-05  | 1.424551e-04        | 3.186666 |\n| 150          | 390              | 2.179623e-04 |  2.270699e-03        | 10.41785 |\n| 1500         | 3900             | 1.665862e-02  | 1.534623e-01        | 9.212187 |\n| 15000        | 39000            | 1.696888e+00  | 1.574137e+01        | 9.276609 |\n\n## Usage\n\n### Example 1: Alignment with default filter and score matrix\n\n```python\nimport mssw\n\nreference = "CAGCCTTTCTGACCCGGAAATCAAAATAGGCACAACAAA"\nquery = "CTGAGCCGGTAAATC"\n# default match: int = 2, mismatch: int = 2, gap_open: int = 3, gap_extend: int = 1\naligner = mssw.Aligner()\naligner_filter = mssw.Filter()\nalignment = aligner.align(query, reference, aligner_filter)\n```\n\n### Example 2: Alignment with default filter and score matrix\n\n```python\nimport mssw\n\nreference = "CAGCCTTTCTGACCCGGAAATCAAAATAGGCACAACAAA"\nquery = "CTGAGCCGGTAAATC"\naligner = mssw.Aligner()\nalignment = aligner.align(query, reference)\n```\n\n### Example 3: Alignment with filter But custom gap open and gap extension\n\n```python\nimport mssw\n\nreference = "CAGCCTTTCTGACCCGGAAATCAAAATAGGCACAACAAA"\nquery = "CTGAGCCGGTAAATC"\naligner = mssw.Aligner(match=3, mismatch=1, gap_open=2, gap_extend=2)\nalignment = aligner.align(query, reference)\n```\n\n### Example 4: Alignment Result\n\n```python\nimport mssw\n\nreference = "CAGCCTTTCTGACCCGGAAATCAAAATAGGCACAACAAA"\nquery = "CTGAGCCGGTAAATC"\naligner = mssw.Aligner(match=3, mismatch=1, gap_open=2, gap_extend=2)\nalignment = aligner.align(query, reference)\n\nassert alignment.sw_score == 21\nassert alignment.sw_score_next_best == 2\nassert alignment.ref_begin == 8\nassert alignment.ref_end == 21\nassert alignment.query_begin == 0\nassert alignment.query_end == 14\nassert alignment.ref_end_next_best == 0\nassert alignment.mismatches == 2\nassert alignment.cigar_string == "4=1X4=1I5="\n```\n',
    'author': 'Yangyang Li',
    'author_email': 'yangyang.li@northwestern.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
