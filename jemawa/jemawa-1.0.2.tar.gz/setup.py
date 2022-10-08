from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="jemawa",
    url="https://github.com/k1m0ch1/jemawa-menti-choices-spammer",
    author="k1m0ch1",
    version='1.0.2',
    description="Python CLI tool that spam the mentimeter live vote",
    packages=find_packages(),
#    long_description_content_type='text/markdown',
#    long_description=long_description,
    entry_points='''
    [console_scripts]
    jemawa=jemawa.cli:main
    ''',
    install_requires=['requests'],
)
