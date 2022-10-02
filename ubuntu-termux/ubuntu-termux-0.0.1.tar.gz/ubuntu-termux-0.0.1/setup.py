from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='ubuntu-termux',
    version='0.0.1',
    url='https://github.com/perseu912/ubuntu-termux',
    license='GPLv3',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='ubuntu termux linux',
    description=u'install and use the Ubuntu on the Termux',
    packages=find_packages(),
    install_requires=['tqdm','request'],)
