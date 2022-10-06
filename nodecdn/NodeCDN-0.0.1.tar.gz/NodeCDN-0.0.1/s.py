from setuptools import setup, find_packages

setup(
    name="NodeCDN",
    version="0.0.1",
    description="Node CDN for Python.",
    long_description=" Original GitHub repository here: [git](https://github.com/WWEMGamer2/NodeCDN)",
    author="Eric",
    author_email="justaneric.c@gmail.com",
    packages=find_packages(),
    entry_points ={
        'console_scripts': [
            'nodecdn = commandLine.m:main'
        ]
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires = []
)