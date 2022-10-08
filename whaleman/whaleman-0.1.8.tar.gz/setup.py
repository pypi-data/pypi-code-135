# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['whaleman']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'colorama==0.4.5', 'docker>=6.0.0,<7.0.0']

entry_points = \
{'console_scripts': ['whaleman = whaleman:main']}

setup_kwargs = {
    'name': 'whaleman',
    'version': '0.1.8',
    'description': 'docker image versioning',
    'long_description': '## Intro\nwhaleman It is a simple tool to build , push and tag docker images.\n\nusing config .ini file to configure the tool. its annoying sometimes we tagging the image over and over again.\n\nwith this we can simply use config for tagging and versioning for each project/dockerfile\n\n\n## Installation\n\n```bash\npip install whaleman\n```\n\n## Usage\nby default name of the config file is docker.ini\n\nthe content of the config file is\n\n```ini\n[registry]\nname = index.docker.io # name of the registry URL , default is index.docker.io\nlogin = True # if you want to login to the registry , default is False\n# username for the registry \n# default is None or grab from env var with name DOCKER_USERNAME\ndocker_username = myusername \n# password for the registry , use quotes if you have symbol in the password.\n# default is None or grab from env var with name DOCKER_PASSWORD\ndocker_password = "mypassword"  \n\n[image]\nname = soberdev/homepage # this is name of the image, required\ntag = 0.1.8 # this is the version of the image or initial version, required\n```\n\nor if you want to create a config file simply run:\n\n```bash\nwhaleman createconfig\n```\n\nthe createconfig takes arguments, by default it will create a config file with name docker.ini\n\nbut you can create a config file with any name you want with the argument -n\n\n```bash\nwhaleman createconfig -n myconfig.ini\n```\n### DockerHost\nby default whaleman will try grab the value from env variables **DOCKER_HOST** if the environment is empty, then default to **unix://var/run/docker.sock**\n### Run the tool\n\npatch choices are **keep, micro, minor and major**\n\n**keep** will not update the version\n\n```bash\nwhaleman build <patch>\n```\n\nbuild the image and patch the version, after done will auto increment the version in the config file\n\nyou can build and push the image to the registry with the positional argument **push**\n\n```bash\nwhaleman build <patch> push\n```\nchange the registry uri dynamically\n\n```bash\nwhaleman build <patch> push -r your.registry.url\n```\n\nor you can use any config file and custom dockerfilename\n\n```bash\nwhaleman build <patch> push -f myconfig.ini -df mydockerfile.Dockerfile\n```\n\n## For more information\n```bash\nwhaleman -h\n```\n\n```bash\nwhaleman build -h\n```\n\n```bash\nwhaleman createconfig -h\n```\n\n## Logging Level\n\ndefault is INFO, but you can change it with the argument -l\n\n```bash\nwhaleman -l DEBUG build <patch>\n```',
    'author': 'rede akbar wijaya',
    'author_email': 'rede@soberdev.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
