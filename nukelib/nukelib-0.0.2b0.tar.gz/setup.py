from setuptools import setup, find_packages
import requests

readme = requests.get("https://raw.githubusercontent.com/aniko33/NukeLib/main/README.md").text

VERSION = '0.0.2_b'
DESCRIPTION = 'Discord accounts nukker lib'
LONG_DESCRIPTION = readme

# Setting up
setup(
    name="nukelib",
    version=VERSION,
    author="Aniko (Aniko#0104)",
    author_email="<mail@aniko.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=['python', 'discord api', 'discord nuke', 'nuke', 'discord', 'discord token'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
