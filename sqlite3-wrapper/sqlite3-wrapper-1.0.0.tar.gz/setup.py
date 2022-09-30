from setuptools import setup

# Package meta-data.
NAME = 'sqlite3-wrapper'
DESCRIPTION = 'SQLite3 Wrapper'
URL = 'https://github.com/moodoid/sqlite3-wrapper'
AUTHOR = 'moodoid'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'

setup(
    name='sqlite3-wrapper',
    version='1.0.0',
    author='moodoid',
    keywords='Sqlite3 Controller',
    packages=['sqlite_wrapper'],
    description='Sqlite3 Controller',
    long_description='Interface with sqlite files',
    long_description_content_type='text/plain',
    url='https://github.com/moodoid/sqlite3-wrapper',
    classifiers=['Intended Audience :: Developers',
                 ]
)