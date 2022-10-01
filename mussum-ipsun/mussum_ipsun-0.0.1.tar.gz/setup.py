from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mussum_ipsun",
    version="0.0.1",
    author="MarkCiano",
    author_email="marcianopazinatto@gmail.com",
    description="Mussum Ipsun generate.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarcianoPazinatto/mussum-ipsun-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)