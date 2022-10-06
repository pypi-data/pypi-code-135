import os
from setuptools import setup
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='fistnd',
      version='0.0.4',
      description='FIST-nD, Fast Imputation of Spatially-resolved transcriptomes by graph-regularized Tensor completion in n-Dimensions imputes 3D as well as 2D spatial transcriptomics data.',
      author='Rui Kuang',
      author_email='kuang@umn.edu',
      url='https://github.com/kuanglab/FIST-nD',
    install_requires=required)