from setuptools import setup, find_packages

setup(
    name='contractbookauto',
    version='0',
    license='MIT',
    author="Dat Nguyen",
    author_email='datnguyentien0311@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/imtiendat0311/ContactBookAuto/',
    keywords='contractbook auto',
    install_requires=[
          'selenium>=4.5.0',
          'pandas>=1.5.0'
      ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]

)
