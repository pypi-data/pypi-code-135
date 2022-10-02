from imp import find_module
from pathlib import Path
import setuptools

setuptools.setup(
    name="ismailpdf",
    version=1.0,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(
        exclude=["tests", "data"]
    )  # to be excluded
)
