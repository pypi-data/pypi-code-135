from setuptools import setup

with open('DESCRIPTION.txt') as file:
    long_description = file.read()

VERSION = '0.0.3'
DESCRIPTION = 'Random Password Generator'

# Setting up
setup(
    name="robust-password-generator",
    version=VERSION,
    author="Raviteja S",
    author_email="<ravitejats18@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    url='https://github.com/ravitejasravi/robust-password-generator',
    license='MIT',
    packages=['password_generator'],
    install_requires=[],
    keywords=['python', 'password', 'strongpassword', 'security', 'random'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
