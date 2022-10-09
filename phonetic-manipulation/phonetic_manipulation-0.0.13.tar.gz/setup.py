from setuptools import setup, find_packages
import codecs
import os

VERSION = "0.0.13"
DESCRIPTION = "A package for manipulating phonetic transcriptions"
LONG_DESCRIPTION = """This package is mainly serves the function of taking phonetic transcriptions and converting it to IPA from X-SAMPA or SAMPA and vice versa.
You can provide your own list of phones for the language you're working with in order to condense the data. No matter what, it will provide you all phones organized
by their feature categories."""

setup(
	name="phonetic_manipulation",
	version=VERSION,
	author="Denny O'Shea",
	author_email="denjaminpip@gmail.com",
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	packages=find_packages(),
	install_requires=['pandas'],
	keywords=['python', 'phonetics', 'phonology', 'computational linguistics', 'IPA conversion'],
	include_package_data=True,
	package_data={'':['data/*.csv']},)