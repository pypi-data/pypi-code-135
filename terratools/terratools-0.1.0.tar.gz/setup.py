# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['terratools', 'terratools.properties']

package_data = \
{'': ['*'], 'terratools.properties': ['data/*']}

install_requires = \
['Cartopy>=0.21.0,<0.22.0',
 'matplotlib>=3.5,<4.0',
 'netcdf4>=1,<2',
 'numpy>=1.23,<2.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'scipy>=1.6,<2.0']

setup_kwargs = {
    'name': 'terratools',
    'version': '0.1.0',
    'description': 'Tools to read, analyse and visualise models written by the TERRA mantle convection code.',
    'long_description': '# TerraTools\nTools to read, analyse and visualise models written by the TERRA mantle convection code.\nTerraTools is released under an MIT License.\n\nHomepage: [https://terratools.readthedocs.io/en/latest/](https://terratools.readthedocs.io/en/latest/)<br>\nDocumentation: [https://terratools.readthedocs.io/en/latest/](https://terratools.readthedocs.io/en/latest/)<br>\nSource code: [https://github.com/mantle-convection-constrained/terratools](https://github.com/mantle-convection-constrained/terratools)\n\n## Citing TerraTools\nWe are currently writing a paper for submission to JOSS. Watch this space.\n\n## Reporting bugs\nIf you would like to report any bugs, please raise an issue on [GitHub](https://github.com/mantle-convection-constrained/terratools/issues).\n\n## Contributing to TerraTools\nIf you would like to contribute bug fixes, new functions or new modules to the existing codebase, please fork the terratools repository, make the desired changes and then make a pull request on [GitHub](https://github.com/mantle-convection-constrained/terratools/pulls).\n\n## Acknowledgement and Support\nThis project is supported by [NERC Large Grant MC-squared](https://www.cardiff.ac.uk/research/explore/find-a-project/view/2592859-mc2-mantle-circulation-constrained).',
    'author': 'James Panton',
    'author_email': 'pantonjc@cardiff.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mantle-convection-constrained/terratools',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
