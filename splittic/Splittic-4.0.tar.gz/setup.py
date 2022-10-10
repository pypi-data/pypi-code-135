from setuptools import setup

setup(
    name='Splittic',
    url='https://github.com/Dart2004/Splittic-AI',
    author='Daniel Klimmer',
    author_email='danielklimmer2000@protonmail.com',
    packages=['splitticai'],
    install_requires=['requests', 'bs4', 'base64'],
    version='4.0',
    license='MIT',
    description='The Most Advanced AI Ever',
    long_description=open('README.rst','r').read()
)
