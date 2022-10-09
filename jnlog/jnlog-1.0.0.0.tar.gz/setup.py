from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='jnlog',
    version='1.0.0.0',
    packages=find_packages(),

    description='jnlog simple colored text logger for python',    
    #long_description_content_type="text/markdown",    
    long_description=open('README.rst', 'rb').read().decode(),    
    url="https://gitlab.com/seeklay/jnlog",
    author='seeklay'
)