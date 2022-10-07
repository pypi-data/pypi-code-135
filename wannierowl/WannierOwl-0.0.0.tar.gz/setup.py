from setuptools import setup, find_packages
from WannierOwl import __version__

__version__ = __version__

with open('README.rst', 'r') as file:
    long_description = ''
    for line in file:
        long_description += line

setup(
    name='WannierOwl',
    version=__version__,
    description='Add Spin-orbit Coupling to Wannier Hamiltonian',
    long_description=long_description,
    author='Andrey Rybakov',
    author_email='rybakov.ad@icloud.com',
    license='MIT license',
    url='https://github.com/adrybakov/WannierOwl',
    download_url='https://github.com/adrybakov/WannierOwl.git',
    packages=find_packages(),
    scripts=[

    ],
    install_requires=[
        'numpy', 'matplotlib'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
