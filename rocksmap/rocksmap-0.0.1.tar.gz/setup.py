try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = [
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Development Status :: 3 - Alpha",
    "Operating System :: OS Independent",
]

with open("README.md", "r") as fp:
    long_description = fp.read()

test_requirements = ["pytest-notebook", "ipython_genutils"]
setup(name="rocksmap",
      version="0.0.1",
      author="Michael Tartre",
      author_email="mtartre@gmail.com",
      url="https://github.com/quantology/rocksmap",
      py_modules=["rocksmap"],
      install_requires=[
        #"lbry-rocksdb>=0.8.2",
        "python-rocksdb",
      ],
      description="MutableMapping interface for RocksDB",
      long_description=long_description,
      long_description_content_type='text/markdown',
      license="bsd-3-clause",
      classifiers=classifiers,
)
