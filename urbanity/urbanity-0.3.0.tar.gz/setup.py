# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['urbanity']

package_data = \
{'': ['*'], 'urbanity': ['map_data/*', 'svi_data/*']}

install_requires = \
['Shapely==1.8.4',
 'geopandas==0.11.1',
 'ipyleaflet==0.17.1',
 'networkx==2.8.6',
 'numpy==1.23.3',
 'pyrosm==0.6.1',
 'rasterio==1.3.2',
 'vt2geojson>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'urbanity',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'winstonyym',
    'author_email': 'winstonyym@u.nus.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
