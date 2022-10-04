from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package",
    version="0.1.0",
    author="Jucicarla Pires",
    author_email="jucipires@gmail.com",
    description="Criação de pacotes de processamento de imagens em Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jucicarla/criacao_de_pacotes_processamento_imagens_Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)