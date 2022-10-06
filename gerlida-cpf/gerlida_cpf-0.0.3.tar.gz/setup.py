from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gerlida_cpf",
    version="0.0.3",
    author="Renato Lage",
    author_email="renato.lage85@gmail.com",
    description="Gerador e verificador de CPFs",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/renatolage/dio-bootcamp-unimed-data-science",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)