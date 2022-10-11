from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="salary_setter_package",
    version="0.0.1",
    author="João Gabriel Barbosa",
    author_email="joaogcb29@gmail.com",
    description="This package includes two functions that calculates both increasement or decreasement of values.",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.0'
)
