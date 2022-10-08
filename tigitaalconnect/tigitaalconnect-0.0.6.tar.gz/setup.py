from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_desciption = '\n' + fh.read() + '\n\n' + open('CHANGELOG.txt').read()

VERSION = '0.0.6' 
DESCRIPTION = 'Tigitaal\'s Official Python Package to connect with TigitaalAPI'

# Setting up
setup(
        name="tigitaalconnect", 
        version=VERSION,
        author="Ninjagor",
        author_email="ninjagor.spoon@gmail.com",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=long_desciption,
        packages=find_packages(),
        install_requires=[
            'requests'
        ],
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)