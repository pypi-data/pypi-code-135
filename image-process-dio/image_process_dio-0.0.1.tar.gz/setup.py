from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_process_dio",
    version="0.0.1",
    author="glauciodrumond",
    author_email="glauciotad@gmail.com",
    description="Test package for image processing",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glauciodrumond/unimed-datascience/IMAGE_PROCESS_PKG",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.7',
)