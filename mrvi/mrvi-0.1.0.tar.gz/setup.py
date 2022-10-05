# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mrvi']

package_data = \
{'': ['*']}

install_requires = \
['anndata>=0.7.5', 'scvi-tools>=0.17.0']

extras_require = \
{':(python_version < "3.8") and (extra == "docs")': ['typing_extensions'],
 ':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0'],
 'dev': ['black>=20.8b1',
         'codecov>=2.0.8',
         'flake8>=3.7.7',
         'isort>=5.7',
         'jupyter>=1.0',
         'loompy>=3.0.6',
         'nbconvert>=5.4.0',
         'nbformat>=4.4.0',
         'pre-commit>=2.7.1',
         'pytest>=4.4',
         'scanpy>=1.6'],
 'docs': ['ipython>=7.1.1',
          'nbsphinx',
          'nbsphinx-link',
          'pydata-sphinx-theme>=0.4.0',
          'scanpydoc>=0.5',
          'sphinx>=4.1,<4.4',
          'sphinx-autodoc-typehints',
          'sphinx-rtd-theme']}

setup_kwargs = {
    'name': 'mrvi',
    'version': '0.1.0',
    'description': 'Multi-resolution analysis of single-cell data.',
    'long_description': '# Multi-resolution Variational Inference\n\nMulti-resolution Variational Inference (MrVI) is a package for analysis of sample-level heterogeneity in multi-site, multi-sample single-cell omics data. Built with [scvi-tools](https://scvi-tools.org).\n\n---\n\nTo install, run:\n\n```\npip install mrvi\n```\n',
    'author': 'Pierre Boyeau',
    'author_email': 'pierreboyeau@berkeley.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/YosefLab/mrvi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.2,<4.0',
}


setup(**setup_kwargs)
