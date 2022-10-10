# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['imgmanip',
 'imgmanip.dialogs',
 'imgmanip.functions',
 'imgmanip.functions.tasks',
 'imgmanip.models',
 'imgmanip.widgets',
 'imgmanip.widgets.main',
 'imgmanip.widgets.task_frames']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.2.0,<10.0.0',
 'PySide6>=6.3.2,<7.0.0',
 'PyYAML>=6.0,<7.0',
 'Shapely>=1.8.4,<2.0.0',
 'geopandas>=0.11.1,<0.12.0',
 'natsort>=8.2.0,<9.0.0',
 'numpy>=1.23.3,<2.0.0',
 'opencv-python>=4.6.0.66,<5.0.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'pyqtdarktheme>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'imgmanip',
    'version': '0.0.1',
    'description': 'Image manipulation tool written in python in which you can select a large number of photos and perform a lot of different operations on them.',
    'long_description': "![logo](assets/logo.png)\n\nImage manipulation tool written in python in\nwhich you can select a large number of photos and\nperform a lot of different operations on them.\n---\nThe current list of operations\n\n- **Resize** - resizes the images to the given resolution or by a specified percentage.\n- **Compress** - compresses the image. The lower the 'quality',\n  the smaller the file size.\n- **Invert** - inverts the colors of the image.\n- **Flip** - flips the image in horizontal or vertical axis.\n- **Color detection** - marks where the given color appears in the image.\n  Additionally, it can save the **mask** in .png format,\n  **shapefile** and **geojson** file.\n- **Convert** - converts the image to the other format.\n\n## How to use\n\n![how_to_use](assets/how_to_use.gif)\n",
    'author': 'Mikołaj Badyl',
    'author_email': 'contact@hawier.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
