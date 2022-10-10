# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['my_package']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'my-package-tomergabay',
    'version': '0.1.0',
    'description': 'Template for a professional (open source) Python package.',
    'long_description': "[![Version](https://img.shields.io/pypi/v/my-package-tomergabay)](https://pypi.org/project/my-package-tomergabay/)\n![](https://img.shields.io/github/license/sTomerG/my-package)\n![](https://img.shields.io/pypi/pyversions/my-package-tomergabay)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# The template for a professional Python Package\n\nIn October 2022 I wrote [this](link) Medium article in which I explain step-by-step on how to create a professional Python Package. To make it extra easy for everyone I've also created [this](https://github.com/sTomerG/my-package) repository which can be used as a template.\n\n## Contents\n\n- A *src/* folder with example code.\n- A *pyproject.toml* with all the necessary dependencies specified.\n- A *tests/* folder with example tests, using pytest and Hypothesis.\n- Pre-commit hooks for *Black*, isort and flake8.\n- A workflow [*test-package.yaml*](.github/workflows/test-package.yaml) which automates testing with Github Actions for different Python versions (optionally) on different Operating Systems, using caching to speed up the process.\n- A *docs/* folder with a Sphinx project template for ReadTheDocs which can easily be auto-generated with one command, including automatic API documentation of all code in *src/*.\n\n## Usage\n\nTo convert this package template to your own package please take the following steps:\n\n1. Clone this repository: `git clone https://github.com/sTomerG/my-package.git`\n\n2. Create a virtual environment using pyenv and pyenv-virtualenv or `python3 -m venv venv`\n\n3. Activate the virtual environment using using pyenv or `source venv/bin/activate`\n\n4. Upgrade pip and install poetry: `pip install --upgrade pip && pip install poetry`\n\n5. Activate the poetry venv with `poetry shell` if you're using pyenv.\n   \n6. Change some fields of `[tool.poetry]` in [*pyproject.toml*](pyproject.toml), e.g. the project name, in field `name` and `packages`\n\n7. Change the name of the *my_package/* folder in *src/* to the new name of your package (use underscores instead of hyphens here).\n\n8. Change the top fields in [*docs/source/conf.py*](docs/source/conf.py), e.g. `project` to the same value as `name` in *pyproject.toml*. \n\n9. Reinstall the package with `poetry install`\n\n10.  Change the `my_package` part in  `from my_package.calc import` to the name of the folder you chose in step 6 in [*tests/test_calc/test_square.py*](tests/test_calc/test_square.py) and in [*docs/source/notebooks/usage.ipynb*](docs/source/notebooks/usage.ipynb).\n\n11. Check if the tests are still running correctly with working with `poetry run pytest` \n\n12. Rebuild the docs with `poetry run sphinx-autobuild docs/source docs/build/html`\n\n13. Edit in the top of the [README](README.md) the links\n\n## Note\n\nWhen you add dependencies with `poetry add`, make sure to also run `poetry export --with doc -f requirements.txt --output docs/rtd_requirements.txt` to update the requirements file for the ReadTheDocs.\n",
    'author': 'Tomer Gabay',
    'author_email': 'tomergabay001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
