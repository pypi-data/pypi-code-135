import os
import re
from codecs import open
from os import path

from setuptools import find_packages, setup

COMPANY_NAME = "chalk"
NAME = "chalk"
DESCRIPTION = f"Python wrapper for Chalk's CLI"

repo_root = path.abspath(path.dirname(__file__))
LONG_DESCRIPTION = open(os.path.join(repo_root, "README.md"), "r").read()
VERSIONFILE = os.path.join(repo_root, "_version.py")
mo = re.search(
    r"^__version__ = ['\"]([^'\"]*)['\"]",
    open(VERSIONFILE, "rt").read(),
    re.M,
)

assert mo is not None, f"Unable to find version string in {str(VERSIONFILE)}"

version = mo.group(1)
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    version=version,
    name="chalk-harness",
    author="Chalk AI, Inc.",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    python_requires=">=3.8.0",
    url="https://chalk.ai",
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
    include_package_data=True,
    package_data={"chalkharness": ["py.typed"]},
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    setup_requires=[
        "setuptools_scm",
    ],
)
