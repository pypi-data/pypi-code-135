import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyspinners",                     # This is the name of the package
    version="0.0.3",                        # The initial release version
    author="Ioannis Tsimpiris",                     # Full name of the author
    description="CLI Progress Spinner collection",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  
    url = "https://github.com/tsimpiris/PySpinners",
    project_urls = {
        "Repository": "https://github.com/tsimpiris/PySpinners",
    },                                    # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["pyspinners"],             # Name of the python package
    package_dir={'':'pyspinners/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)
