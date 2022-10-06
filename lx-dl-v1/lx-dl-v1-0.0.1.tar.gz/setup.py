from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'LayerX Data Lake Python SDK'
LONG_DESCRIPTION = 'Python API Client to interact with layerx datalake'

# Setting up
setup(
    name="lx-dl-v1",
    version=VERSION,
    author="layerx",
    author_email="<annotation.manager.dev@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(include=['datalake']),
    install_requires=['requests', 'uuid'],
    keywords=['python', 'datalake', 'datasetsync', 'ai', 'annotation', 'layerx', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
