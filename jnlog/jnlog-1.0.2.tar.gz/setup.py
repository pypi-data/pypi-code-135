from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='jnlog',
    version='1.0.2',    
    py_modules=['jnlog'],

    description='jnlog simple colored text logger for python',        
    long_description=open('README.rst', 'rb').read().decode(),    
    url="https://gitlab.com/seeklay/jnlog",
    author='seeklay'    
)