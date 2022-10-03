import setuptools
from setuptools import setup
import subprocess

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

version = {}
with open("h2cow/_version.py") as fp:
    exec(fp.read(), version)

# version = (
#     subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
#     .stdout.decode("utf-8")
#     .strip()
# )

# with open("h2cow/_version.py", "w", encoding="utf-8") as fh:
#     fh.write("%s\n" % version)

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
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts':{
            'h2cow = h2cow.cli:main'
        }
    },)

    
