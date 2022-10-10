import setuptools

setuptools.setup(
    name = 'snes_scrub',
    version = '0.1.0',
    url = 'https://github.com/markmahoney/snes_scrub',
    author = 'Mark Mahoney',
    author_email = 'bcmark@gmail.com',
    description = 'Strip SMC headers and rename SNES ROM files using no-intro.org data and naming conventions',
    long_description = open('README.md').read(),
    python_requires = '>=3',
    packages = setuptools.find_packages('src'),
    package_dir = {'':'src'},
    include_package_data = True,
    package_data = {'': ['*.dat']},
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [
            'snes_scrub=snes_scrub:main',
        ],
    },    
)
