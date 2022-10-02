from setuptools import setup, find_packages
from setuptools.command.install import install
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        print('run custominstall successfully!')


setup(
        name='MCsecdemo', #package name
        version='1.0.5',
        description='A sample Python project, do not download it!',
        author='MC Download',
        license='MIT',
        packages=find_packages(),
        cmdclass={'install': CustomInstall},
        author_email='zhuzhuzhuzai@gmail.com',
        install_requires=[
                "Alexsecdemo==1.3.4",
                "Bfixsecdemo==1.0.1",
        ],
)
