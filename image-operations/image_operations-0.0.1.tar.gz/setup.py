from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_operations",
    version="0.0.1",
    author="celso",
    author_email="celsolearner@gmail.com",
    description="Exercice about packages - Bootcamp Data Science Unimed",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/celsolearner/image-operations",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.0',
)
