from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="password_maker",
    version="0.0.2",
    author="Ruham Leal",
    author_email="ruhamxlpro@hotmail.com",
    description="A module that generates a random password",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RuhamLeal/making_package_module",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)