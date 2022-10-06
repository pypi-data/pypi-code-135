# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['_wheel2deb']

package_data = \
{'': ['*']}

modules = \
['wheel2deb']
install_requires = \
['Jinja2>=3,<4',
 'PyYAML>=6,<7',
 'attrs>=20.1',
 'colorama',
 'dirsync',
 'packaging',
 'pkginfo',
 'setuptools',
 'wheel']

extras_require = \
{'pyinstaller': ['pyinstaller==5.4.1']}

entry_points = \
{'console_scripts': ['wheel2deb = wheel2deb:main']}

setup_kwargs = {
    'name': 'wheel2deb',
    'version': '0.7.0',
    'description': 'Python wheel to debian package converter',
    'long_description': '## wheel2deb\n\n![cicd](https://github.com/upciti/wheel2deb/actions/workflows/cicd.yml/badge.svg)\n[![codecov](https://codecov.io/gh/upciti/wheel2deb/branch/main/graph/badge.svg)](https://codecov.io/gh/upciti/wheel2deb)\n[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![PyPI version shields.io](https://img.shields.io/pypi/v/wheel2deb.svg)](https://pypi.python.org/pypi/wheel2deb/)\n[![Downloads](https://static.pepy.tech/personalized-badge/wheel2deb?period=total&units=international_system&left_color=blue&right_color=green&left_text=Downloads)](https://pepy.tech/project/wheel2deb)\n\n`wheel2deb` is a python wheel to debian package converter. It takes a list of wheels as input and produces a list of debian binary CPython packages (those prefixed with python- or python3-).\n\n[![asciicast](https://asciinema.org/a/249779.svg)](https://asciinema.org/a/249779)\n\n## Quick Example\n\nThe following shows how to convert numpy and pytest, along with their dependencies into a list of debian packages:\n\n```sh\n# Download (and build if needed) pytest, numpy and their requirements\npip3 wheel pytest numpy\n# Convert all wheels to debian source packages\nwheel2deb --map attrs=attr\n# Call dpkg-buildpackages for each source package\nwheel2deb build\nls -l output/*.deb\n# Install generated packages\ndpkg -i output/*.deb\n# Run pytest on numpy\npython3 -c "import numpy; numpy.test()"\n```\n\n## Project scope\n\n- Python 2.7 and 3\n- CPython only for now\n- support for non pure python wheels\n- support debian architectures all, armhf, amd64, i686\n- tested on jessie, stretch, buster so far, ubuntu should also work\n\n## Requirements\n\n`wheel2deb` uses python3-apt to search for debian packages, dpkg-shlibdeps to calculate shared library dependencies and apt-file to search packages providing shared library dependencies. `wheel2deb build` requires the usual tools to build a debian package:\n\n```sh\napt update\napt install python3-apt apt-file dpkg-dev fakeroot build-essential devscripts debhelper\napt-file update\n```\n\nIf you want to cross build packages for ARM, you will also need to install `binutils-arm-linux-gnueabihf`.\n\nConverting pure python wheels, don\'t actually requires apt-file and dpkg-dev.\n\nKeep in mind that you should only convert wheels that have been built for your distribution and architecture. wheel2deb will not warn you about ABI compatibility issues.\n\n## Installation\n\nwheel2deb is available from [pypi](https://pypi.org/project/wheel2deb/):\n\n```shell\npipx install wheel2deb\n```\n\n## Features\n\n- guess debian package names from wheel names and search for them in the cache\n- search packages providing shared library dependencies for wheels with native code\n- handle entrypoints and scripts (those will be installed in /usr/bin with a proper shebang)\n- try to locate licence files and to generate a debian/copyright file\n\n## Options\n\nUse `wheel2deb --help` and `wheel2deb build --help` to check all supported options\n\n| Option                    | Description                                                                                                                                                                                        |\n| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| -v                        | Enable debug logs.                                                                                                                                                                                 |\n| -x                        | List of search paths where to look for python wheels. Defaults to current directory. Not recursive.                                                                                                |\n| -o                        | Output directory where debian source packages will be produced. Defaults to ./output                                                                                                               |\n| -i                        | List of wheel names to convert. By default all found wheels are included.                                                                                                                          |\n| --python-version          | cpython version on the target debian distribution. Defaults to platform version (example: 3.4).                                                                                                    |\n| --map                     | list of string pairs to explicitely map python dist names to debian package names. For instance: "--map foo:bar attrs:attr" will tell wheel2deb to map foo to python-bar and attrs to python-attr. |\n| --depends                 | List of additional debian dependencies.                                                                                                                                                            |\n| --epoch                   | Debian package epoch. Defaults to 0.                                                                                                                                                               |\n| --revision                | Debian package revision. Defaults to 1.                                                                                                                                                            |\n| --ignore-entry-points     | Don\'t include the wheel entrypoints in the debian package.                                                                                                                                         |\n| --ignore-upstream-version | Ignore version specifiers from wheel requirements. For instance, if foo requires bar>=3.0.0, using this option will produce a debian package simply depending on bar instead of "bar (>= 3.0.0)".  |\n\n## Bugs/Requests\n\nPlease use the [GitHub issue tracker](https://github.com/upciti/wheel2deb/issues) to submit bugs or request features.\n\n## License\n\nCopyright Parkoview SA 2019-2023.\n\nDistributed under the terms of the [MIT](https://github.com/upciti/wheel2deb/blob/master/LICENSE) license, wheel2deb is free and open source software.\n',
    'author': 'Upciti',
    'author_email': 'support@upciti.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/upciti/wheel2deb',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
