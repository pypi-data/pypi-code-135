from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get_random_people",
    version="1.1.2",
    description="Generates random information of a person",
    author = "Ata Shaikh, Nicholes Viktor, InternetWebSoftwares",
    author_email="atasteven49@gmail.com",
    url="https://github.com/internetwebsoftwares/get_random_people.git",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    packages=setuptools.find_packages(),
    keywords=["random", "fake", "dataset", "user data", "fake data", "user information", "python", "generate data", "generate fake data", "users"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
    py_modules=["get_random_people", "countries", "countries_capital", "get_name_gender_religion","names", "qualifications", "utils"],
    package_dir={"": "src"},
    install_requires=[],
    include_package_data=True
)