from distutils.core import setup
from setuptools import find_packages
import os

try:
    with open(os.path.join(os.getcwd(), 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = 'Gitlab Tools Library'
setup(

    # Project name:
    name='Gitlab Tools',

    # Packages to include in the distribution:
    packages=find_packages(','),

    # Project version number:
    version='0.0.1',

    # List a license for the project, eg. MIT License
    license='',

    # Short description of your library:
    description='Gitlab Tools for gitlab API',

    # Long description of your library:
    long_description=long_description,
    long_description_content_type='text/markdown',

    # Your name:
    author='emilian.craciun',

    # Your email address:
    author_email='emilian.craciun9@yahoo.com',

    # Link to your github repository or website:
    url='https://gitlab.com/ecraciun/gitlab-tools',

    # Download Link from where the project can be downloaded from:

    # List of keywords:
    keywords=[],

    # List project dependencies:
    install_requires=[
        'git',
        'python-gitlab',
        'pyyaml'
    ],

# https://pypi.org/classifiers/
    classifiers=[]
)
