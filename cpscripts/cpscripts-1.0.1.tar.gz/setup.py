# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:14:27 2022

@author: akhan
"""

from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()
  
long_description = 'Python package for using cellpose scripts'
  
setup(
        name ='cpscripts',
        version ='1.0.1',
        author ='Arif Khan',
        author_email ='arif.khan@embl.com',
        url ='https://git.embl.de/grp-cba/embryo-3D-chromatin-tracing-workflow/-/tree/main/code/python/py-cellpose',
        description ='Python cellpose.',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        entry_points ={
            'console_scripts': [
                'cellpose_predict = pycellpose.cellpose_predict:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords ='cellpose python package',
        install_requires = requirements,
        zip_safe = False
)