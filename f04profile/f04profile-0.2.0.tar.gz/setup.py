import re
from pathlib import Path

from setuptools import setup


def get_version():
    VERSIONFILE = "__init__.py"
    initfile_lines = open(VERSIONFILE, "rt").readlines()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    for line in initfile_lines:
        mo = re.search(VSRE, line, re.M)
        if mo:
            return mo.group(1)
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))


long_description = Path("README.rst").read_text()


setup(
    author="Nicolas Cordier",
    author_email="nicolas.cordier@numeric-gmbh.ch",
    python_requires=">=3.8",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    name="f04profile",
    version=get_version(),
    py_modules=["f04profiling"],
    install_requires=["snakeviz"],
    entry_points={"console_scripts": ["f04prof=f04profiling:main"]},
)
