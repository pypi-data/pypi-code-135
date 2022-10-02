from setuptools import setup

version = '0.0.3'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pflib',
    version=version,
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Simple library for send metric into pushgateway',
    author='OldTyT',
    url='https://github.com/OldTyT/pflib',
    install_requires=["urllib3"],
    packages=['pflib'],
)
