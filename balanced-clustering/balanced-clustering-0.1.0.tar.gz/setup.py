# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['balanced_clustering', 'balanced_clustering.utils']

package_data = \
{'': ['*']}

install_requires = \
['Cython>=0.29.28,<0.30.0',
 'ipykernel>=6.9.1,<7.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'jupyterlab-latex>=3.1.0,<4.0.0',
 'jupyterlab>=3.2.9,<4.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'seaborn>=0.11.2,<0.12.0']

setup_kwargs = {
    'name': 'balanced-clustering',
    'version': '0.1.0',
    'description': 'Clustering metrics for imbalanced datasets',
    'long_description': 'None',
    'author': 'Hassaan Maan',
    'author_email': 'hurmaan99@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<=3.10.0',
}


setup(**setup_kwargs)
