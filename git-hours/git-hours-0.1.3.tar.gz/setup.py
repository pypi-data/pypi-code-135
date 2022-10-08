# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['git_hours']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.28,<4.0.0', 'devtools>=0.9.0,<0.10.0', 'pydash>=5.1.1,<6.0.0']

entry_points = \
{'console_scripts': ['git-hours = git_hours.main:main']}

setup_kwargs = {
    'name': 'git-hours',
    'version': '0.1.3',
    'description': 'Estimate time spent on a git repository ',
    'long_description': "# git-hours\n\nEstimate time spent on a git repository.\n\nPort to Python of the `git-hours` project by <https://github.com/kimmobrunfeldt/git-hours>.\n\nTHIS PORT IS NOT COMPLETE YET. IF YOU WANT TO HELP, PLEASE DO SO.\n\n\n## Example use\n\nTime spent on developing [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy.git):\n\n```javascript\n➜  bootstrap git:(master) git-hours\n{\n\n  ...\n\n    'total': {\n        'hours': 18276.158333333322,\n        'commits': 15504,\n    },\n}\n```\n\nFrom a person working 8 hours per day, it would take more than 10 years to build SQLAlchemy.\n\n*Please note that the information is not be accurate enough to be used in billing.*\n\n\n## Install\n\n    $ pipx install git-hours\n\n\n\n## How it works\n\nThe algorithm for estimating hours is quite simple. For each author in the commit history, do the following:\n\n<br><br>\n\n![](https://github.com/sfermigier/git-hours/raw/main/docs/step0.png)\n\n*Go through all commits and compare the difference between\nthem in time.*\n\n<br><br><br>\n\n![](https://github.com/sfermigier/git-hours/raw/main/docs/step1.png)\n\n*If the difference is smaller or equal then a given threshold, group the commits\nto a same coding session.*\n\n<br><br><br>\n\n![](https://github.com/sfermigier/git-hours/raw/main/docs/step2.png)\n\n*If the difference is bigger than a given threshold, the coding session is finished.*\n\n<br><br><br>\n\n![](https://github.com/sfermigier/git-hours/raw/main/docs/step3.png)\n\n*To compensate the first commit whose work is unknown, we add extra hours to the coding session.*\n\n<br><br><br>\n\n![](https://github.com/sfermigier/git-hours/raw/main/docs/step4.png)\n\n*Continue until we have determined all coding sessions and sum the hours\nmade by individual authors.*\n\n\n## Usage\n\nIn root of a git repository run:\n\n    $ git-hours\n\n",
    'author': 'Stefane Fermigier',
    'author_email': 'sf@abilian.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
