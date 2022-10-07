from setuptools import find_packages, setup

setup(
    name='Any Dice Simulator',
    packages=find_packages(include=['anyDiceSimulator']),
    version='0.0.1',
    description='Python library to roll dice!',
    author='Saksham Gupta',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)