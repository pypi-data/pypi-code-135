from setuptools import find_packages, setup

setup(
    name='antcat-py',
    packages=find_packages(include=['antcat', 'api']),
    version='0.1.0',
    description='AntCat.org API Access in Python.',
    author="Richard Makey",
    url='https://github.com/injawoogie/antcat-py.git',
    author_email='injawoogie@icloud.com',
    license='MIT',
    install_requires=['requests'],
    setup_requires=['pytest-runner', 'requests'],
    tests_require=['pytest==4.4.1', 'requests'],
    keywords='antcat catalog taxonomic',
    test_suite='tests',
)