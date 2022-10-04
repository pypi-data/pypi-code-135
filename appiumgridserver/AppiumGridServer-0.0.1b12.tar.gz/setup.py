from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='AppiumGridServer',
    version='0.0.1b12',
    description='ChokChaisak',
    long_description=readme(),
    url='https://test.pypi.org/user/ChokChaisak/',
    author='ChokChaisak',
    author_email='ChokChaisak@gmail.com',
    license='ChokChaisak',
    install_requires=[
        'matplotlib',
        'numpy',
        'nodejs-bin',
        'install-jdk>=0.3.0',
        'robotframework-AppiumLibrary',
        'psutil',
    ],
    keywords='AppiumGridServer',
    packages=['AppiumGridServer'],
    package_dir={
    'AppiumGridServer': 'src/AppiumGridServer',
    },
    package_data={
    'AppiumGridServer': ['*'],
    },
)