from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="my_first_package_project_dio",
    version="0.0.1",
    author="Leone",
    author_email="leonedeola@gmail.com",
    description="Pacote com algoritmo simples para testar empacotamento",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leodeola/my_first_package_project_dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
