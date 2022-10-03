import setuptools
from setuptools import setup

version = {}
with open("h2cow/_version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    version=version["__version__"],
    name="h2cow",
    license = "MIT",
    description="Monitoring drinking behaviour of animals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniël M. van Herwijnen",
    author_email="danielvh8@gmail.com",
    url = "https://github.com/danielvh8/Master-Research-Project-2022",
    packages=setuptools.find_packages(),
    python_requires="==3.10.4",
    install_requires=[
        "click==8.1.3",
        "deeplabcut==2.2.2",
        "numpy>=1.18.5",
        "opencv_contrib_python==4.6.0.66",
        "ruamel.yaml>=0.15.0",
        "setuptools<60"
    ],
    entry_points={
        'console_scripts':{
            'h2cow = h2cow.cli:main'
        }
    },)

    
