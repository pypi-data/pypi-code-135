from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='csv_from_root',
    version='1.0',
    description='From a given root directory will generate a csv file containing the files present in each subdir with respect to a given main_dir',
    author='Jack Geraghty',
    install_requires=['pandas'],
    author_email='jgeraghty049@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['csv_from_root=csv_from_root.csv_from_root:main'],
    },
    zip_safe=False
)