import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    name="argparsejson",
    version="0.0.6",
    author="Jon Prentice",
    author_email="jon77p@gmail.com",
    description="A library that allows converts JSON into an argparse ArgumentParser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jon77p/argparsejson",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=["jsonschema"],
    include_package_data=True
)
