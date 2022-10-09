from distutils.core import  setup
import setuptools
packages = ['xyxt']# 唯一的包名
setup(name='xyxt',
    version='1.0',
    author='hyg',
    packages=packages, 
    package_dir={'requests': 'requests'},)
