# This file is part of GasBlowdownCalculator.
from setuptools import setup, find_packages


setup(
    name='gasblowdowncalculator',
    version='0.0.5',
    description='GasBlowdownCalculator',
    long_description='GasBlowdownCalculator',
    author='Michael Fischer',
    author_email='mfischer.sw@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.7, <4',
    entry_points={
        'console_scripts': [
            'gasblowdowncalculator=gasblowdowncalculator:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/mfischersw/GasBlowdownCalculator/',
    }
)
