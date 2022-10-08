from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='ROBLOAPI',
  version='0.0.1',
  description='A ROBLOX to Python API wrapper',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Jacks Productions',
  author_email='jackbusinessac@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='roblox', 
  packages=find_packages(),
  install_requires=[''] 
)