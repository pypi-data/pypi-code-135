from setuptools import setup

from os import path

def fetch_long_description():
    """Loads the `long_description` from README.md."""
    this_directory = path.abspath(path.dirname(__file__))
    try:
        with open(path.join(this_directory, 'README.md'), encoding='utf-8') as readme_file:
            return readme_file.read()
    except FileNotFoundError:
        return 'See https://github.com/PGecom/python-pg-sdk'

setup(
    name="pgrwpy",
    version="0.1.4",
    description="PG Rewards python SDK",
    long_description=fetch_long_description(),
    long_description_content_type='text/markdown',
    author="Stanley Castin",
    author_email="stanleycastin19@gmail.com",
    license="MIT",
    project_urls={
        'Documentation': 'https://github.com/PGecom/python-pg-sdk/blob/main/README.md',
        'Source': 'https://github.com/PGecom/python-pg-sdk',
    },
    install_requires=["requests"],
    extras_require={
        'test': ['responses'],
    },
    include_package_data=True,
    package_dir={'pgrwpy': 'pgrwpy',
                 'pgrwpy.resources': 'pgrwpy/resources',
                 'pgrwpy.constants': 'pgrwpy/constants'},
    packages=['pgrwpy', 'pgrwpy.resources', 'pgrwpy.constants'],
    keywords='PGREWARDS payment moncash CC',
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",

        # List of supported Python versions
        # Make sure that this is reflected in .travis.yml as well
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
