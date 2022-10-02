# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 16:01:03 2022

@author: Shanyu and Pranav
"""

from setuptools import setup, find_packages

classifiers = [ 
    'Development Status :: 5 - Production/Stable',
    'Intended Audience:: Education',
    'Operating System:: Microsoft :: Windows:: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]
setup(
   name='Project_Grid_lock',
   version='1.0',
   description='A module that allows the use of positions in images as a password',
   license="MIT",
   long_description= open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
   author='Shanyu Dabbiru, Pranav Reddy Dumpa',
   author_email='project.gridlock.2022@gmail.com',
   url="",
   packages= find_packages(),  #same as name
   install_requires=['tempfile', 'matplotlib', 'PIL', 'pylab', 'io', 'numpy', 'base64', "time" ], #external packages as dependencies
   key_words = "password"

)