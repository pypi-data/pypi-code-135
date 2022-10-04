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
    'version': '0.1.22',
    'description': '',
    'long_description': '# Geographic coordinates coding problem \n\nContained is my solution for the geographic coordinates coding problem. The Julia version of this code can be found at https://github.com/kathesch/GeoCoordinates.\n\n## Installation \n\nRun the following in terminal to install geocoordinates with pip\n\n`pip install geocoordinates`\n\n## Running \n\n1. Open a python REPL\n2. `import geocoordinates as gc`\n3. `gc.time_series_analysis()`\n\n```python\n~ % python\nPython 3.10.7 (main, Sep 14 2022, 22:38:23) [Clang 14.0.0 (clang-1400.0.29.102)] on darwin\nType "help", "copyright", "credits" or "license" for more information.\n>>> import geocoordinates as gc\n>>> gc.time_series_analysis()\nVelocity at Unix time  1532334000 :\n [ -995.91526875 -2514.43889398    55.92122005] m/s\nVelocity at Unix time  1532335268 :\n [-3471.02128308  1760.25788787 -4867.4760627 ] m/s\n ```',
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
