# Read contents README
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

from setuptools import setup
setup(
    name="EarthMC",
    version="2.1.0",
    description="Provides data on people, places and more on the EarthMC Minecraft server.",
    author="Owen3H",
    license="MIT",
    url="https://github.com/EarthMC-Toolkit/EarthMC-Py",
    packages=["Classes"],
    py_modules=["__init__", "Utils"],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=False
)

# Build dist using this: python setup.py sdist bdist_wheel
# Upload using this: python -m twine upload dist/*