from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

setup(
    name="pybisol",
    version="0.1.0",
    author="Eniz Museljic",
    author_email="eniz.m@outlook.com",
    description="Python wrapper module for a c++ implementation of superconducting coil field solver",
    ext_modules = cythonize([Extension("pybisol", ["pybisol.pyx"])]),
    include_dirs = [numpy.get_include()],
    install_requires=["numpy", "cython"],
    keywords=["team22", "solenoid", "solver"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)