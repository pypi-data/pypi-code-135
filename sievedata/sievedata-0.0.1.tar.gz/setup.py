from setuptools import setup, find_packages

VERSION = "0.0.1"

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sievedata',
    version=VERSION,
    description='Sieve CLI and Python Client',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Sieve Team',
    author_email='developer@sievedata.com',
    url='https://github.com/sieve-data/sieve',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=[
        "requests>=2.0",
        "click>=8.0",
        "pydantic>=1.8.2",
    ],
    entry_points={
        'console_scripts': [
            'sieve = cli.sieve:cli',
        ]
    }
)
