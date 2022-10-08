# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['repotea', 'repotea.cmds']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.0,<5.0']}

entry_points = \
{'console_scripts': ['repotea = repotea.repotea:main']}

setup_kwargs = {
    'name': 'repotea',
    'version': '0.1.0',
    'description': 'Command-line interface for Gitea API',
    'long_description': "# repotea\n\nrepotea is a command-line interface to operate Gitea's API endpoints.\n",
    'author': 'Michal Goral',
    'author_email': 'dev@goral.net.pl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
