from setuptools import setup, find_packages

setup(
    name='split_csv_into',
    version='1.0',
    description='Given a path to a csv file will split the csv into three subsets containing specified percentages of the full csv',
    author='Jack Geraghty',
    install_requires=['pandas', 'numpy'],
    author_email='jgeraghty049@gmail.com',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['split_csv=split_csv.split_csv:main'],
    },
    zip_safe=False
)