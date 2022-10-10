import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = "pygame_light",
	version = "0.0.1-dev",
	author = "Ben Landon",
	description = "A simple 2D light library for pygame.",
	long_description = read("README.md"),
	long_description_content_type = "text/markdown",
	liscense = "MIT",
	keywords = "pygame light",
	url = "https://github.com/https123456789/pygame_light",
	packages = [ "pygame_light" ],
	classifiers = [
		"Development Status :: 2 - Pre-Alpha",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent"
	]
)