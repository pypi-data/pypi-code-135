from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.2'
DESCRIPTION = 'Python GUIS made easy'
LONG_DESCRIPTION = 'Python GUIS made easy.'

setup(
    name="PyOptionPane",
    version="0.17",
    author="yavda1",
    description="Python GUIs made easy",
    packages=find_packages(),
    install_requires=['tk'],
    keywords=['python', 'tkinter', 'gui'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
