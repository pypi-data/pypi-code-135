import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = "example_package_dw",
        version = "0.0.1",
        author = "DW Shin",
        author_email = "dongwookshin@hotmail.com",
        description = ("Example package from DW"),
        liscense = "BSD",
        keywords = "example python package",
        url = "http://packages.python.org/example_package_dw",
        packages = find_packages('src'),
        package_dir = {'': 'src'},
        long_description = read('README.md'),
)
