from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text(encoding='utf-8')

setup(
    name='pandas-nosql',
    version='0.0.1',
    description='A Module to add read and write capabilities to pandas for several nosql databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://bitbucket.org/blacklotus231/pandas-nosql',
    author='James Baker Jr',
    install_requires=['pandas>=1.4.4', 'pymongo>=4.2.0', 'elasticsearch>=8.4.0', 'redis-py>=4.3.4', 'cassandra-driver>=3.25.0'],
    keywords=['pandas', 'nosql', 'mongo', 'mongodb', 'elasticsearch', 'redis', 'cassandra', 'apache-cassandra'],
    license='Apache License 2.0',
    python_requires='>=3.9',
    packages=['pandas_nosql'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)