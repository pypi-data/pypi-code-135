# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grafana-calendar-annotator']

package_data = \
{'': ['*']}

install_requires = \
['ics>=0.7.2,<0.8.0',
 'python-decouple>=3.6,<4.0',
 'requests>=2.28.1,<3.0.0',
 'rich-click>=1.5.2,<2.0.0']

entry_points = \
{'console_scripts': ['grafana-calendar-annotator = src.cli:cli']}

setup_kwargs = {
    'name': 'grafana-calendar-annotator',
    'version': '0.1.0',
    'description': 'Generate Grafana Annotations from calendar events',
    'long_description': "# Grafana Calendar Annotator\n\n[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6552/badge)](https://bestpractices.coreinfrastructure.org/projects/6552)\n\nGenerate [annotations](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/annotate-visualizations/) in Grafana from events pulled from an ICS calendar.\n\n## Getting Started\n\n<!--TODO-->\n\n### Installing\n\n<!--TODO-->\n\n## Running the tests\n\n<!--TODO-->\n\n## Deployment\n\n<!--TODO-->\n\n## Built With\n\n  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used for the Code of Conduct\n  - [Poetry](https://python-poetry.org/) - Used for build and packaging\n  - [Contributing.md Generator](https://generator.contributing.md/)\n  - [Billie Thompson's README Template](https://github.com/PurpleBooth/a-good-readme-template)\n\n## Contributing\n\nPlease read [CONTRIBUTING.md](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/CONTRIBUTING.md) for details on our code\nof conduct, and the process for submitting pull requests to us.\n\n## Versioning\n\nWe use [Semantic Versioning](http://semver.org/) for versioning. For the versions\navailable, see the [tags on this\nrepository](https://github.com/cam-barts/grafana-calendar-annotator/tags).\n\n## Contributors\n\n[Contributors](https://github.com/cam-barts/grafana-calendar-annotator/contributors)\nwho participated in this project.\n\n## License\n\nThis project is licensed under the [MIT](https://github.com/cam-barts/grafana-calendar-annotator/blob/main/LICENSE.txt).",
    'author': 'Cam',
    'author_email': 'camerond.barts@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cam-barts/grafana-calendar-annotator',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
