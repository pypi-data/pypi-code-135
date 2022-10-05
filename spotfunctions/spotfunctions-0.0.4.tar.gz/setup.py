from setuptools import setup, find_packages

setup(
    name='spotfunctions',
    version='0.0.4',
    author='Jacopo Rota',
    description='Python SDK for SpotFunctions',
    long_description='Python SDK to write SpotFunctions in Python',
    url='https://github.com/r00ta/SpotFunctions',
    keywords='development, setup, spotfunctions',
    python_requires='>=3.6',
    packages=find_packages(include=['spotfunctions', 'spotfunctions.*']),
    install_requires=[
        "Flask==2.0.3",
        "kafka-python==2.0.2",
        "waitress==2.0.0"
    ]
)