from platform import python_revision
from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='my_pkg_setuptools_binlecode',
    version='0.0.2',
    author='Bin Le',
    author_email='bin.le.code@gmail.com',
    packages=find_packages(include=['my_pkg']),
    description='A small test package by setuptools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    license='MIT',
    python_requires='>=3.8',
    # set to True only when data files are needed
    include_package_data=False,
    # list all packages that must be installed before your package can work
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite='tests'
)