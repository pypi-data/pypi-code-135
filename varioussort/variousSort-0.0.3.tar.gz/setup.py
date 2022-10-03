from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="variousSort",
    version="0.0.3",
    author="Ilya Marshev",
    author_email="ismarshev@gmail.com",
    description="Various sorting algorithms in one library, ranging from slow bubble sorting to the fastest single-row sorting.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/IsMarshevs/VariousSort",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)