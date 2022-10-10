try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
    name='ranged_number',
    version="1.0.0",
    license='MIT', 
    classifiers=classifiers,
    description="number with limits in python",
    author="Noam Avned",
    packages=[
        'rangednumber',
    ],
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
)
