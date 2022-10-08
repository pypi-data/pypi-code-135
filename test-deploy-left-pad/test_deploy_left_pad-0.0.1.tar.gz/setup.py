from setuptools import setup

with open('README.md', 'r') as f:
  long_description = f.read()


setup(
  name='test_deploy_left_pad',
  version='0.0.1',
  description='just add left padding to the text.',
  py_modules=['left_pad'],
  package_dir={'': 'src'},
  author='Mhmd',
  author_email='d3v.mhmd@gmail.com',
  url='https://ninja-bag.devmhmd.com',

  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  long_description=long_description,
  long_description_content_type='text/markdown',
  install_requires = [],
  extras_require = { 'dev': [ 'pytest>=3.7' ] }
)

