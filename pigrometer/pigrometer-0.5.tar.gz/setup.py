# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pigrometer']

package_data = \
{'': ['*'], 'pigrometer': ['templates/*']}

install_requires = \
['Flask>=2.2.2,<3.0.0',
 'RPi.GPIO>=0.7.1,<0.8.0',
 'adafruit-circuitpython-dht>=3.7.7,<4.0.0']

setup_kwargs = {
    'name': 'pigrometer',
    'version': '0.5',
    'description': 'An app for capturing temperature/humidity readings on a raspberrry pi and displaying the information through a web interface',
    'long_description': "# Raspberry Pi Temperature and Humidity\n\nThis app can be used to measure temperature and humidity with a DHT11 or DHT22 sensor connected to your raspberry pi. \n\n![Chart](docs/chart.png)\n\n### Usage\nInstall the wheel from the releases section using pip and connect a DHT11/DHT22 sensor connected to your raspberrry pi on port GPIO 4. You can then run the app with `python -m pigrometer`. To change which DHT sensor you're using or which pin you want to connect it to, run with `--dht-version` or `--dht-pin` set. Type `--help` for more options.\n\nTo change the amount of data shown on the chart add params to the url `?granularity=900&history=3` where granularity is the number of seconds between points on the graph and history is the number of days to display.\n\n### Upcoming features\n- More readable timestamps at the bottom of the chart\n- Better logging\n- More features in the web ui, ability to easily set time range and granularity\n- Ability to download data .csv with data from the web ui\n\n#### Feel free to create an issue if you run into any problems, or if there's any features you think would be a nice addition. Contributions are welcome as well.\n",
    'author': 'Brian Moody',
    'author_email': 'brian.k.moody@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
