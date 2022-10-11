from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = "pyterri",
    version = "0.1.1",
    description = "A simple python package for getting territorial.io player and clan data",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/theotherhades/pyterri",
    author = "theotherhades",
    author_email = "theotherhades1@gmail.com",
    license = "BSD 2-clause",
    packages = ["pyterri"],
    install_requires = ["requests"]
)