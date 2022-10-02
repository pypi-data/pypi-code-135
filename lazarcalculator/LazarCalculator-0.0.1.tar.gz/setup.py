from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
]

setup(name='LazarCalculator',
      version='0.0.1',
      description='Very simple calculator',
      author='Alex Arseniev',
      author_email='aagueorguiev@gmail.com',
      license='MIT',
      url='',
      classifiers=classifiers,
      keywords='calculator',
      packages=find_packages(),
      install_requires=['']
      )
