from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ola-mundo-pack",
    version="0.0.1",
    author="Jefferson",
    author_email="jefferson772@hotmail.com",
    description="Criar uma aplicação e empacotar",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JeffersonMarioto/ola-mundo-pack.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    setup_requires=['wheel'],
)