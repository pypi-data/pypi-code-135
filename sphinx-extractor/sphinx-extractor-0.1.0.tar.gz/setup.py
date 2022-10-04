# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sphinx_extractor', 'sphinx_extractor.directives']

package_data = \
{'': ['*']}

install_requires = \
['sphinx>=5.0']

setup_kwargs = {
    'name': 'sphinx-extractor',
    'version': '0.1.0',
    'description': 'A Sphinx extension to extract rst code from text-based files.',
    'long_description': 'Sphinx-Extractor\n================\n\nA `Sphinx <https://www.sphinx-doc.org>`_ extension to extract \n`rst code <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ from text-based files.\n\nFor more details, please read the `documentation <https://useblocks.com/sphinx-extractor/>`_.\n',
    'author': 'Haiyang Zhang',
    'author_email': 'haiyang.zhang@useblocks.com',
    'maintainer': 'Haiyang Zhang',
    'maintainer_email': 'haiyang.zhang@useblocks.com',
    'url': 'https://github.com/useblocks/sphinx-extractor',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<3.11',
}


setup(**setup_kwargs)
