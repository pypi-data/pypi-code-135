from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Information Technology',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='DocxpressoSDK',
  version='1.0.1',
  description='SDK package',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://docxpresso.com',  
  author='Docxpresso',
  author_email='eduardo@docxpresso.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Docxpresso SDK', 
  packages=['DocxpressoSDK'],
  install_requires=[''] 
)   