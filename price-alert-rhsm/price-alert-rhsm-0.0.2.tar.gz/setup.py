from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="price-alert-rhsm",
    version="0.0.2",
    author="Rafael Meireles",
    author_email="rafameireles2011@gmail.com",
    description="Script to monitoring price.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafael-hsm/price_alert",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
