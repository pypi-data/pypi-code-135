# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['example_package']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['demo-example-package = example_package:main']}

setup_kwargs = {
    'name': 'package-installation-test',
    'version': '1.0.0',
    'description': 'A test package for verifying which Python is in use and where `pip` is installing packages',
    'long_description': '# `package-installation-test`\n\nThis package is designed to verify that you can successfully install Python packages from PyPI using `pip`, and subsequently use them. In particular, it is meant to test that you are installing packages **to the correct Python installation**. It is written to complement a question on Stack Overflow about this problem, to allow for testing the solutions offered there.\n\n## Installation\n\nInstall this package from PyPI using `pip install package-installation-test`. Alternately, clone the repository, navigate to the root of the repository, and then use `pip install .` to install it. Note the `.` at the end of the latter command (specifying the current directory).\n\nNote carefully that the installed package has a **different name** from the name used on PyPI and in this repository; although we install `package-installation-test` (notice that this is not a valid Python identifier anyway), code will refer to the package as `example_package`.\n\n## Command-line use\n\nOnce installed, you should be able to "run" the package as a module, using `python -m example_package`.\n\nInstallation will also create a wrapper executable called `demo-example-package`, which you can run at the command line by that name.\n\nEither of these options should print a diagnostic message that looks like:\n```\nVersion 1.0.0 of example_package successfully installed.\nThe source code is in <...>.\n```\nwhere the `<...>` is replaced by the actual path where the code was installed.\n\n## API\n\nYou can verify that the code is usable as a package by `import`ing it from the interactive prompt:\n```\n>>> import example_package\n>>>\n```\nThis provides two functions:\n\n`main` - prints the same message as before.\n\n`home` - returns the path to where the code was installed, as a `pathlib.Path` instance.\n\nBoth of these functions take no arguments.\n\n## Troubleshooting\n\nIf the above steps don\'t work as advertised, the problem is **almost certainly** that `pip` installed to a different installation of Python than the one you are trying to use. (If the `demo-example-package` doesn\'t work, that\'s because you installed to a Python installation that isn\'t the first one on the `PATH`. \n\nPlease read the corresponding question and answer on Stack Overflow to understand how to solve the problem.',
    'author': 'Karl Knechtel',
    'author_email': 'karl.a.knechtel@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zahlman/package-installation-test',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
