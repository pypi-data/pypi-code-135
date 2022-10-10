from setuptools import setup

with open ("README.md") as f:
	long_description = f.read()
setup(name='VCFRIDER',
version='1.0.0',
description='VCFRIDER python for VCF data analysis',
url='https://github.com/sasurasa/VCFRIDER/tree/main.',
author='Surasak Sangkhathat',
author_email='s.sangkhathat@gmail.com',
license='Prince of Songkla University',
packages=['VCFRIDER'],
zip_safe=False,
long_description=long_description,
    long_description_content_type='text/markdown'
)