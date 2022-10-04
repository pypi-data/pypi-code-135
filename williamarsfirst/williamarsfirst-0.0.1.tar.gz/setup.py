from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A basic hello package'

# Setting up
setup(
    name="williamarsfirst",
    version=VERSION,
    author="William Arsenault",
    author_email="idk@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)