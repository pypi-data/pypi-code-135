import os
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='syngenta_digital_uoms',
    version=os.getenv('CIRCLE_TAG'),
    url='https://github.com/syngenta-digital/package-python-uoms.git',
    author='Jeff Payne, Syngenta Digital',
    author_email='jeffrey.payne@syngenta.com',
    description='Standardized hub for unit of measure conversions across systems and dimensions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={"": ["*.xlsx"]},
    python_requires='>=3.0',
    install_requires=[
        'pandas',
        'openpyxl'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)