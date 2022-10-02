# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studatio', 'studatio._vendor', 'studatio._vendor.icalevents']

package_data = \
{'': ['*'], 'studatio._vendor': ['icalevents-0.1.26.dist-info/*']}

install_requires = \
['pyperclip>=1.8.2,<2.0.0', 'tomlkit>=0.11.4,<0.12.0']

entry_points = \
{'console_scripts': ['studatio = studatio:main']}

setup_kwargs = {
    'name': 'studatio',
    'version': '0.1.3',
    'description': 'Personal tool for my violin teaching database',
    'long_description': "# studatio\n\nstudatio is a Python tool for private music teachers to manage their studio's data.\n\nI am a violin teacher, and am primarily developing this for my own use, but I hope for the project to become useful to more teachers as it grows. Currently, studatio is meant to pull iCal data about music lessons and format in a way that can be useful for lesson schedules or facility reservations. I want to add support for automated facility reservations, billing, and note-taking.\n\nCurrently, studatio has only been tested on macOS. It likely runs out of the box on other Unix systems as well, and I would guess it can run on Windows with a few alterations to the file paths.\n\n## Installation\n\nFirst, install Python if it is not already installed. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install studatio.\n\n```bash\npip install studatio\n```\n\nOn first use, studatio will prompt you for a URL containing iCal data of your studio's calendar. This is stored in ```.config/studatio/config.toml```\n\n## Usage\n\n```studatio``` prints and copies to clipboard a formatted list of studio events.\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or add. Documentation and test coverage additions are just as welcome as changes to source code. I am an amateur programmer, but I always want to learn, so if there are things that work but are not best practices, I would be eager to hear them.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n",
    'author': 'Eliza Wilson',
    'author_email': 'elizaaverywilson@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
