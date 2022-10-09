from setuptools import setup, find_packages

VERSION = '0.0.12'
DESCRIPTION = 'Type Analysis tool for Pandas DataFrames'
LONG_DESCRIPTION = 'A package that helps data analysts, engineers, and scientists to efficiently identify the data type distribution in a pandas dataframe'

# Setting up
setup(
    name="typalizer",
    version=VERSION,
    author="Mursil Khan",
    author_email="<mursilkhan30@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas'],
    keywords=['python', 'data', 'analysis', 'type analysis', 'pandas', 'dataframes'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)