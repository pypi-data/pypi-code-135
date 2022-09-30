#!/usr/bin/env python
# -*- coding: utf-8 -*-

MODULE_VERSION = "1.0.0"
PACKAGE_NAME = "aics_bead_alignment_core"

"""The setup script."""

from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup_requirements = [
    "black",
    "flake8 ~= 3.9",
    "isort ~= 5.9",
    "mypy ~= 0.910",
    "pre-commit ~= 2.13",
    "pytest-runner ~= 5.2",
]

test_requirements = [
    "pytest ~= 6.2",
    "pytest-runner ~= 5.3",
    "pytest-cov ~= 2.12",
    "pytest-raises ~= 0.11",
]

dev_requirements = [
    *setup_requirements,
    *test_requirements,
    "bump2version ~= 1.0.1",
    "twine ~= 3.4.2",
    "wheel ~= 0.37.0",
    # Documentation generation
    "Sphinx ~= 4.1.2",
    "furo == 2021.8.17b43",  # Third-party theme (https://pradyunsg.me/furo/quickstart/)
    "m2r2 ~= 0.3.1",  # Sphinx extension for parsing README.md as reST and including in Sphinx docs
]

requirements = ["aicsimageio[czi] ~= 4.4", "numpy ~= 1.21", "scikit-image ~= 0.18"]

extra_requirements = {
    "setup": setup_requirements,
    "test": test_requirements,
    "dev": dev_requirements,
    "all": [
        *requirements,
        *dev_requirements,
    ],
}

setup(
    author="AICS Software",
    author_email="brian.whitney@alleninstitute.org",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: Free for non-commercial use",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="A uitlity package containing functions to align bead images ",
    install_requires=requirements,
    extras_require=extra_requirements,
    setup_requires=setup_requirements,
    entry_points={
        "console_scripts": [
            "bead_align = aics_bead_alignment_core.bin.align_cli:main".format(
                PACKAGE_NAME
            )
        ],
    },
    license="Allen Institute Software License",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="aics_bead_alignment_core",
    name="aics_bead_alignment_core",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*"]),
    python_requires=">=3.8",  # This is driven by aicsimageio constraints
    url="https://github.com/BrianWhitneyAI/aics_bead_alignment_core",
    # Do not edit this string manually, always use bumpversion
    # Details in CONTRIBUTING.rst
    test_suite="aics_bead_alignment_core/tests",
    tests_require=test_requirements,
    version="0.0.0",
    zip_safe=False,
)
