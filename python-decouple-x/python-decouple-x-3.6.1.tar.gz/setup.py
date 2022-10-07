# coding: utf-8
from setuptools import setup
import os


README = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(name='python-decouple-x',
      version='3.6.1',
      description='Strict separation of settings from code.',
      long_description=open(README).read(),
      author="Henrique Bastos", author_email="henrique@bastos.net",
      license="MIT",
      install_requires=['python-dotenv', 'PyYAML'],
      py_modules=['decouple'],
      zip_safe=False,
      platforms='any',
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Django',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries',
      ],
      url='http://github.com/henriquebastos/python-decouple/',)
