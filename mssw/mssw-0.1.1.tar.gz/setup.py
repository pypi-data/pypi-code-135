# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mssw']

package_data = \
{'': ['*'], 'mssw': ['src/*']}

install_requires = \
['pybind11>=2.10.0,<3.0.0', 'setuptools>=65.4.1,<66.0.0']

setup_kwargs = {
    'name': 'mssw',
    'version': '0.1.1',
    'description': 'Modern Cpp binding for complete-striped-smith-watern-library',
    'long_description': '[![Release](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/release.yml/badge.svg)](https://github.com/cauliyang/Complete-Striped-Smith-Waterman-Library/actions/workflows/release.yml)\n\n# Modern C++ Binding for SSW Library\n\n## Changes\n\n- Add Modern C++ Binding\n- Use pybind11 Binding\n- Provide Python api\n\n## Installation\n\n```bash\n$ pip install mssw\n```\n\n## Usage\n\n```python\nimport mssw\n\nreference = "CAGCCTTTCTGACCCGGAAATCAAAATAGGCACAACAAA"\nquery = "CTGAGCCGGTAAATC"\nmasklen = 15\naligner = mssw.StripedSmithWaterman.Aligner()\naligner_filter = mssw.StripedSmithWaterman.Filter()\nalignment = mssw.StripedSmithWaterman.Alignment()\naligner.Align(query, reference, len(reference), aligner_filter, alignment, masklen)\n```\n',
    'author': 'Yangyang Li',
    'author_email': 'yangyang.li@northwestern.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
