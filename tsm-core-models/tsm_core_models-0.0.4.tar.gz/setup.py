from setuptools import find_packages, setup

setup(
    name='tsm_core_models',
    packages=find_packages(include=['tsm_core_models']),
    version='0.0.4',
    description='Core Model library for The Social Matrix',
    author='Michael Duboc',
    license='MIT',
    install_requires=['django>=4.0.3', 'py2neo>=2021.2.3'],
)