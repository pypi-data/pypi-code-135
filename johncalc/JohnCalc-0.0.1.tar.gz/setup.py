from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3' 
]

setup(
    name = 'JohnCalc',
    version='0.0.1',
    description='A basic calculation function',
    long_description=open('ReadMe.txt').read()+'\n\n'+open('ChangeLOG.txt').read(),
    url='',
    author='Paul John Maddala',
    author_email='maddalapauljohn@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Calculations',
    packages=find_packages(),
    install_requires=['']
)