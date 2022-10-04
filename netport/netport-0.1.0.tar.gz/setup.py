# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netport']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.85.0,<0.86.0',
 'psutil>=5.9.2,<6.0.0',
 'redis>=4.3.4,<5.0.0',
 'requests>=2.28.1,<3.0.0',
 'uvicorn[standard]>=0.18.3,<0.19.0']

entry_points = \
{'console_scripts': ['netport = netport.cli:run']}

setup_kwargs = {
    'name': 'netport',
    'version': '0.1.0',
    'description': 'Tool for managing resources on a remove machine using openapi',
    'long_description': '# Developer Guide\n1. Clone the repo\n2. Make sure that poetry is installed on your computer (How to install \n   [Poetry](https://python-poetry.org/docs/))\n3. run `poetry install`\n4. Your environment is now ready to run, develop and test **netport**!\n\n\n# Run\n\n```bash\n# Inside the repository\nuvicorn netport.netport:app --host 0.0.0.0 --port 80 --reload\n```\n\nOpen browser at: http://host_ip/docs',
    'author': 'Igal Kolihman',
    'author_email': 'igalk.spam@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/IgalKolihman/netport',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
