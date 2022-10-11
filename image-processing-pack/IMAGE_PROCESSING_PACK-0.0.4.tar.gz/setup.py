# O Codigo apresentado durante a atividade é de autoria de Karine Kato e fou apresentado com intuito pedagogico
#  Nesta parte do setup devemos inserir as informações gerais sor=bre o pacote
#

from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="IMAGE_PROCESSING_PACK",
    version="0.0.4",
    author="Gilcimar Gomes",
    author_email="aguiar.gilcimar@gmail.com",
    description="Version for test, processing to image - Project development by Karina Kato - teacher for DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gil-uai/DIO-Gera-o-Tech-Unimed/tree/main/CAP_02-Python/02_Projetos/Pacotes/IMAGE_PROCESSING_PACK",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)