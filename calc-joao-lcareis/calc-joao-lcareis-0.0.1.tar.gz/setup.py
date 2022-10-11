from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calc-joao-lcareis",
    version="0.0.1",
    author="JoaoLucio",
    description="Mini Calculadora",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoaoLucio1204/Pacotes",
    packages=find_packages(),
    python_requires='>=3.8',
)