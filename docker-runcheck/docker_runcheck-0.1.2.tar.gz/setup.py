# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['docker_runcheck']

package_data = \
{'': ['*']}

install_requires = \
['docker>=6.0.0,<7.0.0', 'dockerfile>=3.2.0,<4.0.0', 'rich>=12.5.1,<13.0.0']

entry_points = \
{'console_scripts': ['docker_runcheck = docker_runcheck.docker_runcheck:run']}

setup_kwargs = {
    'name': 'docker-runcheck',
    'version': '0.1.2',
    'description': 'An application to parse Dockerfiles and determine whether all called binaries are able to run (are either present in the base image or are installed by a package manager)',
    'long_description': '\n<a name="readme-top"></a>\n\n\n<!-- PROJECT SHIELDS -->\n<!--\n*** I\'m using markdown "reference style" links for readability.\n*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).\n*** See the bottom of this document for the declaration of the reference variables\n*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.\n*** https://www.markdownguide.org/basic-syntax/#reference-style-links\n-->\n<!--[![Issues][issues-shield]][issues-url]\n[![LinkedIn][linkedin-shield]][linkedin-url]-->\n\n\n\n<!-- PROJECT LOGO -->\n<br />\n<div align="center">\n  <a href="https://github.com/pfaaj/docker-runcheck">\n    <img src="images/logo.png" alt="Logo" width="400" height="400">\n  </a>\n\n  <h3 align="center">Docker runcheck</h3>\n\n  <p align="center">\n    Check wheter required binaries are available in the used docker image without having to first run an expensive and long docker build.\n    <br />\n    ·\n    <a href="https://github.com/pfaaj/docker-runcheck/issues">Report Bug</a>\n    ·\n    <a href="https://github.com/pfaaj/docker-runcheck/issues">Request Feature</a>\n  </p>\n</div>\n\n\n\n<!-- TABLE OF CONTENTS -->\n<details>\n  <summary>Table of Contents</summary>\n  <ol>\n    <li>\n      <a href="#about-the-project">About The Project</a>\n    </li>\n    <li>\n      <a href="#getting-started">Getting Started</a>\n    </li>\n    <li><a href="#usage">Usage</a></li>\n    <li><a href="#roadmap">Roadmap</a></li>\n    <li><a href="#contributing">Contributing</a></li>\n    <li><a href="#license">License</a></li>\n    <li><a href="#contact">Contact</a></li>\n    <li><a href="#acknowledgments">Acknowledgments</a></li>\n  </ol>\n</details>\n\n\n\n<!-- ABOUT THE PROJECT -->\n## About The Project\n\n+ Run docker-runcheck to validate your Dockerfile before attempting time-intensive docker builds. \n\n+ docker-runcheck works as follows:\n  + contructs one or more containers based on the mentioned image\n  + docker image is downloaded if not present\n  but it is not built.\n  + export image as tar file and compile a list of the available binaries in the image\n  + compile a list of any binaries mentioned in a RUN command that are  missing from the image or are used before being installed by a package manager.\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n\n\n<!-- GETTING STARTED -->\n## Getting Started\n\n\nWe need the docker sdk and the dockerfile library\n \n  ```sh\n  pip install -r requirements.txt \n  ```\n\n\n</br>\n\n\n<!-- USAGE EXAMPLES -->\n### Usage\n\nYou can run docker-runcheck with:\n\n  ```sh\n  python docker-runcheck.py\n  ```\n\n![](images/runcheck.gif)\n\n\n\n\n\n<!-- ROADMAP -->\n## Roadmap\n\n- [] Detect binary is installed by super package (e.g. build-essential)\n\n\n<!--See the [open issues](https://github.com/pfaaj/docker-runcheck/issues) for a full list of proposed features (and known issues).-->\n\n\n<!-- For apt stuff, package info\n\ngit clone https://salsa.debian.org/apt-team/python-apt\ncd python-apt\nsudo apt install libapt-pkg-dev\npython setup.py build\n\nor alternatively https://help.launchpad.net/API/launchpadlib\n\nor https://sources.debian.org/doc/api/ -> examples \nhttps://sources.debian.org/api/info/package/davfs2/1.5.2-1/ \nhttps://sources.debian.org/api/src/cowsay/3.03+dfsg1-4/cows/\n-->\n\n \n## Contributing\n\nContributions are **greatly appreciated**.\n\nIf you have a suggestion to make this project better, please fork the repo and create a pull request. \nDon\'t forget to give the project a star! Thanks!\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/SuperAmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some Super Amazing Feature\'`)\n4. Push to the Branch (`git push origin feature/SuperAmazingFeature`)\n5. Open a Pull Request\n\n</br>\n\n<!-- LICENSE -->\n## License\n\nDistributed under the MIT License. \n\n\n</br>\n\n<!-- CONTACT -->\n## Contact\n\nPaulo Aragao - paulo.aragao.dev@gmail.com\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n\n\n\n<!-- ACKNOWLEDGMENTS \n## Acknowledgments\n\n\n<p align="right">(<a href="#readme-top">back to top</a>)</p>\n-->\n\n\n<!-- MARKDOWN LINKS & IMAGES -->\n<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->\n[contributors-shield]: https://img.shields.io/github/contributors/pfaaj/docker-runcheck.svg?style=for-the-badge\n[contributors-url]: https://github.com/pfaaj/docker-runcheck/graphs/contributors\n[forks-shield]: https://img.shields.io/github/forks/pfaaj/docker-runcheck.svg?style=for-the-badge\n[forks-url]: https://github.com/pfaaj/docker-runcheck/network/members\n[stars-shield]: https://img.shields.io/github/stars/pfaaj/docker-runcheck.svg?style=for-the-badge\n[stars-url]: https://github.com/pfaaj/docker-runcheck/stargazers\n[issues-shield]: https://img.shields.io/github/issues/pfaaj/docker-runcheck.svg?style=for-the-badge\n[issues-url]: https://github.com/pfaaj/docker-runcheck/issues\n[license-shield]: https://img.shields.io/github/license/pfaaj/docker-runcheck.svg?style=for-the-badge\n[license-url]: https://github.com/pfaaj/docker-runcheck/blob/master/LICENSE.txt\n[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555\n[linkedin-url]: https://linkedin.com/in/paulo-aragao\n[product-screenshot]: images/screenshot.png\n[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white\n',
    'author': 'Paulo Aragao',
    'author_email': 'paulo.aragao.dev@gmail.com',
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
