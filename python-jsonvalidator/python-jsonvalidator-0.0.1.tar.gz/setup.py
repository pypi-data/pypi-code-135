import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-jsonvalidator",
    version="0.0.1",
    author="Murunga Kibaara",
    author_email="matatamatata3@gmail.com",
    description="""
    This package helps you validate
    dictionaries against a defined schema
    """,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/murungakibaara/jsonvalidator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
