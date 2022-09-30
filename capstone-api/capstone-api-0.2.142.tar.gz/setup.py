import setuptools

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='capstone-api',
    version='0.2.142',
    author='Teddy Katayama',
    author_email='katayama@udel.edu',
    description='Unofficial Python Wrappers and Utilities for UD Capstone_Api Class',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkatayama/capstone_api',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'capstone=capstone_api.bin.__main__:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
