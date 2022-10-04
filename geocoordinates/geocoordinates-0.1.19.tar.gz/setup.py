# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geocoordinates']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.3,<2.0.0', 'pandas>=1.5.0,<2.0.0']

setup_kwargs = {
    'name': 'geocoordinates',
    'version': '0.1.19',
    'description': '',
    'long_description': '# Geographic coordinates coding problem \n\nContained is my solution for the geographic coordinates coding problem. There should be the following within this folder:\n\n* The dataset `lla_coordinate_time_series.csv`\n\n* The solution `geo-coordinates.py` file which outputs the two values to stdout\n\nAdditionally, there is a much more robust Julia implementation available at the private repository https://github.com/kathesch/GeoCoordinates.jl. This can be imported to any julia repl and is a good showcase of visualizations of this data. E-mail katherinegruenewald@gmail.com with your github information for access.  \n\n## Installation and Running \n\n1. Open a terminal with the working directory in this file. \n2. Run the following line to activate the virtual environment.\n   ```\n   source GeoCoordinates/bin/activate\n   ```\n3. Run the `geo-coordinates.py` script\n   ```\n   python GeoCoordinatespy\n   ```',
    'author': 'kathesch',
    'author_email': 'katherinegruenewald@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
