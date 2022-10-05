from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package-gabriel-pereira",
    version="0.0.1",
    author="Gabriel",
    author_email="pereissgabriel@gmail.com",
    description="Teste para criar pacotes DIO.me",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabbrielpereira/learningpython/package-gabriel-pereira",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)