# python setup.py sdist bdist_wheel
#https://www.freecodecamp.org/news/build-your-first-python-package/
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="sdss_module",
        version=VERSION,
        author="Shaunak Dhande",
        author_email="shaunak.dhande@innoplexus.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'first package'],
        classifiers = [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
                        ]
)
