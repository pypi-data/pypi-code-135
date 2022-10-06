""" Setup instructions for nt3-lib """
from setuptools import find_packages, setup

install_requires = ["pyyaml"]

setup(
    name="nt3core",
    description="Core Library for NovaTouch 3",
    author="novacom software GmbH",
    version="0.0.01",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=install_requires,
)
