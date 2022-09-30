# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['iricore']

package_data = \
{'': ['*'],
 'iricore': ['data/ccir/*',
             'data/igrf/*',
             'data/index/*',
             'data/mcsat/*',
             'data/ursi/*',
             'iri2016/*',
             'iri2020/*']}

install_requires = \
['matplotlib>=3.6.0,<4.0.0', 'numpy>=1.23.3,<2.0.0', 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'iricore',
    'version': '1.0.7',
    'description': '',
    'long_description': '# iricore\nA fork of [iri2016](https://github.com/space-physics/iri2016). `iricore` implements a couple of optimizations to the `iri2016`\ncore Fortran code and Python interface to make it faster:\n1. Optimization of data files reading gives boost in case of iteration over large list of coordinates;\n2. `f2py` interface provides faster communication between Python and Fortran.\n\nOverall, this gives performance boost up to ~100x (see `examples/comparison.py`).\n\n**Important!** Because this package is mainly used for the [MIST experiment](http://www.physics.mcgill.ca/mist/), \nthe `iricore` cuts off calculation of unnecessary atmospheric parameters available in `iri2016`, leaving only electron density\nand electron temperature. All other parameters can be restored on demand (please contact me).\n\n## Installation\n\nThis package proved to work under Linux only (due to compilation difficulties in Windows). \nIf you are using Windows - consider installing [WSL](https://docs.microsoft.com/en-us/windows/wsl/install).\n\n### Prerequisites\n- Git\n```\nsudo apt instal git\n```\n\n- Fortran compiler, e.g. `gfortran`\n```\nsudo apt isntall gfortran\n```\n\n### Installing package\nNow you can simply install it via `pip`:\n\n```\npython3 -m pip install iricore\n```\n\n## Data files\n`IRI2016` model depends on [data files](http://irimodel.org/indices/) which are regularly updated.\n`iricore` does not autoupdate those, but provides tool for quick update. You can run from terminal\n```\npython3 -c "import iricore; iricore.update()"\n```\n\nor add\n\n```\nimport iricore\niricore.update()\n```\nto any Python script.\n\n## Usage\nFor usage examples see `examples/`.',
    'author': 'lap1dem',
    'author_email': 'vadym.bidula@gmail.com',
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
