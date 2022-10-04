#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Alexander Kast",
    author_email='alexander.kast@mailbox.org',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="a bunch of code for data analysis",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='liquidData',
    name='liquidData',
    packages=find_packages(include=['liquidData', 'liquidData.*']),
    tests_require=test_requirements,
    url='https://github.com/Limthu/liquidData',
    version='0.1.0',
    zip_safe=False,
)
