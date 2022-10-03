from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processador_de_imagem_ptbr",
    version="0.0.3",
    author="Gabriel Calasans",
    author_email="andersongabriel08@gmail.com",
    description="Meu pacote de processamento de imagem usando skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndersonGabrielCalasans/pacote-processador-de-imagem-ptbr",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)