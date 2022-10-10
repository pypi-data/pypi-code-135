import re
from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='my_pkg_setuptools_binlecode',
    version='0.1.2',
    author='Bin Le',
    author_email='bin.le.code@gmail.com',
    # automatically detect python files
    description='A small test package by setuptools',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/binlecode/example-python-setuptools',
    license='MIT',
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        'License :: OSI Approved :: MIT License',
        "Topic :: Software Development",
    ],
    packages=find_packages(include=['my_pkg'], exclude=['tests']),
    # set to True only when data files are needed
    include_package_data=False,
    # list all packages that must be installed before your package can work
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    test_suite='tests'
)
