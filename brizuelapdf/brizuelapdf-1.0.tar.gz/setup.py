import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='brizuelapdf', version='1.0', long_description=long_description, author='Juan Brizuela',
                 packages=setuptools.find_packages(exclude=["test", "data"]))
