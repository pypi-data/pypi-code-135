from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='solNFT',
  version='0.0.1',
  description='Basic solana NFT tools.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Yahia Shaker',
  author_email='yahiashaker1@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='python',
  packages=find_packages(),
  install_requires=['bs4']
)