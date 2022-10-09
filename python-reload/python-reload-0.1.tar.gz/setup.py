from setuptools import setup

with open("README.md", "r") as readme_file:
	readme = readme_file.read()

version = "0.1"

long_description = "A module that allows you to make changes to a running python script and reload it"

setup(
	name="python-reload",
	version=version,
	license='MIT',
	author="Feb",
	author_email="drons_dron@mail.ru",

	description = long_description,
	long_description=readme,
	long_description_content_type = 'text/markdown',

	url = "https://github.com/febdaynik/PyReload",

	packages=["pyreload"],
)

