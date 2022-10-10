# Copyright (c) 2022 Katsuaki Higashimori

from setuptools import setup
import rhsolpy

DESCRIPTION = "rhsolpy: Rankine-Hugoniot relation solver for anisotropic plasmas"
NAME = 'rhsolpy'
AUTHOR = 'Katsuaki Higashimori'
AUTHOR_EMAIL = 'k.higashimori@gmail.com'
URL = 'https://github.com/kx198x/rhsolpy'
LICENSE = 'BSD 3-Clause'
DOWNLOAD_URL = 'https://github.com/kx198x/rhsolpy'
VERSION = rhsolpy.__version__
PYTHON_REQUIRES = ">=3.7"

"""
INSTALL_REQUIRES = [
    'matplotlib>=3.3.4',
    'seaborn>=0.11.0',
    'numpy >=1.20.3',
    'pandas>=1.2.4',
    'matplotlib>=3.3.4',
    'scipy>=1.6.3',
    'scikit-learn>=0.24.2',
]

EXTRAS_REQUIRE = {
    'tutorial': [
        'mlxtend>=0.18.0',
        'xgboost>=1.4.2',
    ]
}

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Multimedia :: Graphics',
    'Framework :: Matplotlib',
]

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts
"""
PACKAGES = [
    'rhsolpy'
]
with open('README.md', 'r') as rf:
    readme = rf.read()

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description_content_type="text/markdown",
      long_description=readme,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      #install_requires=INSTALL_REQUIRES,
      #extras_require=EXTRAS_REQUIRE,
      packages=PACKAGES#,
      #classifiers=CLASSIFIERS
    )