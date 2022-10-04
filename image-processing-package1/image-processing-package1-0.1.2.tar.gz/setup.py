from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package1",
    version="0.1.2",
    author="Jucicarla Pires",
    author_email="jucipires@gmail.com",
    description="Criação de pacotes de processamento de imagens em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jucicarla",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)