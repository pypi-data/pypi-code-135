from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'Encrypt strings to the Bee Movie script and back'
LONG_DESCRIPTION = 'If you want to encrypt your strings and want to have the Bee Movie script in your code than this is the Python package for you! With this package you can encrypt strings to the first part of the Bee Movie scipt and decrypt it back. Go to https://github.com/Agent-Kwabbel/Beecrypted for more information.'

# Setting up
setup(
    name="beencrypted",
    version=VERSION,
    author="Agent-Kwabbel (Fabe Stuffken)",
    description=DESCRIPTION,
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=[],
    keywords=['python', 'bee', 'movie', 'bee movie', 'encryption', 'decryption', 'meme'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)