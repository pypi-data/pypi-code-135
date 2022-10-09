# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mdatpy',
 'mdatpy.bin',
 'mdatpy.bin.datasets',
 'mdatpy.bin.datasources',
 'mdatpy.bin.generators',
 'mdatpy.bin.graph',
 'mdatpy.bin.iterators',
 'mdatpy.bin.tensorflow_train',
 'mdatpy.bin.tensorflow_train.layers',
 'mdatpy.bin.tensorflow_train.losses',
 'mdatpy.bin.tensorflow_train.networks',
 'mdatpy.bin.tensorflow_train.utils',
 'mdatpy.bin.tensorflow_train_v2',
 'mdatpy.bin.tensorflow_train_v2.dataset',
 'mdatpy.bin.tensorflow_train_v2.layers',
 'mdatpy.bin.tensorflow_train_v2.networks',
 'mdatpy.bin.tensorflow_train_v2.utils',
 'mdatpy.bin.transformations',
 'mdatpy.bin.transformations.intensity',
 'mdatpy.bin.transformations.intensity.np',
 'mdatpy.bin.transformations.intensity.sitk',
 'mdatpy.bin.transformations.spatial',
 'mdatpy.bin.utils',
 'mdatpy.bin.utils.io',
 'mdatpy.bin.utils.landmark',
 'mdatpy.bin.utils.landmark.visualization',
 'mdatpy.bin.utils.segmentation']

package_data = \
{'': ['*']}

install_requires = \
['itk==5.3rc4',
 'matplotlib>=3.6.0,<4.0.0',
 'nekton==0.2.6rc2',
 'networkx>=2.8.7,<3.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'tensorflow-gpu>=2.10.0,<3.0.0',
 'tensorflow>=2.10.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'mdatpy',
    'version': '0.0.4rc0',
    'description': 'A pypi release of the MDAT',
    'long_description': '# poetry_pypi_template\n\n> A minimal template for creating a pypi package using poetry and github actions\n\nThis template allows the creation of python projects managed by poetry to be submitted to PyPi. All the github actions have been setup too. The github actions run tests on every push and also creates and new pacakage and pushes to the pypi when a merge happens to the release branch.\n\nJust follow the seteps below for an hassle free setup of the project.\n\n## Create from the Project Template\n\n- [Click here](https://github.com/a-parida12/poetry_pypi_template/generate) to create a new repo (you need to be logged in to GitHub for this link to work), and follow the instructions to create a new repo from this template.\n- `git clone` your new repo\n\n## Install Poetry in your Environment\n\n- activate your environment.\n- install poetry `python -m  pip install poetry`\n\n## Update the Project Toml\n\n- Insert/Update the values in the `pyproject.toml` under `tool.poetry`\n- Dont forget to update the desired python version under the `tool.poetry.dependencies`\n- Dont forget to modify the release branch under `tool.semantic_release` (assumption is `main` is the release branch)\n- add project dependancies. eg - if you want `numpy` as an dependancy simply run `poetry add numpy`\n- install the dependancies by running `poetry install`\n- More information on setting up a [project with poetry](https://realpython.com/dependency-management-python-poetry/)\n\n## Write Code for your python package\n\n- Create a project folder. eg. `hapi_pypi` here\n- add all the code/implemenations in the folder.\n\n## Implement the Tests\n\n- Check the functionality of the project folder by implementing tests.\n- Implement tests in the `tests` folder.\n- All the tests should pass when you run the command `poetry run pytest tests/`\n- Details on how to implement [tests with pytest](https://realpython.com/pytest-python-testing/).\n\n## Github Actions Configuration\n\n- all the github actions are defined in the `.github/workflows` folder\n- setup the `test.yml`. Update the env variables according to the project setup before. The default coverage limit is set to 90% ie the test will fail below the coverage of 90.\n\n``` yaml\nenv:\n  PYTHON_VERSION: "3.8.5"\n  PROJECT_FOLDER: hapy_pypi\n  TEST_FOLDER: tests\n  COVERAGE_LIMIT: 90\n```\n\n- setup the similar env variables in `release.yml` as well.\n\n## Setup Secrets\n\n### Pypi Creds\n\nThese secrets are used to push releases to the pypi repository.\n\n- Generate a pypi [api token](https://pypi.org/help/#apitoken)\n- [Set Repo Secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md)\n- Add `PYPI_USER` as `__token__`\n- Add `PYPI_TOKEN` as the token from above step including the `pypi-` prefix\n\n### Github Token\n\nThis secret is required to generate the `CHANGELOG.MD` and update the version by SemRel.\n\n- Generate a [github token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)\n- [Set Repo Secrets](https://github.com/Azure/actions-workflow-samples/blob/master/assets/create-secrets-for-GitHub-workflows.md)\n- Add `GH_TOKEN` as the token from github.',
    'author': 'Abhijeet Parida',
    'author_email': 'abhijeet.parida@tum.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/a-parida12/MDAT',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<3.11.0',
}


setup(**setup_kwargs)
