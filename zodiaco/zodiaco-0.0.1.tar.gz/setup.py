from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="zodiaco",
    version="0.0.1",
    author="Julio Cesar Bueno de Oliveira",
    author_email="jcboliveira@gmail.com	",
    description="Determina seu signo com base na sua data de nascimento",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcbdoliveira/pacotes-python-DIO-Bootcamp-Unimed-BH",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)